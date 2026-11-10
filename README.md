# Urban Grocers API Automation Testing

### Automated API Testing | Python | Pytest | Requests

![Python](https://img.shields.io/badge/Python-3.15-blue)
![Pytest](https://img.shields.io/badge/Pytest-9.2.0-green)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange)
![Testing](https://img.shields.io/badge/Testing-API-purple)

## Project Overview

This project focuses on automated API testing of the
Urban Grocers application, specifically validating
the kit creation functionality.

The main objective is to verify API behavior,
validate request and response data, and identify
potential defects according to the documented
business requirements.

## Technologies

- Python
- Pytest
- Requests
- REST API
- JSON
- Git & GitHub
- Pytest HTML

## Testing Scope

**Endpoint:** `POST /api/v1/kits`

The automated test suite covers:

- Kit creation with valid names.
- Empty name validation.
- Invalid characters.
- Numeric characters.
- Underscores and special characters.
- HTTP response status validation.
- Response body verification.

## Project Structure

```text
qa-project-Urban-Grocers-app-es/
│
├── configuration.py
├── data.py
├── sender_stand_request.py
├── create_kit_name_kit_test.py
├── conftest.py
├── BUG_REPORT.md
├── README.md
└── .gitignore