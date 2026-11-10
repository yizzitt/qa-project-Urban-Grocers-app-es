from datetime import datetime
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):

    metadata.update({
        "Proyecto": "Urban Grocers API Testing",
        "Autor": "Freddy Ramirez",
        "Especialidad": "QA Automation",
        "Lenguaje": "Python 3.15",
        "Framework": "Pytest",
        "Libreria HTTP": "Requests",
        "Tipo de pruebas": "API REST",
        "Fecha de ejecucion": datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    })


def pytest_html_report_title(report):
    report.title = "Urban Grocers | API Testing Report"