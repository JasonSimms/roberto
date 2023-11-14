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
history = company.history(interval='weekly', start='2023-05-01', end='2023-11-13')
# print(history.open())
historical_data = history.close()
print(historical_data)

def calculate_rsi(data, period=14):
    # Example usage with the provided data
    # historical_data = {'2011-01-01': 11.63, '2011-02-01': 12.189286, '2011-03-01': 12.695357, '2011-04-01': 12.539643, '2011-05-01': 12.490714, '2011-06-01': 12.459643, '2011-07-01': 11.998214, '2011-08-01': 14.206429, '2011-09-01': 13.779286, '2011-10-01': 13.584643, '2011-11-01': 14.193214, '2011-12-01': 13.662143, '2012-01-01': 14.621429}

    closes = list(data.values())[-period:]

    # Calculate price changes
    changes = [closes[i] - closes[i-1] for i in range(1, len(closes))]

    # Separate positive and negative changes
    up_changes = [change for change in changes if change > 0]
    down_changes = [abs(change) for change in changes if change < 0]

    # Calculate average gain and average loss
    avg_gain = sum(up_changes) / period if up_changes else 0
    avg_loss = sum(down_changes) / period if down_changes else 0

    # Calculate relative strength (RS)
    rs = avg_gain / avg_loss if avg_loss != 0 else 0

    # Calculate RSI
    rsi = 100 - (100 / (1 + rs))

    return rsi


rsi_result = calculate_rsi(historical_data)
print(f"RSI: {rsi_result}")