import json
from backend.core.llm_client import DeepSeekClient
from backend.services.core.api_client import fetch_data
from backend.services.data_apis.global_database_api import GlobalDatabaseAPI
from backend.services.utils.table_generator import create_table

JSON_SCHEMA = {
  "type": "object",
  "properties": {
    "endpoints": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "operation": {
            "type": "string",
            "description": "Description of the operation to perform"
          },
          "name": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_]+$",
            "description": "Unique endpoint identifier"
          },
          "method": {
            "type": "string",
            "enum": ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
            "description": "HTTP method for the endpoint"
          },
          "path": {
            "type": "string",
            "pattern": "^/",
            "description": "Endpoint path starting with a slash"
          },
          "parameters": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "description": "Key-value pairs of parameters"
          }
        },
        "required": ["name", "method", "path"],
        "additionalProperties": False
      }
    }
  },
  "required": ["endpoints"],
  "additionalProperties": False
}


if __name__ == "__main__":
    gd_api = GlobalDatabaseAPI()
    api_name = gd_api.get_name()
    api_description = gd_api.get_description()
    endpoint_schema = gd_api.get_endpoint_schema()
    input_options = gd_api.get_input_options()

    deepseek_client = DeepSeekClient(
      system_prompt= f"""
        You are an expert in {api_name}.
        {api_description}.
        Your mission is to learn about the user's intent and translate it into a list of operations, each include an endpoint and parameters.
        You have access to the following endpoints:
        {endpoint_schema}
        
        Return the endpoint and parameters in the following JSON format.
        {JSON_SCHEMA}

        You have access to the following input options:
        {input_options}
        
        If the task requires multiple steps, break the mission down into smaller steps and return a list of operations. This includes interating over a paginated endpoint results.
      """,
      response_format= {
        "type": "json_object"
      }
    )
    response_string = deepseek_client.generate_response("Give me a list of 50 companies in the UK that are in the retail industry and have more than 100 employees.")
    print(response_string)

    response = json.loads(response_string)

    # Fetch data from the API
    if isinstance(response.get("endpoints"), list):
      for operation in response.get("endpoints"):
        endpoint = gd_api.get_base_url() + operation.get("path")
        endpoint_method = operation.get("method")
        authentication_method = gd_api.get_authentication_method()
        api_key = gd_api.get_api_key()
        parameters = operation.get("parameters")

        data = fetch_data(endpoint, endpoint_method, authentication_method, api_key, parameters)
        print(data)
        with open("backend/playground/test_company_names.json", "w") as f:
          json.dump(data, f)

        
        table = create_table(data)
        print(table)