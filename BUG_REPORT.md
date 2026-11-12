# BUG REPORT
## Urban Grocers API Testing

**Project:** Urban Grocers API
**Module:** Kit Creation
**Endpoint:** POST /api/v1/kits
**Bug ID:** BUG-001
**Severity:** Major
**Priority:** High
**Status:** Open
**Reported by:** Freddy Ramirez
**Test type:** API Testing
**Report date:** November 12, 2026

---

### 1. Title

The API does not correctly validate invalid kit creation requests.

### 2. Description

When sending POST requests to `/api/v1/kits`, the API
does not consistently validate the `name` parameter
according to the official project requirements.

During automated testing, four invalid input scenarios
produced unexpected HTTP responses.

Three requests were accepted with HTTP 201 Created,
while a request without the required `name` parameter
returned HTTP 500 Internal Server Error.

The expected response for all four scenarios is
HTTP 400 Bad Request.

### 3. Preconditions

- Have access to the Urban Grocers API.
- Create a new user through the corresponding endpoint.
- Obtain a valid authToken.
- Use the token to authorize kit creation requests.

### 4. Steps to Reproduce

1. Create a new user.
2. Obtain the user's authToken.
3. Send a POST request to `/api/v1/kits`.
4. Include one of the invalid JSON payloads listed below.
5. Review the HTTP status code returned by the API.
6. Compare the actual response with the expected result.

### 5. Test Data and Results

| Case | Request Body | Expected Result | Actual Result |
|---|---|---|---|
| 1 | `{"name": ""}` | HTTP 400 | HTTP 201 |
| 2 | `{"name": "A" * 512}` | HTTP 400 | HTTP 201 |
| 3 | `{}` | HTTP 400 | HTTP 500 |
| 4 | `{"name": 123}` | HTTP 400 | HTTP 201 |

### 6. Expected Result

The API must validate the request body according to
the project requirements.

For all four invalid scenarios, the API must reject
the request and return:

HTTP 400 Bad Request.

### 7. Actual Result

The API returns unexpected HTTP responses:

- Empty name: HTTP 201 Created.
- Name exceeding 511 characters: HTTP 201 Created.
- Missing `name` parameter: HTTP 500 Internal Server Error.
- Numeric value instead of a string: HTTP 201 Created.

The API therefore does not handle these invalid
requests according to the expected behavior.

### 8. Test Evidence

Automated execution using Python and Pytest.

**Latest execution:** November 12, 2026

| Metric | Result |
|---|---:|
| Total test cases | 9 |
| Passed | 5 |
| Failed | 4 |
| Positive scenarios | 5 |
| Negative scenarios | 4 |

All five positive scenarios passed.

The four negative scenarios failed because the API
returned unexpected HTTP status codes.

### 9. Impact

Incorrect request validation may allow invalid kit
creation requests to be accepted.

Additionally, returning HTTP 500 instead of HTTP 400
for a missing required parameter exposes an incorrect
error-handling behavior.

This affects API reliability and compliance with
the documented project requirements.

### 10. Test Environment

- Operating System: Windows 11
- Programming Language: Python 3.15.0
- Testing Framework: Pytest 9.2.0
- HTTP Library: Requests
- Application Type: REST API
- HTTP Method: POST
- Endpoint: /api/v1/kits
