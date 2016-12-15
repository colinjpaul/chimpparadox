import requests

def test_index():
    r = requests.get('http://localhost:5000')
    assert r.status_code == 200

    #r = request('localhost:5000/todo/api/v1.0/tasks/





   
    

