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