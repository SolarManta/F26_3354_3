# Group Number and Team Name: Group 3
# UTD Escort App


## Files

| File | Purpose |
| --- | --- |
| service_request.py | Defines the request, escort, and status classes and implements the request decision methods. |
| test_service_request.py | Contains three automated tests for retrieving, accepting, and declining a request. |

## Setup and local execution

1. Install Python 3.8 or newer from [python.org](https://www.python.org/downloads/) if needed.
2. Download or clone the repository and open a terminal in the project root.
3. Skip package installation and environment configuration.
4. Run the sample through its automated tests.
   sh
   python -m unittest -v test_service_request
   
## Expected results

- **Retrieve:** Returns the same request with status Pending.
- **Accept:** Returns an Accepted status linked to the escort and updates the request to Accepted.
- **Decline:** Updates the request to Declined and returns no value.

A successful run reports three tests and ends with OK. These tests cover the sample class.
