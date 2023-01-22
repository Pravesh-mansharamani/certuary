import os
#import
import requests
from dotenv import load_dotenv
import pestuary as pest

load_dotenv()  # take environment variables from .env.
API_KEY = os.getenv("API_KEY")
print(API_KEY)
# url = "https://api.estuary.tech/content/add"
#
# files = [
#   ('data', ('file', open('/Users/edisonqu/PycharmProjects/certuary/haha.txt', 'rb'),
#             'application/octet-stream'))
#   ]
#
# # files=open('/Users/edisonqu/PycharmProjects/certuary/haha.txt', 'rb')
# payload={}
# headers = {
#   'Content-Type': 'multipart/form-data',
#   'Accept': 'application/json',
#   'Authorization': f'Bearer {API_KEYS}'
#
#
# }
# Body= {
#   "data": files,
#   'filename': "george."
# }
#
#
# response = requests.request("POST", url, headers=headers, data=payload, files=files)
#
#
# print(response.text)

# pest.Pestuary(estuary_key=API_KEY)
#
# from pestuary import content
#
#
# content.content_add("/Users/edisonqu/PycharmProjects/certuary/haha.txt")
#
# print(os.getenv('API_KEY'))
import requests
url = "https://api.estuary.tech/content/add"
payload={}
files=[
  ('data',('file',open('/Users/edisonqu/PycharmProjects/certuary/haha.txt','rb'),'application/octet-stream'))
]
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json',
  'Authorization': 'Bearer ESTf4be2f1c-dd16-4813-a6d5-0dad7ec0b0d3ARY'
}
response = requests.request("POST", url, headers=headers, data=payload, files=files)
print(response.text)


