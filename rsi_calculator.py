import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

token = os.environ.get('TRADIER_ACCESS_TOKEN_PAPER')
account_id = os.environ.get('TRADIER_ACCOUNT_NUMBER_PAPER')
endpoint = 'developer_sandbox'

from pytradier.tradier import Tradier
# Authenticate with the API. Historical data requires a brokerage account.
tradier = Tradier(token, account_id, endpoint)

# historical prices come from the Company class. choose which company's data to model:
company = tradier.company(symbol='AAPL')

# get the historical prices between 2011 and 2012
history = company.history(interval='monthly', start='2011-01-01', end='2012-01-01')
print(history.open())