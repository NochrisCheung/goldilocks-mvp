
import json
from typing import Any, Dict
import requests

def fetch_data(endpoint: str, endpoint_method: str, authentication_method: str, api_key: str, params: Dict) -> Dict[str, Any]:
    """
    Generic function to fetch data from APIs
    """
    headers = {
        # "Accept": "application/json",
        "Content-Type": "application/json",
    }

    if authentication_method == "token":
        headers["Authorization"] = f"Token {api_key}"
    elif authentication_method == "api_key":
        headers["X-Api-Key"] = api_key
    else:
        raise ValueError(f"Invalid authentication method: {authentication_method}")

    try:
        if endpoint_method == "GET":
            response = requests.get(
                endpoint,
                headers=headers,
                params=params  # Send GET parameters as query string
            )
        elif endpoint_method == "POST":
            response = requests.post(
                endpoint,
                json=params,  # Let requests handle JSON serialization
                headers=headers
            )
        else:
            raise ValueError(f"Invalid endpoint method: {endpoint_method}")

        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.HTTPError as e:
        # Add detailed error logging
        error_info = {
            "status_code": e.response.status_code,
            "url": e.response.url,
            "request_headers": headers,
            "request_params": params,
            "response_text": e.response.text
        }
        raise Exception(f"API request failed: {json.dumps(error_info, indent=2)}")