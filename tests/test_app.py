def test_root_redirect(client):
    # Arrange
    url = "/"
    # Act
    resp = client.get(url, follow_redirects=False)
    # Assert
    assert resp.status_code == 307
    assert resp.headers["location"].endswith("/static/index.html")


def test_get_activities(client):
    # Arrange
    url = "/activities"
    # Act
    resp = client.get(url)
    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
