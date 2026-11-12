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
    |-- reports/ (generated locally, not tracked by Git)

## Testing Scope

**Endpoint:** `POST /api/v1/kits`

The automated test suite covers nine test scenarios based on the project requirements.

### Positive Testing

The following scenarios are expected to return HTTP 201 Created:

1. Kit name containing one character.
2. Kit name containing 511 characters.
3. Kit name containing special characters (`№%@`).
4. Kit name containing leading and trailing spaces.
5. Kit name containing numeric characters as a string (`123`).

### Negative Testing

The following scenarios are expected to return HTTP 400 Bad Request:

1. Empty kit name.
2. Kit name exceeding the 511-character limit.
3. Missing `name` parameter.
4. Numeric value instead of a string for the `name` parameter.

### Response Validation

- HTTP status code verification.
- Response body validation.
- Returned kit name verification.
- Positive and negative response handling.
- JSON request body validation.

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

**Latest execution: November 12, 2026**

| Metric | Result |
|---|---:|
| Total test cases | 9 |
| Passed | 5 |
| Failed | 4 |
| Positive scenarios | 5 |
| Negative scenarios | 4 |

### Defect Identified

**BUG-001: API does not correctly validate invalid kit creation requests.**

The four negative scenarios returned unexpected HTTP status codes:

| Scenario | Expected Result | Actual Result |
|---|---|---|
| Empty name | HTTP 400 | HTTP 201 |
| 512-character name | HTTP 400 | HTTP 201 |
| Missing name parameter | HTTP 400 | HTTP 500 |
| Numeric name type | HTTP 400 | HTTP 201 |

All five positive test scenarios passed.

Four negative test scenarios failed because the API returned unexpected HTTP status codes.

The defect is documented in `BUG_REPORT.md`.

The failed tests represent API behavior issues identified during testing, not automation framework configuration errors.

## QA Skills Demonstrated

- API testing.
- Test case design.
- Positive and negative testing.
- Test parametrization.
- Pytest fixtures.
- HTTP request handling.
- JSON request validation.
- Response validation.
- Defect identification and documentation.
- HTML test reporting.
- Git and GitHub version control.

## Author

**Freddy Ramirez**

QA Manual | QA Automation

- GitHub: [yizzitt](https://github.com/yizzitt)
- LinkedIn: [Freddy Ramirez](https://www.linkedin.com/in/freddy-ram%C3%ADrez-rede-8b4778283/)