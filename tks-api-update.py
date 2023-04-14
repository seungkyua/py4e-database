import os
import requests
import sys

TKS_API_URL = 'http://localhost:8080'
CLUSTER_ID = 'cmibsrdnq'
APP_ID = '46e2b042-5d09-4b23-b442-e5b496816111'
TASK_ID = '663f82d8-4b75-432f-80f2-89a6e48c4fd8'
ORG_ID = 'master'
ACCOUNT_ID = 'admin'
PASSWORD = 'admin'


def getToken():
    data = {
        # 'organizationId': os.environ['ORGANIZATION_ID'],
        # 'accountId': os.environ['ACCOUNT_ID'],
        # 'password': os.environ['PASSWORD']
        'organizationId': ORG_ID,
        'accountId': ACCOUNT_ID,
        'password': PASSWORD
    }

    res = requests.post(TKS_API_URL + '/api/1.0/auth/login', json=data)
    if res.status_code != 200:
        return ''
    res_json = res.json()
    return res_json['user']['token']


TOKEN = getToken()

print(TOKEN)

uri = '/api/1.0/app-serve-apps/%s/status' % APP_ID
data = {
    'task_id': TASK_ID,
    'status': 'BUILDING',
    'output': 'Updating status is succeeded.'
}
res = requests.patch(TKS_API_URL + uri,
                     headers={"Authorization": "Bearer " + TOKEN},
                     json=data)
if res.status_code != 200:
    sys.exit('Failed to update status')

res_json = res.json()
print(res_json)
