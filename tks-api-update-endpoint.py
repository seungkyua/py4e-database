import os
import requests
import sys

TKS_API_URL = 'http://ac58c15ff852a459bbb77a7b2e46a5d7-1088998339.ap-northeast-2.elb.amazonaws.com:9110'
CLUSTER_ID = 'cmibsrdnq'
APP_ID = '5f65be87-977d-4d00-a57c-4acb3e44000f'
TASK_ID = 'b0aad96b-79f1-4d3e-b659-49dbb55ff2ae'
ENDPOINT_URL = 'https://endpoint_url'
PREVIEW_ENDPOINT_URL = 'https://preview_endpoint_url'
HELM_REVISION = '1'
ORG_ID = 'master'
ACCOUNT_ID = 'admin'
PASSWORD = 'admin'

print(f'TKS_API_URL={TKS_API_URL}, APP_ID={APP_ID}, TASK_ID={TASK_ID}, ENDPOINT_URL={ENDPOINT_URL}, '
      f'PREVIEW_ENDPOINT_URL={PREVIEW_ENDPOINT_URL}, HELM_REVISION={HELM_REVISION}')


def getToken():
    data = {
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

uri = '/api/1.0/app-serve-apps/%s/endpoint' % APP_ID
data = {
    'task_id': TASK_ID,
    'endpoint_url': ENDPOINT_URL,
    'preview_endpoint_url': PREVIEW_ENDPOINT_URL,
    'Helm_revision': int(HELM_REVISION)
}
res = requests.patch(TKS_API_URL + uri,
                     headers={"Authorization": "Bearer " + TOKEN},
                     json=data)
if res.status_code != 200:
    print(res.reason)
    sys.exit('Failed to update status')

res_json = res.json()
print(res_json)
