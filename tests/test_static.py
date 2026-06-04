def test_index_html_served(client):
    # Arrange
    url = "/static/index.html"
    # Act
    resp = client.get(url)
    # Assert
    assert resp.status_code == 200
    assert "Mergington High School" in resp.text


def test_app_js_served(client):
    # Arrange
    url = "/static/app.js"
    # Act
    resp = client.get(url)
    # Assert
    assert resp.status_code == 200
    assert "fetchActivities" in resp.text or "DOMContentLoaded" in resp.text
