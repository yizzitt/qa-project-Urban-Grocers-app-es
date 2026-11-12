from datetime import datetime

import pytest
import data
import sender_stand_request


# METADATOS DEL REPORTE HTML

@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):

    metadata.update({
        "Proyecto": "Urban Grocers API Testing",
        "Autor": "Freddy Ramirez",
        "Especialidad": "QA Automation",
        "Lenguaje": "Python",
        "Framework": "Pytest",
        "Libreria HTTP": "Requests",
        "Tipo de pruebas": "API REST",
        "Fecha de ejecucion": datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    })


def pytest_html_report_title(report):
    report.title = "Urban Grocers | API Testing Report"


# FIXTURES

@pytest.fixture
def auth_token():

    response = sender_stand_request.post_new_user(data.user_body)

    assert response.status_code == 201, (
        f"No se pudo crear el usuario. "
        f"Codigo HTTP recibido: {response.status_code}"
    )

    return response.json()["authToken"]


@pytest.fixture
def create_kit(auth_token):

    def _create_kit(kit_body):

        return sender_stand_request.post_new_client_kit(
            auth_token,
            kit_body
        )

    return _create_kit