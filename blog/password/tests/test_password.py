
def test_generate(client):
    response = client.post('/password/generate', json={
        'lowercase': True
    })

    assert response.status_code, 200
    assert type(response.json), list


def test_request_without_json(client):
    response = client.post('/password/generate')
    assert response.status_code, 400


def test_request_with_all_false(client):
    response = client.post('/password/generate', json={
        'lowercase': False,
        'uppercase': False,
        'number': False,
        'symbol': False
    })

    assert response.status_code, 400
