import pytest
from rest_framework import status


@pytest.mark.django_db
def test_unauthorized_request(api_client):
    url = '/api/v1.0/users/'
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, f"Expected 401, got {response.status_code}"
