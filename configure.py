#Configure the Tradier API

ACCESS_TOKEN = '<TOKEN>'

BASE_URL = 'https://sandbox.tradier.com'

HEADERS = {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN), 'Accept': 'application/json'}

HISTORY_URL = ''
OPTION_CHAIN_URL = '{}/v1/markets/options/chains'.format(BASE_URL)
