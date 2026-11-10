# Urban Grocers API Automation Testing

![Python](https://img.shields.io/badge/Python-3.15-blue)
![Pytest](https://img.shields.io/badge/Pytest-9.2.0-green)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange)
![Testing](https://img.shields.io/badge/Testing-API-purple)

Automated API testing project focused on validating the kit creation functionality of the Urban Grocers application.

## Project Overview

The purpose of this project is to validate API behavior, verify request and response data, and identify defects based on documented business requirements.

The test suite uses Python, Pytest, and Requests to automate positive and negative API scenarios.

## Technologies

- Python 3.15
- Pytest 9.2.0
- Requests
- REST API
- JSON
- Git and GitHub
- Pytest HTML Reports

## Project Structure

    qa-project-Urban-Grocers-app-es/
    |
    |-- configuration.py
    |-- data.py
    |-- sender_stand_request.py
    |-- create_kit_name_kit_test.py
    |-- conftest.py
    |-- pytest.ini
    |-- BUG_REPORT.md
    |-- README.md
    |-- .gitignore
    |
    |-- reports/ (generated locally, not tracked by Git)

## Testing Scope

**Endpoint:** `POST /api/v1/kits`

The automated test suite covers the following scenarios:

### Positive Testing

- Kit creation with valid names.
- Names containing spaces.
- Names containing hyphens.
- Single-word names.

### Negative Testing

- Empty names.
- Names containing numbers.
- Names containing underscores.
- Names containing special characters.
- Numeric-only names.

### Response Validation

- HTTP status code verification.
- Response body validation.
- Returned kit name verification.

## Test Execution

### 1. Clone the repository

    git clone https://github.com/yizzitt/qa-project-Urban-Grocers-app-es.git
    cd qa-project-Urban-Grocers-app-es

### 2. Create a virtual environment

    python -m venv .venv

### 3. Activate the environment

Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

### 4. Install dependencies

    pip install pytest requests pytest-html

### 5. Run automated tests

    pytest -v

### 6. Generate an HTML report

    pytest -v --html=reports/reporte_pruebas.html --self-contained-html

The HTML report is generated locally and excluded from version control.

## Test Results

**Latest execution: November 10, 2026**

| Metric | Result |
|---|---:|
| Total test cases | 9 |
| Passed | 4 |
| Failed | 5 |

### Defect Identified

**BUG-001: Invalid kit names are accepted by the API.**

- Expected result: HTTP 400 Bad Request.
- Actual result: HTTP 201 Created.
- Affected scenarios: 5 negative test cases.

The API accepts inputs that do not comply with the documented naming requirements.

The defect is documented in `BUG_REPORT.md`.

The failed tests represent an API behavior issue identified during testing, not an automation framework configuration error.

## QA Skills Demonstrated

- API testing.
- Test case design.
- Positive and negative testing.
- Test parametrization.
- Pytest fixtures.
- HTTP request handling.
- Response validation.
- Defect identification and documentation.
- HTML test reporting.
- Git and GitHub version control.

## Author

**Freddy Ramirez**

QA Manual | QA Automation

- GitHub: [yizzitt](https://github.com/yizzitt)
- LinkedIn: [Freddy Ramirez](https://www.linkedin.com/in/freddy-ram%C3%ADrez-rede-8b4778283/)