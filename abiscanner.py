import requests
import json
import time
import os

"""
address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413&apikey=IQ2I5ITPV33933GMVI329QNIKMSDKEKDDQ
"""

# Scrapes for ABI's from Etherscan API's

class AbiScanner:

    def __init__(self):
        self.api_url = "https://api.etherscan.io/api?module=contract&action=getabi&"
        self.api_key = "IQ2I5ITPV33933GMVI329QNIKMSDKEKDDQ"
        self.obj_per_file = 10
        self.sleep_time = 0.3  # Sleep between requests because etherscan will block if more than 5 requests in 1 sec

    @property
    def erc_contracts(self):
        return self.get_contracts_array(file="erc.txt")

    @property
    def non_erc_contracts(self):
        return self.get_contracts_array(file="non_erc.txt")

    def get_contracts_array(self, file="erc.txt"):
        with open(file, "r") as contract_file:
            contracts = contract_file.read().splitlines()
            contract_file.close()
            return contracts

    def get_abi(self, contract_address):
        url = self.get_api_url(contract_address)
        r = requests.get(url)
        obj = r.json()
        if (obj["message"] == "OK"):
            return obj.get("result", "")
        else:
            return ""

    def get_api_url(self, contract_address):
        return self.api_url + "address="+ contract_address + "&apikey=" + self.api_key

    def write_json(self, directory, file_name, json_data):
        if not os.path.isdir(directory):
            os.mkdir(directory)
        with open(os.path.join(directory, file_name), 'w') as outfile:
            json.dump(json_data, outfile)
            print("writing the file " + file_name)
            outfile.close()

    def get_file_name(self, contract_type, index):
        return contract_type+str(index)+".json"

    def write_json_files(self, contract_type, directory):
        selected = self.erc_contracts if contract_type == "erc" else self.non_erc_contracts
        contracts_2d = [selected[p:p + self.obj_per_file] for p in range(0, len(selected), self.obj_per_file)]
        for i, contracts in enumerate(contracts_2d):
            data = []
            print(contracts)
            for contract_address in contracts:
                data.append({contract_address: self.get_abi(contract_address)})
                time.sleep(0.3)
            self.write_json(directory, self.get_file_name(contract_type, i), data)


if __name__ == "__main__":
    abi_scanner = AbiScanner()
    print(len(abi_scanner.erc_contracts))
    print(len(abi_scanner.non_erc_contracts))
    # abi_scanner.write_json_files("erc", "erc_contracts")
    # abi_scanner.write_json_files("non_erc", "non_erc_contracts")