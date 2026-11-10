import pytest
import data
import sender_stand_request


def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)

    assert response.status_code == 201, (
        f"No se pudo crear el usuario. "
        f"Código HTTP recibido: {response.status_code}"
    )

    return response.json()["authToken"]


def create_kit(kit_name):
    auth_token = get_new_user_token()

    kit_body = data.kit_body.copy()
    kit_body["name"] = kit_name

    return sender_stand_request.post_new_client_kit(
        auth_token,
        kit_body
    )


# PRUEBAS POSITIVAS

@pytest.mark.parametrize("kit_name", [
    "Mi kit prueba",
    "Kit-con-guiones",
    "Kit",
    "Kit con espacios"
])
def test_create_kit_with_valid_name(kit_name):

    response = create_kit(kit_name)

    assert response.status_code == 201, (
        f"Se esperaba HTTP 201, pero se recibió "
        f"{response.status_code}."
    )

    assert response.json()["name"] == kit_name


# PRUEBAS NEGATIVAS

@pytest.mark.parametrize("kit_name", [
    "",
    "Kit123",
    "Kit_name",
    "Kit @#$%",
    "123456"
])
def test_create_kit_with_invalid_name(kit_name):

    response = create_kit(kit_name)

    assert response.status_code == 400, (
        f"Se esperaba HTTP 400, pero se recibió "
        f"{response.status_code}."
    )