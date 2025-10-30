def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_one_records(client, one_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "atmosphere": "livable",
        "description": "Not livable",
        "name": "Uaranus"
    }
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "id": 1,
        "atmosphere": "livable",
        "description": "livable",
        "name": "Earth"
    })

    response_body = response.get_json() 

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "atmosphere": "livable",
        "description": "livable",
        "name": "Earth"
    }
 