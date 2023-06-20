# test api using pytest.
# python filename must begin with 'test'
# function name must begin with 'test'
# need to pip install pytest

# test that the end point can be called and return 200 status code

import requests

API_ENDPOINT = 'https://todo.pixegami.io'

def test_can_call_endpoint():
    get_response = requests.get(API_ENDPOINT)
    assert get_response.status_code == 200

def test_create_task():
    json_payload= {
        "content": "Hello",
        "user_id": "user1",
        "task_id": "1234",
        "is_done": False
    }
    url= API_ENDPOINT+'/create-task'
    print('url: ', url)
    create_response = requests.put(url, json=json_payload)
    assert create_response.status_code == 200
    print(create_response.json())

    task_id = create_response.json()['task']['task_id']
    print('task_id ', task_id)
    print('url: ', API_ENDPOINT+'/get-task/' + task_id)
    get_response = requests.get(API_ENDPOINT+'/get-task/' + task_id )
    assert get_response.status_code == 200

    data=get_response.json()
    print('data: ', data)
    assert data['content'] ==json_payload['content']
    assert data['is_done'] == json_payload['is_done']
    assert data['user_id'] == json_payload['user_id']
