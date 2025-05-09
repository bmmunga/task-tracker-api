from .utils import *
from ..routers.users import get_db, get_current_user

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'jayhus'
    assert response.json()['email'] == 'jayhus@email.com'
    assert response.json()['first_name'] == 'Jay'
    assert response.json()['last_name'] == 'Hus'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '11111'


def test_change_password_success(test_user):
    response = client.put("/user/password", json={"password": "test12345",
                                                    "new_password": "newtest12345"})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put("/user/password", json={"password": "wrongpassword",
                            "new_password": "new+password"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}


def test_change_phone_number_success(test_user):
    response = client.put("/user/phonenumber/111111")
    assert response.status_code == status.HTTP_204_NO_CONTENT
