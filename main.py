from algosdk.v2client import algod
from algosdk import account, mnemonic

# Step 1: Connect to Algorand TestNet (free public network)
ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN = ""  # No token needed for public node

algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

# Step 2: Generate a new test account
private_key, address = account.generate_account()
print("Your new Algorand TestNet account address is:", address)

# Step 3: Display account info
try:
    account_info = algod_client.account_info(address)
    print("Account balance:", account_info.get('amount'), "microAlgos")
except Exception:
    print("Account not found yet — fund it using the TestNet dispenser:")
    print("🔗 https://dispenser.testnet.aws.algorand.com/")

print("\n✅ Script executed successfully!")
