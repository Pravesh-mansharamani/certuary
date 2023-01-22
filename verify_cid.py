

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

print(verify_cid('bafkreigbd5f56mztpwnlkghlkxb7r2fmmpdky3prbroxpqcxdkiqqaq6wu'))
