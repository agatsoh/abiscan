# ABI Scanner

This `abiscanner.py` scrapes through the contract addresses in `erc.txt` and `non_erc.txt` for their ABI's using the ethereum etherscan API's. You need to have a API Key to call the etherscan API's which you can easily register on the ethereum etherscan.

Just call the `write_json_files` using `contract_type` `erc` or `non_erc` and the program will create multiple JSON files in the `erc_contracts` and the `non_erc_contracts` folders.

You can change or customize the program in the following way:
1. Change `self.api_key` variable to change it to your key
2. Change `self.obj_per_file` variable to a different value to change the number
   Objects recorded per json file
