import requests
import json

def generate_request(url, params={}):
    response = requests.post(url, params=params)

    if response.status_code == 200:
        return response.json()

def send_trashed(params={}):
    response = generate_request('https://randomuser.me/api', params)
    if response:
       user = response.get('results')[0]
       return user.get('name').get('first')

    return ''    

def get_api(params = {}):
    header =  {"Content-Type":"application/json", "Authorization": f"Bearer {get_token()}"}
    url_send = 'https://matis-uat.ovam.be/api/meldingen/verwerking'    

    try:
        response = requests.post(url = url_send, headers=header, data=json.dumps(params))
    except Exception as e:
        print(e)

    res = response.json()
    

    response_detail ={
        'status' : response,
        'input': res[0]['input'],
        'errors': res[0]['errors'],
        'referentie': res[0]['referentie'],
        'versie': res[0]['versie'],
        'geldig': res[0]['geldig']
    }

    return response_detail

def get_token():
    values = {
        "client_id": 'b5500dc6-6927-49be-9fc6-9386f4d683e2',
        "client_secret": 'H7YNWKeLk3yhCIrXtmPvzKEYGl1Ie0yp',
        "grant_type": 'client_credentials'
    }

    url_send = 'https://login-uat.ovam.be/auth/realms/ovam/protocol/openid-connect/token'

    try:
        req = requests.post(url = url_send, data = values ).json()
        return req.get('access_token')
    except Exception as e:
        print(e)
