import pytest


# PRUEBAS POSITIVAS

@pytest.mark.parametrize("kit_name", [
    "Mi kit prueba",
    "Kit-con-guiones",
    "Kit",
    "Kit con espacios"
])
def test_create_kit_with_valid_name(create_kit, kit_name):

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
def test_create_kit_with_invalid_name(create_kit, kit_name):

    response = create_kit(kit_name)

    assert response.status_code == 400, (
        f"Se esperaba HTTP 400, pero se recibió "
        f"{response.status_code}."
    )