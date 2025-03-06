import json
import pandas as pd

def create_table(data):
    df = pd.DataFrame(data)
    return df.to_markdown()

def extract_table_data(json):
    keyword_list = ["data", "results"]
    keyword = None
    for key in json.keys():
      for keyword in keyword_list:
        if keyword in key:
          keyword = key
          break
    if keyword is None:
      raise ValueError("No keyword found in the JSON file")
    return json[keyword]

def create_table_from_json(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    table_data = extract_table_data(data)
    return create_table(table_data)

def store_table_to_csv(table, csv_file):
    df = pd.DataFrame(table)
    df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    print(create_table_from_json("backend/playground/test_company_names.json"))
