from src import app as app_module


def test_signup_and_unregister_flow(client):
    # Arrange
    activity = "Chess Club"
    email = "pytest_user@example.com"

    # Act: sign up
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert: signup succeeded and participant added
    assert resp.status_code == 200
    assert email in client.get("/activities").json()[activity]["participants"]

    # Act: duplicate signup
    resp_dup = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert: duplicate attempt rejected
    assert resp_dup.status_code == 400

    # Act: unregister
    resp_un = client.delete(f"/activities/{activity}/participants", params={"email": email})
    # Assert: unregister succeeded and participant removed
    assert resp_un.status_code == 200
    assert email not in client.get("/activities").json()[activity]["participants"]

    # Act: unregister non-existent participant
    resp_not = client.delete(f"/activities/{activity}/participants", params={"email": email})
    # Assert: not found
    assert resp_not.status_code == 404


def test_unknown_activity_errors(client):
    # Arrange / Act / Assert: signup unknown activity
    resp = client.post("/activities/NoSuchActivity/signup", params={"email": "a@b.com"})
    assert resp.status_code == 404

    # Arrange / Act / Assert: unregister unknown activity
    resp = client.delete("/activities/NoSuchActivity/participants", params={"email": "a@b.com"})
    assert resp.status_code == 404
