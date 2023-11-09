import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.environ.get('API_KEY')
print('hello world')
print(api_key)