import logging
import kiteconnect
# just for checking import gone right
logging.basicConfig(level=logging.DEBUG)

# Initialise
#kws = KiteTicker("your_api_key", "your_access_token")

print("No problem.. you can proceed")

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
#kws.connect()