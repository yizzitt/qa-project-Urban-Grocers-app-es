import pytest


# PRUEBAS POSITIVAS: HTTP 201 CREATED

@pytest.mark.parametrize("kit_body", [
    pytest.param(
        {"name": "a"},
        id="1-character"
    ),
    pytest.param(
        {"name": "A" * 511},
        id="511-characters"
    ),
    pytest.param(
        {"name": "\u2116%@"},
        id="special-characters"
    ),
    pytest.param(
        {"name": " A Aaa "},
        id="spaces-in-name"
    ),
    pytest.param(
        {"name": "123"},
        id="numbers-as-string"
    )
])
def test_create_kit_with_valid_name(create_kit, kit_body):

    response = create_kit(kit_body)

    assert response.status_code == 201, (
        f"Se esperaba HTTP 201, pero se recibio "
        f"{response.status_code}."
    )

    assert response.json()["name"] == kit_body["name"], (
        "El nombre del kit recibido no coincide "
        "con el nombre enviado."
    )


# PRUEBAS NEGATIVAS: HTTP 400 BAD REQUEST

@pytest.mark.parametrize("kit_body", [
    pytest.param(
        {"name": ""},
        id="empty-name"
    ),
    pytest.param(
        {"name": "A" * 512},
        id="512-characters"
    ),
    pytest.param(
        {},
        id="missing-name-parameter"
    ),
    pytest.param(
        {"name": 123},
        id="numeric-name-type"
    )
])
def test_create_kit_with_invalid_name(create_kit, kit_body):

    response = create_kit(kit_body)

    assert response.status_code == 400, (
        f"Se esperaba HTTP 400, pero se recibio "
        f"{response.status_code}."
    )