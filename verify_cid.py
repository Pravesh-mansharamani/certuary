import requests


# Get CID from the frontend
def verify_cid(CID):
    headers = {
        'Content-Type': 'multipart/form-data',
        'Accept': 'application/json'
    }
    url = f'https://api.estuary.tech/public/by-cid/{CID}'
    response = requests.request('GET',url=url,headers=headers)

    return response.text

# print(verify_cid('bafkreib2f2diqig2yqjpopdpb2jgxeyuimfgbua2m4ipinu2x5o3izj25q'))
print(verify_cid('bafybeie5begtaycfhqkuiekqob6pjbi4eb3wcv475jalmp7h326npl2ixi'))