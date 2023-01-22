import os
import requests
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
API_KEY = os.getenv("API_KEY")

FILENAME="/Users/edisonqu/Downloads/anna_library1.jpg"
url = "https://api.estuary.tech/content/add"

name = 'anna_edison'
payload={}
files=[
  ('data',(f'{name}',open(FILENAME,'rb'),'application/octet-stream'))
]
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer ESTf4be2f1c-dd16-4813-a6d5-0dad7ec0b0d3ARY'
}


response = requests.request("POST", url, headers=headers, data=payload, files=files)


print(response.text)