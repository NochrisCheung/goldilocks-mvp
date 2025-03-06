from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")

class GlobalDatabaseAPI:
    def __init__(self):
        self.name = NAME
        self.description = DESCRIPTION
        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.version = VERSION
        self.authentication_method = AUTHENTICATION_METHOD
        self.endpoint_schema = ENDPOINTS_SCHEMA
        self.input_options = INPUT_OPTIONS
        self.errors_schema = ERRORS_SCHEMA

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_base_url(self):
        return self.base_url
    
    def get_version(self):
        return self.version
    
    def get_authentication_method(self):
        return self.authentication_method   

    def get_api_key(self):
        return self.api_key
    
    def get_errors_schema(self):
        return self.errors_schema
    
    def get_endpoint_schema(self):
        return self.endpoint_schema
    
    def get_input_options(self):
        return self.input_options

NAME = "Global Database API"
DESCRIPTION = "The Global Database API is a RESTful API that provides access to records of companies and employees."
AUTHENTICATION_METHOD = "token"
API_KEY = os.getenv("GLOABL_DATABASE_API_KEY")
VERSION = "2.0"
BASE_URL = "https://api.globaldatabase.com/v2"
ERRORS_SCHEMA = { 
    "errors": {
        "TokenVerificationError": {
        "description": "Error when the provided token is invalid.",
        "example": {
            "detail": "Invalid token"
        }
        },
        "InvalidRequest": {
        "description": "Error when required fields are missing or invalid.",
        "example": {
            "field_name": [
            "This field is required."
            ]
        }
        },
        "InternalError": {
        "description": "Generic server error.",
        "example": {
            "detail": "A server error occurred."
        }
        },
        "LimitError": {
        "description": "Error when usage limits have been reached.",
        "example": {
            "access": {
            "permission": "code_permission",
            "permission_name": "Name permission",
            "module": "code_module",
            "module_name": "Name Module",
            "app": "api",
            "app_name": "Api"
            },
            "error_guard": "limits.daily",
            "message_guard": "You have reached your daily online browsing limit"
        }
    }
  }
}
ENDPOINTS_SCHEMA = {
  "endpoints": [ {
      "name": "Usage Metrics",
      "method": "GET",
      "path": "/metrics",
      "description": "Retrieves usage metrics for various API features.",
      "parameters": [],
      "responses": {
        "200": {
          "description": "List of usage metrics.",
          "example": [
            {
              "name": "Executives Company",
              "codename": "executives_company",
              "metrics": [
                {
                  "name": "Executives Company",
                  "codename": "executives_company",
                  "used": 10,
                  "total": 100
                }
              ]
            }
          ]
        }
      }
    },
    {
      "name": "Prospecting Companies",
      "method": "POST",
      "path": "/prospecting",
      "description": "Search for companies based on various filter criteria. Records are paginated.",
      "parameters": [
        {
          "name": "page",
          "in": "body",
          "type": "integer",
          "required": False,
          "description": "Page number (WARNING: maximum page value is 10)."
        },
        {
          "name": "per_page",
          "in": "body",
          "type": "integer",
          "required": False,
          "description": "Number of results per page (WARNING: maximum value is 50)."
        },
        {
          "name": "filters",
          "in": "body",
          "type": "object",
          "required": False,
          "description": "Filter criteria for the search.",
          "properties": {
            "company_status": {
              "type": "array",
              "items": { "type": "integer" },
              "description": "Company status IDs, available in nomenclatures."
            },
            "number_of_employees": {
              "type": "object",
              "description": "Range for company size.",
              "properties": {
                "gte": { "type": "integer", "description": "Minimum number of employees." },
                "lte": { "type": "integer", "description": "Maximum number of employees." }
              }
            },
            "trading_activity": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Trading activity values, available in nomenclatures."
            },
            "activity_type": {
              "type": "array",
              "items": { "type": "integer" },
              "description": "Company activity type IDs, available in nomenclatures."
            },
            "company_type": {
              "type": "array",
              "items": { "type": "integer" },
              "description": "Company type IDs, available in nomenclatures."
            },
            "company_incorporation": {
              "type": "object",
              "description": "Range for company incorporation date.",
              "properties": {
                "gte": { "type": "string", "format": "date", "description": "Earliest incorporation date." },
                "lte": { "type": "string", "format": "date", "description": "Latest incorporation date." }
              }
            },
            "legal_form": {
              "type": "array",
              "items": { "type": "integer" },
              "description": "Legal form IDs, available in nomenclatures."
            },
            "industry_focus": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Industry focus values, available in nomenclatures.",
              "example": [
                "4564019"
              ]
            },
            "website_keywords": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Keywords from the company website."
            },
            "nace": {
              "type": "array",
              "items": { "type": "string" },
              "description": "NACE Rev. 2 codes, available in nomenclatures."
            },
            "isic": {
              "type": "array",
              "items": { "type": "string" },
              "description": "International SIC codes, available in nomenclatures."
            },
            "sic_code_be": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Belgium SIC Codes, available in nomenclatures."
            },
            "sic_code_de": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Germany SIC Codes, available in nomenclatures."
            },
            "sic_code_dk": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Denmark SIC Codes, available in nomenclatures."
            },
            "sic_code_fr": {
              "type": "array",
              "items": { "type": "string" },
              "description": "France SIC Codes, available in nomenclatures."
            },
            "sic_code_gb": {
              "type": "array",
              "items": { "type": "string" },
              "description": "United Kingdom SIC Codes, available in nomenclatures."
            },
            "sic_code_ie": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Ireland SIC Codes, available in nomenclatures."
            },
            "sic_code_it": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Italy SIC Codes, available in nomenclatures."
            },
            "sic_code_lu": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Luxembourg SIC Codes, available in nomenclatures."
            },
            "sic_code_nl": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Netherlands SIC Codes, available in nomenclatures."
            },
            "sic_code_no": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Norway SIC Codes, available in nomenclatures."
            },
            "sic_code_se": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Sweden SIC Codes, available in nomenclatures."
            },
            "sic_code_sg": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Singapore SIC Codes, available in nomenclatures."
            },
            "sic_code_us": {
              "type": "array",
              "items": { "type": "string" },
              "description": "US SIC Codes, available in nomenclatures."
            },
            "sic_code_ca": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Canada SIC Codes, available in nomenclatures."
            },
            "sic_code_mx": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Mexico SIC Codes, available in nomenclatures."
            },
            "sic_code_anz": {
              "type": "array",
              "items": { "type": "string" },
              "description": "ANZ SIC Codes, available in nomenclatures."
            },
            "location_regions": {
              "type": "object",
              "description": "Company region, available in nomenclatures id (dive into nomenclature) parents (use in prospecting filter)",
              "properties": {
                "id": { "type": "string" },
                "parents": {
                  "type": "array",
                  "items": { "type": "string" }
                }
              }
            },
            "location_countries": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Company country, options available in input options",
              "example": [
                "1219916_1800795"
              ]
            },
            "location_zip": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Company ZIP Codes."
            },
            "location_type": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Filter by city or state."
            },
            "financial_currency": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Company currency, available in nomenclatures."
            },
            "financial_turnover": {
              "type": "object",
              "description": "Company turnover range.",
              "properties": {
                "gte": { "type": "number", "description": "Minimum turnover." },
                "lte": { "type": "number", "description": "Maximum turnover." }
              }
            },
            "financial_profit": {
              "type": "object",
              "description": "Company net profit range.",
              "properties": {
                "gte": { "type": "number", "description": "Minimum net profit." },
                "lte": { "type": "number", "description": "Maximum net profit." }
              }
            },
            "financial_liabilities": {
              "type": "object",
              "description": "Company total liabilities range.",
              "properties": {
                "gte": { "type": "number", "description": "Minimum liabilities." },
                "lte": { "type": "number", "description": "Maximum liabilities." }
              }
            },
            "financial_directors": {
              "type": "object",
              "description": "Company director remuneration range.",
              "properties": {
                "gte": { "type": "number", "description": "Minimum director remuneration." },
                "lte": { "type": "number", "description": "Maximum director remuneration." }
              }
            },
            "financial_employee_profit": {
              "type": "object",
              "description": "Profit per employee range.",
              "properties": {
                "gte": { "type": "number" },
                "lte": { "type": "number" }
              }
            },
            "financial_exports": {
              "type": "object",
              "description": "Company financial exports range.",
              "properties": {
                "gte": { "type": "number" },
                "lte": { "type": "number" }
              }
            },
            "foreign_parents": {
              "type": "string",
              "description": "Foreign Parent filter, available in nomenclatures."
            },
            "ownership_accounts": {
              "type": "string",
              "description": "Consolidated Accounts filter, available in nomenclatures."
            },
            "insights_visits": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Company website visits, available in nomenclatures."
            },
            "insights_technologies": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Website technologies, available in nomenclatures."
            },
            "insights_ranking": {
              "type": "object",
              "description": "Alexa ranking range, available in nomenclatures.",
              "properties": {
                "gte": { "type": "number" },
                "lte": { "type": "number" }
              }
            },
            "advance_companies": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Filter option for selecting only specific companies."
            },
            "yoy_exports": {
              "type": "object",
              "description": "Year-over-year exports range.",
              "properties": {
                "gte": { "type": "number" },
                "lte": { "type": "number" }
              }
            },
            "yoy_liabilities": {
              "type": "object",
              "description": "Year-over-year liabilities range.",
              "properties": {
                "gte": { "type": "number" },
                "lte": { "type": "number" }
              }
            },
            "yoy_staff": {
              "type": "object",
              "description": "Year-over-year staff numbers range.",
              "properties": {
                "gte": { "type": "number" },
                "lte": { "type": "number" }
              }
            },
            "yoy_turnover": {
              "type": "object",
              "description": "Year-over-year turnover growth range.",
              "properties": {
                "gte": { "type": "number" },
                "lte": { "type": "number" }
              }
            },
            "yoy_ebitda": {
              "type": "object",
              "description": "Year-over-year EBITDA range.",
              "properties": {
                "gte": { "type": "number" },
                "lte": { "type": "number" }
              }
            },
            "yoy_profit": {
              "type": "object",
              "description": "Year-over-year profit range.",
              "properties": {
                "gte": { "type": "number" },
                "lte": { "type": "number" }
              }
            },
            "linkedin": {
              "type": "string",
              "format": "uri",
              "description": "Company LinkedIn URL."
            }
          },
          "additionalProperties": False
        }
      ],
      "responses": {
        "200": {
          "description": "Response containing total companies, total pages, and matching company data.",
          "example": {
            "total_companies": 2594573,
            "total_pages": 200,
            "data": [
              {
                "id": 17784513,
                "name": "FIAT CHRYSLER AUTOMOBILES UK LTD"
              },
              {
                "id": 19844844,
                "name": "BAKKAVOR LIMITED"
              },
              {
                "id": 22084035,
                "name": "ASTRAZENECA UK LIMITED"
              }
            ]
          }
        }
      }
    },
    {
      "name": "Search Companies",
      "method": "POST",
      "path": "/overview",
      "description": "Search companies by name, country code, registration number, website, etc.",
      "parameters": [
        {
          "name": "name",
          "in": "body",
          "type": "string",
          "required": False,
          "description": "Company name search term."
        },
        {
          "name": "country_code",
          "in": "body",
          "type": "string",
          "required": False,
          "description": "ISO country code."
        },
        {
          "name": "registration_number",
          "in": "body",
          "type": "string",
          "required": False,
          "description": "Company registration number."
        },
        {
          "name": "vat_number",
          "in": "body",
          "type": "string",
          "required": False,
          "description": "VAT number."
        },
        {
          "name": "website",
          "in": "body",
          "type": "string",
          "required": False,
          "description": "Company website."
        },
        {
          "name": "phone_number",
          "in": "body",
          "type": "string",
          "required": False,
          "description": "Phone number."
        },
        {
          "name": "person",
          "in": "body",
          "type": "string",
          "required": False,
          "description": "Employee full name."
        },
        {
          "name": "company_status",
          "in": "body",
          "type": "array",
          "required": False,
          "description": "Company status IDs."
        },
        {
          "name": "page",
          "in": "body",
          "type": "int",
          "required": False,
          "description": "Page number (default is 1)."
        },
        {
          "name": "linkedin",
          "in": "body",
          "type": "url",
          "required": False,
          "description": "Company LinkedIn URL."
        }
      ],
      "responses": {
        "200": {
          "description": "Search results containing total results, total pages, and a list of companies.",
          "example": {
            "total_results": 8,
            "total_pages": 2,
            "data": [
              {
                "id": "22401777",
                "name": "DATABASE SERVICE PROVIDER GLOBAL LTD",
                "status": "Active",
                "country_code": "GB",
                "registration_number": "03898451"
              }
            ]
          }
        }
      }
    },
    {
      "name": "Company Details",
      "method": "GET",
      "path": "/companies/{id}",
      "description": "Retrieve detailed information for a specific company by its ID.",
      "parameters": [
        {
          "name": "id",
          "in": "url",
          "type": "int",
          "required": True,
          "description": "Unique company ID."
        }
      ],
      "responses": {
        "200": {
          "description": "Detailed company information.",
          "example": {
            "id": 17937983,
            "name": "TESCO PLC",
            "registration_number": "00445790",
            "country_code": "GB",
            "company_phone": [
              "+441992632222"
            ],
            "company_email": [],
            "company_fax": [],
            "company_website": "http://www.tesco.com",
            "company_legal_form": "Public Limited Company",
            "status": "Active",
            "brands": "TESCO PLC, TESCO STORES (HOLDINGS) PUBLIC LIMITED COMPANY",
            "address_street": "TESCO HOUSE SHIRE PARK",
            "address_location": "KESTREL WAY",
            "address_city": "WELWYN GARDEN CITY",
            "zip_code": "AL7 1GA",
            "country_name": "United Kingdom",
            "size": "10001",
            "vat_number": None,
            "founding_date": "1947-11-27",
            "industry": [
              {
                "id": 4592033,
                "type": "industry_focus",
                "value": "Retail"
              }
            ],
            "sic": [
              {
                "id": 3969852,
                "type": "sic_code_gb",
                "value": "47110 - Retail sale in non-specialised stores with food, beverages or tobacco predominating"
              }
            ],
            "twitter": "twitter.com/tesco",
            "linkedin": "linkedin.com/company/-tesco",
            "facebook": "facebook.com/tesco"
          }
        }
      }
    },
    {
      "name": "Search Employee",
      "method": "POST",
      "path": "/employees",
      "description": "Search for employees using filter criteria.",
      "parameters": [
        {
          "name": "page",
          "in": "body",
          "type": "int",
          "required": False,
          "description": "Page number (maximum page value is 10)."
        },
        {
          "name": "per_page",
          "in": "body",
          "type": "int",
          "required": False,
          "description": "Number of results per page."
        },
        {
          "name": "filters",
          "in": "body",
          "type": "object",
          "required": True,
          "description": "Filter criteria (e.g. full_name, seniority, department, job_title, company_id, linkedin)."
        }
      ],
      "responses": {
        "200": {
          "description": "Employee search results.",
          "example": {
            "total_employees": 69,
            "total_pages": 14,
            "data": [
              {
                "id": "20773074",
                "name": "Alex Puttock",
                "company_id": "20581257",
                "company_name": "NOVATECH LIMITED"
              }
            ]
          }
        }
      }
    },
    {
      "name": "Employee Details",
      "method": "GET",
      "path": "/employees/{id}",
      "description": "Retrieve detailed information for a specific employee by their ID.",
      "parameters": [
        {
          "name": "id",
          "in": "url",
          "type": "int",
          "required": True,
          "description": "Unique employee ID."
        }
      ],
      "responses": {
        "200": {
          "description": "Employee details.",
          "example": {
            "id": "199328763",
            "full_name": "Kerry Louise Johnson",
            "first_name": "Kerry",
            "last_name": "Johnson",
            "patronime_name": "Louise",
            "gender": "F",
            "seniority_level": [
              "Manager"
            ],
            "function_original_name": "governance officer",
            "phone": "+447446108873",
            "email": "kerry.johnson@lewisham.gov.uk",
            "company_name": "LONDON SOUTH BANK UNIVERSITY",
            "twitter": None,
            "linkedin": None,
            "facebook": None
          }
        }
      }
    },
    {
      "name": "Start Watch Company",
      "method": "POST",
      "path": "/watch-companies/start",
      "description": "Begin watching a specific company for updates.",
      "parameters": [
        {
          "name": "company_id",
          "in": "body",
          "type": "int",
          "required": True,
          "description": "ID of the company to watch."
        },
        {
          "name": "fields",
          "in": "body",
          "type": "array",
          "required": False,
          "description": "List of company fields to monitor."
        }
      ],
      "responses": {
        "200": {
          "description": "Confirmation of starting the watch."
        }
      }
    },
    {
      "name": "Stop Watch Company",
      "method": "POST",
      "path": "/watch-companies/stop",
      "description": "Stop watching a specific company.",
      "parameters": [
        {
          "name": "company_id",
          "in": "body",
          "type": "int",
          "required": True,
          "description": "ID of the company to stop watching."
        }
      ],
      "responses": {
        "200": {
          "description": "Confirmation of stopping the watch."
        }
      }
    },
    {
      "name": "Watched Companies",
      "method": "GET",
      "path": "/watch-companies",
      "description": "Retrieve a list of all companies currently being watched.",
      "parameters": [],
      "responses": {
        "200": {
          "description": "List of watched companies."
        }
      }
    },
    {
      "name": "All Companies Events",
      "method": "GET",
      "path": "/watch-companies/events",
      "description": "Retrieve events for all watched companies.",
      "parameters": [],
      "responses": {
        "200": {
          "description": "List of events."
        }
      }
    },
    {
      "name": "Watched Company Fields",
      "method": "GET",
      "path": "/watch-companies/fields",
      "description": "Retrieve the fields being monitored for watched companies.",
      "parameters": [],
      "responses": {
        "200": {
          "description": "List of watched fields."
        }
      }
    },
    {
      "name": "Add Watched Fields",
      "method": "POST",
      "path": "/watch-companies/fields/add",
      "description": "Add additional fields to watch for a company.",
      "parameters": [
        {
          "name": "company_id",
          "in": "body",
          "type": "int",
          "required": True,
          "description": "ID of the company."
        },
        {
          "name": "fields",
          "in": "body",
          "type": "array",
          "required": True,
          "description": "Fields to add."
        }
      ],
      "responses": {
        "200": {
          "description": "Confirmation of added fields."
        }
      }
    },
    {
      "name": "Remove Watched Fields",
      "method": "POST",
      "path": "/watch-companies/fields/remove",
      "description": "Remove fields from the watch list for a company.",
      "parameters": [
        {
          "name": "company_id",
          "in": "body",
          "type": "int",
          "required": True,
          "description": "ID of the company."
        },
        {
          "name": "fields",
          "in": "body",
          "type": "array",
          "required": True,
          "description": "Fields to remove."
        }
      ],
      "responses": {
        "200": {
          "description": "Confirmation of removed fields."
        }
      }
    },
    {
      "name": "Set Callback URL",
      "method": "POST",
      "path": "/watch-companies/callback",
      "description": "Set the callback URL for watch notifications.",
      "parameters": [
        {
          "name": "callback_url",
          "in": "body",
          "type": "url",
          "required": True,
          "description": "The URL to receive callbacks."
        }
      ],
      "responses": {
        "200": {
          "description": "Callback URL set confirmation."
        }
      }
    },
    {
      "name": "Get Callback URL",
      "method": "GET",
      "path": "/watch-companies/callback",
      "description": "Retrieve the current callback URL for watch notifications.",
      "parameters": [],
      "responses": {
        "200": {
          "description": "Current callback URL."
        }
      }
    },
    {
      "name": "Companies Webhook",
      "method": "POST",
      "path": "/watch-companies/webhook",
      "description": "Configure a webhook for companies.",
      "parameters": [
        {
          "name": "webhook_url",
          "in": "body",
          "type": "url",
          "required": True,
          "description": "The URL to be used for webhook callbacks."
        }
      ],
      "responses": {
        "200": {
          "description": "Webhook configured confirmation."
        }
      }
    },
    {
      "name": "Enrichment Company By Website",
      "method": "GET",
      "path": "/enrichment/company/website",
      "description": "Retrieve enriched company data using a website URL.",
      "parameters": [
        {
          "name": "website",
          "in": "query",
          "type": "string",
          "required": True,
          "description": "Company website URL."
        }
      ],
      "responses": {
        "200": {
          "description": "Enriched company data."
        }
      }
    },
    {
      "name": "Enrichment Company By Linkedin URL",
      "method": "GET",
      "path": "/enrichment/company/linkedin",
      "description": "Retrieve enriched company data using a LinkedIn URL.",
      "parameters": [
        {
          "name": "linkedin",
          "in": "query",
          "type": "url",
          "required": True,
          "description": "Company LinkedIn URL."
        }
      ],
      "responses": {
        "200": {
          "description": "Enriched company data."
        }
      }
    },
    {
      "name": "Enrichment Contact By Email",
      "method": "GET",
      "path": "/enrichment/contact/email",
      "description": "Retrieve enriched contact data using an email address.",
      "parameters": [
        {
          "name": "email",
          "in": "query",
          "type": "string",
          "required": True,
          "description": "Contact email address."
        }
      ],
      "responses": {
        "200": {
          "description": "Enriched contact data."
        }
      }
    },
    {
      "name": "Enrichment Contact By Linkedin URL",
      "method": "GET",
      "path": "/enrichment/contact/linkedin",
      "description": "Retrieve enriched contact data using a LinkedIn URL.",
      "parameters": [
        {
          "name": "linkedin",
          "in": "query",
          "type": "url",
          "required": True,
          "description": "Contact LinkedIn URL."
        }
      ],
      "responses": {
        "200": {
          "description": "Enriched contact data."
        }
      }
    },
    {
      "name": "Enrichment Contact",
      "method": "GET",
      "path": "/enrichment/contact",
      "description": "Retrieve enriched contact data (by an identifier or other criteria).",
      "parameters": [
        {
          "name": "id",
          "in": "query",
          "type": "int",
          "required": False,
          "description": "Optional contact identifier."
        }
      ],
      "responses": {
        "200": {
          "description": "Enriched contact data."
        }
      }
    },
    {
      "name": "Autocomplete Company Detail",
      "method": "GET",
      "path": "/autocomplete/company",
      "description": "Provides autocomplete suggestions for company details.",
      "parameters": [
        {
          "name": "query",
          "in": "query",
          "type": "string",
          "required": True,
          "description": "Search term for autocomplete."
        }
      ],
      "responses": {
        "200": {
          "description": "List of autocomplete suggestions."
        }
      }
    },
    {
      "name": "Company Financials",
      "method": "GET",
      "path": "/financials/company/{id}",
      "description": "Retrieve financial data for a specific company.",
      "parameters": [
        {
          "name": "id",
          "in": "url",
          "type": "int",
          "required": True,
          "description": "Unique company ID."
        }
      ],
      "responses": {
        "200": {
          "description": "Company financial data."
        }
      }
    },
    {
      "name": "Search Company for Digital Insights",
      "method": "POST",
      "path": "/digital-insights/search",
      "description": "Search companies for digital insights using filter criteria.",
      "parameters": [
        {
          "name": "filters",
          "in": "body",
          "type": "object",
          "required": True,
          "description": "Digital insights filter criteria."
        }
      ],
      "responses": {
        "200": {
          "description": "List of companies with digital insights."
        }
      }
    },
    {
      "name": "Company Digital Insights",
      "method": "GET",
      "path": "/digital-insights/company/{id}",
      "description": "Retrieve digital insights for a specific company.",
      "parameters": [
        {
          "name": "id",
          "in": "url",
          "type": "int",
          "required": True,
          "description": "Unique company ID."
        }
      ],
      "responses": {
        "200": {
          "description": "Digital insights for the company."
        }
      }
    },
    {
      "name": "Search Company for Ownership",
      "method": "POST",
      "path": "/ownership/search",
      "description": "Search for companies with ownership details using filter criteria.",
      "parameters": [
        {
          "name": "filters",
          "in": "body",
          "type": "object",
          "required": True,
          "description": "Ownership search filter criteria."
        }
      ],
      "responses": {
        "200": {
          "description": "List of companies with ownership details."
        }
      }
    },
    {
      "name": "Company Ownership",
      "method": "GET",
      "path": "/ownership/company/{id}",
      "description": "Retrieve ownership details for a specific company.",
      "parameters": [
        {
          "name": "id",
          "in": "url",
          "type": "int",
          "required": True,
          "description": "Unique company ID."
        }
      ],
      "responses": {
        "200": {
          "description": "Ownership details of the company."
        }
      }
    },
    {
      "name": "Search Credit Report",
      "method": "POST",
      "path": "/credit-report/search",
      "description": "Search for credit reports based on filter criteria.",
      "parameters": [
        {
          "name": "filters",
          "in": "body",
          "type": "object",
          "required": True,
          "description": "Credit report search filters."
        }
      ],
      "responses": {
        "200": {
          "description": "List of matching credit reports."
        }
      }
    },
    {
      "name": "Generate Credit Report",
      "method": "POST",
      "path": "/credit-report/generate",
      "description": "Generate a credit report for a company.",
      "parameters": [
        {
          "name": "company_id",
          "in": "body",
          "type": "int",
          "required": True,
          "description": "Unique company ID."
        }
      ],
      "responses": {
        "200": {
          "description": "Result of credit report generation."
        }
      }
    },
    {
      "name": "Check Credit Report",
      "method": "GET",
      "path": "/credit-report/check/{id}",
      "description": "Check the status of a credit report by its ID.",
      "parameters": [
        {
          "name": "id",
          "in": "url",
          "type": "int",
          "required": True,
          "description": "Credit report ID."
        }
      ],
      "responses": {
        "200": {
          "description": "Status of the credit report."
        }
      }
    },
    {
      "name": "Content Credit Report by ID",
      "method": "GET",
      "path": "/credit-report/content/{id}",
      "description": "Retrieve the content of a credit report by its ID.",
      "parameters": [
        {
          "name": "id",
          "in": "url",
          "type": "int",
          "required": True,
          "description": "Credit report ID."
        }
      ],
      "responses": {
        "200": {
          "description": "Credit report content."
        }
      }
    },
    {
      "name": "Generate CR and Get Content",
      "method": "POST",
      "path": "/credit-report/generate-content",
      "description": "Generate a credit report and retrieve its content in one step.",
      "parameters": [
        {
          "name": "company_id",
          "in": "body",
          "type": "int",
          "required": True,
          "description": "Unique company ID."
        }
      ],
      "responses": {
        "200": {
          "description": "Generated credit report content."
        }
      }
    },
    {
      "name": "Get Credit Report by ID",
      "method": "GET",
      "path": "/credit-report/{id}",
      "description": "Retrieve detailed information of a credit report by its ID.",
      "parameters": [
        {
          "name": "id",
          "in": "url",
          "type": "int",
          "required": True,
          "description": "Credit report ID."
        }
      ],
      "responses": {
        "200": {
          "description": "Credit report details."
        }
      }
    },
    {
      "name": "Purchased Credit Report",
      "method": "GET",
      "path": "/credit-report/purchased/{id}",
      "description": "Retrieve a purchased credit report by its ID.",
      "parameters": [
        {
          "name": "id",
          "in": "url",
          "type": "int",
          "required": True,
          "description": "Credit report ID."
        }
      ],
      "responses": {
        "200": {
          "description": "Details of the purchased credit report."
        }
      }
    },
  ]
}

INPUT_OPTIONS = {
    "location_countries": {
        "name": "location_countries",
        "values": [
          {
              "id": 4647461,
              "parents": "1463712_4004115",
              "name": "Afghanistan",
              "has_children": True,
              "active": True
          },
          {
              "id": 5666310,
              "parents": "1219916_1547645",
              "name": "Albania",
              "has_children": True,
              "active": True
          },
          {
              "id": 4636320,
              "parents": "4292987_4367081",
              "name": "Algeria",
              "has_children": True,
              "active": True
          },
          {
              "id": 5101203,
              "parents": "1219916_1365832",
              "name": "Andorra",
              "has_children": True,
              "active": True
          },
          {
              "id": 4673960,
              "parents": "4292987_4292988",
              "name": "Angola",
              "has_children": True,
              "active": True
          },
          {
              "id": 4630903,
              "parents": "1869197_4598167",
              "name": "Antigua and Barbuda",
              "has_children": False,
              "active": True
          },
          {
              "id": 4645647,
              "parents": "4024368_4025268",
              "name": "Argentina",
              "has_children": True,
              "active": True
          },
          {
              "id": 4631306,
              "parents": "1463712_3990621",
              "name": "Armenia",
              "has_children": True,
              "active": True
          },
          {
              "id": 4682935,
              "parents": "4271351_4274650",
              "name": "Australia",
              "has_children": True,
              "active": True
          },
          {
              "id": 5714035,
              "parents": "1219916_1551116",
              "name": "Austria",
              "has_children": True,
              "active": True
          },
          {
              "id": 4634835,
              "parents": "1463712_3364113",
              "name": "Azerbaijan",
              "has_children": True,
              "active": True
          },
          {
              "id": 4630905,
              "parents": "4249245_4606665",
              "name": "Bahamas",
              "has_children": False,
              "active": True
          },
          {
              "id": 4630901,
              "parents": "1463712_4598169",
              "name": "Bahrain",
              "has_children": False,
              "active": True
          },
          {
              "id": 4770959,
              "parents": "1463712_4007095",
              "name": "Bangladesh",
              "has_children": True,
              "active": True
          },
          {
              "id": 4630906,
              "parents": "1869197_4598170",
              "name": "Barbados",
              "has_children": False,
              "active": True
          },
          {
              "id": 5800308,
              "parents": "1219916_1575345",
              "name": "Belarus",
              "has_children": True,
              "active": True
          },
          {
              "id": 5968500,
              "parents": "1219916_1621326",
              "name": "Belgium",
              "has_children": True,
              "active": True
          },
          {
              "id": 4630907,
              "parents": "4249245_4249246",
              "name": "Belize",
              "has_children": True,
              "active": True
          },
          {
              "id": 4685054,
              "parents": "4292987_4294892",
              "name": "Benin",
              "has_children": True,
              "active": True
          },
          {
              "id": 4631530,
              "parents": "1869197_4598171",
              "name": "Bermuda",
              "has_children": False,
              "active": True
          },
          {
              "id": 4783616,
              "parents": "1463712_3118064",
              "name": "Bhutan",
              "has_children": True,
              "active": True
          },
          {
              "id": 4752412,
              "parents": "4024368_4185025",
              "name": "Bolivia",
              "has_children": True,
              "active": True
          },
          {
              "id": 7560460,
              "parents": "1219916_3095502",
              "name": "Bosnia and Herzegovina",
              "has_children": True,
              "active": True
          },
          {
              "id": 4692139,
              "parents": "4292987_4295915",
              "name": "Botswana",
              "has_children": True,
              "active": True
          },
          {
              "id": 4864857,
              "parents": "4024368_4047745",
              "name": "Brazil",
              "has_children": True,
              "active": True
          },
          {
              "id": 4785077,
              "parents": "1463712_1468241",
              "name": "Brunei",
              "has_children": True,
              "active": True
          },
          {
              "id": 5990506,
              "parents": "1219916_1627513",
              "name": "Bulgaria",
              "has_children": True,
              "active": True
          },
          {
              "id": 4700349,
              "parents": "4292987_4296518",
              "name": "Burkina Faso",
              "has_children": True,
              "active": True
          },
          {
              "id": 4721398,
              "parents": "4292987_4300247",
              "name": "Burundi",
              "has_children": True,
              "active": True
          },
          {
              "id": 4788234,
              "parents": "1463712_1531640",
              "name": "Cambodia",
              "has_children": True,
              "active": True
          },
          {
              "id": 4738437,
              "parents": "4292987_4376378",
              "name": "Cameroon",
              "has_children": True,
              "active": True
          },
          {
              "id": 4648269,
              "parents": "1869197_3171062",
              "name": "Canada",
              "has_children": True,
              "active": True
          },
          {
              "id": 4791061,
              "parents": "4292987_4301158",
              "name": "Cape Verde",
              "has_children": True,
              "active": True
          },
          {
              "id": 4631535,
              "parents": "1869197_4598172",
              "name": "Cayman Islands",
              "has_children": False,
              "active": True
          },
          {
              "id": 4796721,
              "parents": "4292987_4301633",
              "name": "Central African Republic",
              "has_children": True,
              "active": True
          },
          {
              "id": 4819480,
              "parents": "4292987_4508975",
              "name": "Chad",
              "has_children": True,
              "active": True
          },
          {
              "id": 5231683,
              "parents": "4024368_4124572",
              "name": "Chile",
              "has_children": True,
              "active": True
          },
          {
              "id": 4968195,
              "parents": "1463712_3370236",
              "name": "China",
              "has_children": True,
              "active": True
          },
          {
              "id": 5319463,
              "parents": "4024368_4139694",
              "name": "Colombia",
              "has_children": True,
              "active": True
          },
          {
              "id": 4861496,
              "parents": "4292987_4305028",
              "name": "Comoros",
              "has_children": True,
              "active": True
          },
          {
              "id": 4862203,
              "parents": "4292987_4305166",
              "name": "Congo-Brazzaville",
              "has_children": True,
              "active": True
          },
          {
              "id": 4631540,
              "parents": "1869197_4598173",
              "name": "Costa Rica",
              "has_children": False,
              "active": True
          },
          {
              "id": 6011481,
              "parents": "1219916_1634518",
              "name": "Croatia",
              "has_children": True,
              "active": True
          },
          {
              "id": 4634235,
              "parents": "4249245_4249625",
              "name": "Cuba",
              "has_children": True,
              "active": True
          },
          {
              "id": 4646982,
              "parents": "4024368_4606664",
              "name": "Curacao",
              "has_children": False,
              "active": True
          },
          {
              "id": 7571201,
              "parents": "1219916_4598174",
              "name": "Cyprus",
              "has_children": False,
              "active": True
          },
          {
              "id": 6043294,
              "parents": "1219916_1645920",
              "name": "Czechia",
              "has_children": True,
              "active": True
          },
          {
              "id": 4874496,
              "parents": "4292987_4386490",
              "name": "Democratic Republic of the Congo",
              "has_children": True,
              "active": True
          },
          {
              "id": 6085910,
              "parents": "1219916_1673692",
              "name": "Denmark",
              "has_children": True,
              "active": True
          },
          {
              "id": 4935565,
              "parents": "4292987_4497784",
              "name": "Djibouti",
              "has_children": True,
              "active": True
          },
          {
              "id": 4646987,
              "parents": "1869197_4598175",
              "name": "Dominica",
              "has_children": False,
              "active": True
          },
          {
              "id": 4648208,
              "parents": "4249245_4265856",
              "name": "Dominican Republic",
              "has_children": True,
              "active": True
          },
          {
              "id": 5743028,
              "parents": "1463712_4598176",
              "name": "East Timor",
              "has_children": False,
              "active": True
          },
          {
              "id": 5403399,
              "parents": "4024368_4198280",
              "name": "Ecuador",
              "has_children": True,
              "active": True
          },
          {
              "id": 4943455,
              "parents": "4292987_4522763",
              "name": "Egypt",
              "has_children": True,
              "active": True
          },
          {
              "id": 5462895,
              "parents": "1869197_4598177",
              "name": "El Salvador",
              "has_children": False,
              "active": True
          },
          {
              "id": 4968840,
              "parents": "4292987_4306616",
              "name": "Equatorial Guinea",
              "has_children": True,
              "active": True
          },
          {
              "id": 4970206,
              "parents": "4292987_4306741",
              "name": "Eritrea",
              "has_children": True,
              "active": True
          },
          {
              "id": 6094605,
              "parents": "1219916_1682387",
              "name": "Estonia",
              "has_children": True,
              "active": True
          },
          {
              "id": 4974421,
              "parents": "4292987_4527446",
              "name": "Ethiopia",
              "has_children": True,
              "active": True
          },
          {
              "id": 7559858,
              "parents": "1219916_3094900",
              "name": "Faroe Islands",
              "has_children": True,
              "active": True
          },
          {
              "id": 5743465,
              "parents": "4271351_4271352",
              "name": "Fiji",
              "has_children": True,
              "active": True
          },
          {
              "id": 6123311,
              "parents": "1219916_1693631",
              "name": "Finland",
              "has_children": True,
              "active": True
          },
          {
              "id": 6526325,
              "parents": "1219916_1880837",
              "name": "France",
              "has_children": True,
              "active": True
          },
          {
              "id": 4985640,
              "parents": "4292987_4307047",
              "name": "Gabon",
              "has_children": True,
              "active": True
          },
          {
              "id": 6870316,
              "parents": "1219916_2217102",
              "name": "Georgia",
              "has_children": True,
              "active": True
          },
          {
              "id": 5239003,
              "parents": "1219916_1366178",
              "name": "Germany",
              "has_children": True,
              "active": True
          },
          {
              "id": 4993039,
              "parents": "4292987_4529089",
              "name": "Ghana",
              "has_children": True,
              "active": True
          },
          {
              "id": 6874876,
              "parents": "1219916_2221662",
              "name": "Greece",
              "has_children": True,
              "active": True
          },
          {
              "id": 4655725,
              "parents": "1869197_4598178",
              "name": "Grenada",
              "has_children": False,
              "active": True
          },
          {
              "id": 4656068,
              "parents": "1219916_1880837_4546715",
              "name": "Guadeloupe",
              "has_children": True,
              "active": True
          },
          {
              "id": 5465676,
              "parents": "4249245_4258138",
              "name": "Guatemala",
              "has_children": True,
              "active": True
          },
          {
              "id": 5021523,
              "parents": "4292987_4537098",
              "name": "Guinea",
              "has_children": True,
              "active": True
          },
          {
              "id": 5066898,
              "parents": "4292987_4307382",
              "name": "Guinea-Bissau",
              "has_children": True,
              "active": True
          },
          {
              "id": 5475667,
              "parents": "4024368_4598179",
              "name": "Guyana",
              "has_children": False,
              "active": True
          },
          {
              "id": 4663478,
              "parents": "4249245_4260232",
              "name": "Haiti",
              "has_children": True,
              "active": True
          },
          {
              "id": 4687383,
              "parents": "1869197_4598180",
              "name": "Honduras",
              "has_children": False,
              "active": True
          },
          {
              "id": 5746536,
              "parents": "1463712_3370236_3373747",
              "name": "Hong Kong",
              "has_children": True,
              "active": True
          },
          {
              "id": 6885601,
              "parents": "1219916_2232387",
              "name": "Hungary",
              "has_children": True,
              "active": True
          },
          {
              "id": 7121681,
              "parents": "1219916_2469231",
              "name": "Iceland",
              "has_children": True,
              "active": True
          },
          {
              "id": 5810554,
              "parents": "1463712_3545561",
              "name": "India",
              "has_children": True,
              "active": True
          },
          {
              "id": 6095301,
              "parents": "1463712_3644700",
              "name": "Indonesia",
              "has_children": True,
              "active": True
          },
          {
              "id": 4677380,
              "parents": "1463712_3730722",
              "name": "Iran",
              "has_children": True,
              "active": True
          },
          {
              "id": 4870821,
              "parents": "1463712_3777815",
              "name": "Iraq",
              "has_children": True,
              "active": True
          },
          {
              "id": 6185987,
              "parents": "1219916_1714081",
              "name": "Ireland",
              "has_children": True,
              "active": True
          },
          {
              "id": 5101723,
              "parents": "1219916_1365943",
              "name": "Isle of Man",
              "has_children": True,
              "active": True
          },
          {
              "id": 4974050,
              "parents": "1463712_3801399",
              "name": "Israel",
              "has_children": True,
              "active": True
          },
          {
              "id": 4741864,
              "parents": "1219916_1219917",
              "name": "Italy",
              "has_children": True,
              "active": True
          },
          {
              "id": 5080602,
              "parents": "4292987_4307887",
              "name": "Ivory Coast",
              "has_children": True,
              "active": True
          },
          {
              "id": 4688035,
              "parents": "4249245_4267385",
              "name": "Jamaica",
              "has_children": True,
              "active": True
          },
          {
              "id": 6247345,
              "parents": "1463712_3805316",
              "name": "Japan",
              "has_children": True,
              "active": True
          },
          {
              "id": 4989354,
              "parents": "1463712_3830674",
              "name": "Jordan",
              "has_children": True,
              "active": True
          },
          {
              "id": 6301264,
              "parents": "1463712_3831963",
              "name": "Kazakhstan",
              "has_children": True,
              "active": True
          },
          {
              "id": 5114473,
              "parents": "4292987_4400184",
              "name": "Kenya",
              "has_children": True,
              "active": True
          },
          {
              "id": 6311445,
              "parents": "4271351_4606661",
              "name": "Kiribati",
              "has_children": False,
              "active": True
          },
          {
              "id": 7122423,
              "parents": "1219916_2469945",
              "name": "Kosovo",
              "has_children": True,
              "active": True
          },
          {
              "id": 4996306,
              "parents": "1463712_4598181",
              "name": "Kuwait",
              "has_children": False,
              "active": True
          },
          {
              "id": 6311446,
              "parents": "1463712_3841396",
              "name": "Kyrgyzstan",
              "has_children": True,
              "active": True
          },
          {
              "id": 6313072,
              "parents": "1463712_1532889",
              "name": "Laos",
              "has_children": True,
              "active": True
          },
          {
              "id": 7124392,
              "parents": "1219916_2471914",
              "name": "Latvia",
              "has_children": True,
              "active": True
          },
          {
              "id": 4998323,
              "parents": "1463712_3843022",
              "name": "Lebanon",
              "has_children": True,
              "active": True
          },
          {
              "id": 5129528,
              "parents": "4292987_4545785",
              "name": "Lesotho",
              "has_children": True,
              "active": True
          },
          {
              "id": 5156665,
              "parents": "4292987_4313556",
              "name": "Liberia",
              "has_children": True,
              "active": True
          },
          {
              "id": 5230982,
              "parents": "4292987_4332303",
              "name": "Libya",
              "has_children": True,
              "active": True
          },
          {
              "id": 7571168,
              "parents": "1219916_3106352",
              "name": "Liechtenstein",
              "has_children": True,
              "active": True
          },
          {
              "id": 7198002,
              "parents": "1219916_2545524",
              "name": "Lithuania",
              "has_children": True,
              "active": True
          },
          {
              "id": 7570108,
              "parents": "1219916_3105150",
              "name": "Luxembourg",
              "has_children": True,
              "active": True
          },
          {
              "id": 7219669,
              "parents": "1219916_2567957",
              "name": "Macedonia",
              "has_children": True,
              "active": True
          },
          {
              "id": 5240699,
              "parents": "4292987_4403140",
              "name": "Madagascar",
              "has_children": True,
              "active": True
          },
          {
              "id": 5266454,
              "parents": "4292987_4407622",
              "name": "Malawi",
              "has_children": True,
              "active": True
          },
          {
              "id": 6319188,
              "parents": "1463712_1501934",
              "name": "Malaysia",
              "has_children": True,
              "active": True
          },
          {
              "id": 6330700,
              "parents": "1463712_3844227",
              "name": "Maldives",
              "has_children": True,
              "active": True
          },
          {
              "id": 5282580,
              "parents": "4292987_4408793",
              "name": "Mali",
              "has_children": True,
              "active": True
          },
          {
              "id": 5102441,
              "parents": "1219916_1366066",
              "name": "Malta",
              "has_children": True,
              "active": True
          },
          {
              "id": 6331342,
              "parents": "4271351_4598182",
              "name": "Marshall Islands",
              "has_children": False,
              "active": True
          },
          {
              "id": 4687351,
              "parents": "1219916_1880837_1880838_2118015_2119008_2119009_2119681_2119732",
              "name": "Martinique",
              "has_children": False,
              "active": True
          },
          {
              "id": 5315048,
              "parents": "4292987_4333379",
              "name": "Mauritania",
              "has_children": True,
              "active": True
          },
          {
              "id": 5317035,
              "parents": "4292987_4333776",
              "name": "Mauritius",
              "has_children": True,
              "active": True
          },
          {
              "id": 5527660,
              "parents": "1869197_3119521",
              "name": "Mexico",
              "has_children": True,
              "active": True
          },
          {
              "id": 6331345,
              "parents": "4271351_4606658",
              "name": "Micronesia",
              "has_children": False,
              "active": True
          },
          {
              "id": 4631123,
              "parents": "1219916_1306964",
              "name": "Moldova",
              "has_children": True,
              "active": True
          },
          {
              "id": 7571202,
              "parents": "1219916_4598183",
              "name": "Monaco",
              "has_children": False,
              "active": True
          },
          {
              "id": 6331624,
              "parents": "1463712_3844548",
              "name": "Mongolia",
              "has_children": True,
              "active": True
          },
          {
              "id": 7221697,
              "parents": "1219916_2569985",
              "name": "Montenegro",
              "has_children": True,
              "active": True
          },
          {
              "id": 4687361,
              "parents": "1219916_2259346_2261513_2262206_2262298_2262335",
              "name": "Montserrat",
              "has_children": False,
              "active": True
          },
          {
              "id": 5327861,
              "parents": "4292987_4415476",
              "name": "Morocco",
              "has_children": True,
              "active": True
          },
          {
              "id": 5366819,
              "parents": "4292987_4422350",
              "name": "Mozambique",
              "has_children": True,
              "active": True
          },
          {
              "id": 6336174,
              "parents": "1463712_1539016",
              "name": "Myanmar",
              "has_children": True,
              "active": True
          },
          {
              "id": 5375988,
              "parents": "4292987_4334039",
              "name": "Namibia",
              "has_children": True,
              "active": True
          },
          {
              "id": 6353427,
              "parents": "4271351_4598184",
              "name": "Nauru",
              "has_children": False,
              "active": True
          },
          {
              "id": 6356252,
              "parents": "1463712_4009614",
              "name": "Nepal",
              "has_children": True,
              "active": True
          },
          {
              "id": 7224560,
              "parents": "1219916_2572877",
              "name": "Netherlands",
              "has_children": True,
              "active": True
          },
          {
              "id": 6374315,
              "parents": "4271351_4328987",
              "name": "New Zealand",
              "has_children": True,
              "active": True
          },
          {
              "id": 5758472,
              "parents": "4249245_4267808",
              "name": "Nicaragua",
              "has_children": True,
              "active": True
          },
          {
              "id": 5398979,
              "parents": "4292987_4334928",
              "name": "Niger",
              "has_children": True,
              "active": True
          },
          {
              "id": 5531618,
              "parents": "4292987_4423820",
              "name": "Nigeria",
              "has_children": True,
              "active": True
          },
          {
              "id": 6381233,
              "parents": "1463712_3852880",
              "name": "North Korea",
              "has_children": True,
              "active": True
          },
          {
              "id": 7233613,
              "parents": "1219916_2581940",
              "name": "Norway",
              "has_children": True,
              "active": True
          },
          {
              "id": 5005466,
              "parents": "1463712_4598185",
              "name": "Oman",
              "has_children": False,
              "active": True
          },
          {
              "id": 6386587,
              "parents": "1463712_3853816",
              "name": "Pakistan",
              "has_children": True,
              "active": True
          },
          {
              "id": 6407249,
              "parents": "1463712_4606657",
              "name": "Palestine",
              "has_children": False,
              "active": True
          },
          {
              "id": 5770756,
              "parents": "4249245_4254713",
              "name": "Panama",
              "has_children": True,
              "active": True
          },
          {
              "id": 6408058,
              "parents": "4271351_4272249",
              "name": "Papua New Guinea",
              "has_children": True,
              "active": True
          },
          {
              "id": 5779894,
              "parents": "4024368_4210383",
              "name": "Paraguay",
              "has_children": True,
              "active": True
          },
          {
              "id": 5794995,
              "parents": "4024368_4211948",
              "name": "Peru",
              "has_children": True,
              "active": True
          },
          {
              "id": 6421236,
              "parents": "1463712_3864150",
              "name": "Philippines",
              "has_children": True,
              "active": True
          },
          {
              "id": 7268096,
              "parents": "1219916_2726057",
              "name": "Poland",
              "has_children": True,
              "active": True
          },
          {
              "id": 7357229,
              "parents": "1219916_2815190",
              "name": "Portugal",
              "has_children": True,
              "active": True
          },
          {
              "id": 4687372,
              "parents": "1869197_3119521_3145087_3150334_3150469",
              "name": "Puerto Rico",
              "has_children": False,
              "active": True
          },
          {
              "id": 5005477,
              "parents": "1463712_4598187",
              "name": "Qatar",
              "has_children": False,
              "active": True
          },
          {
              "id": 7253893,
              "parents": "1219916_2711849",
              "name": "Romania",
              "has_children": True,
              "active": True
          },
          {
              "id": 7373436,
              "parents": "1219916_2831409",
              "name": "Russia",
              "has_children": True,
              "active": True
          },
          {
              "id": 5769525,
              "parents": "4292987_4349318",
              "name": "Rwanda",
              "has_children": True,
              "active": True
          },
          {
              "id": 5771266,
              "parents": "4292987_4497969",
              "name": "Saint Helena, Ascension and Tristan da Cunha",
              "has_children": True,
              "active": True
          },
          {
              "id": 4690551,
              "parents": "1869197_4598188",
              "name": "Saint Kitts and Nevis",
              "has_children": False,
              "active": True
          },
          {
              "id": 4690562,
              "parents": "1869197_4598189",
              "name": "Saint Lucia",
              "has_children": False,
              "active": True
          },
          {
              "id": 6454313,
              "parents": "4271351_4598191",
              "name": "Samoa",
              "has_children": False,
              "active": True
          },
          {
              "id": 7571203,
              "parents": "1219916_4598192",
              "name": "San Marino",
              "has_children": False,
              "active": True
          },
          {
              "id": 5005487,
              "parents": "1463712_4594412",
              "name": "Saudi Arabia",
              "has_children": False,
              "active": True
          },
          {
              "id": 5776936,
              "parents": "4292987_4532161",
              "name": "Senegal",
              "has_children": True,
              "active": True
          },
          {
              "id": 6892804,
              "parents": "1219916_2240320",
              "name": "Serbia",
              "has_children": True,
              "active": True
          },
          {
              "id": 5788400,
              "parents": "4292987_4350043",
              "name": "Seychelles",
              "has_children": True,
              "active": True
          },
          {
              "id": 5788535,
              "parents": "4292987_4350178",
              "name": "Sierra Leone",
              "has_children": True,
              "active": True
          },
          {
              "id": 6454314,
              "parents": "1463712_1468081",
              "name": "Singapore",
              "has_children": True,
              "active": True
          },
          {
              "id": 6898504,
              "parents": "1219916_2246020",
              "name": "Slovakia",
              "has_children": True,
              "active": True
          },
          {
              "id": 6904948,
              "parents": "1219916_2252464",
              "name": "Slovenia",
              "has_children": True,
              "active": True
          },
          {
              "id": 6454498,
              "parents": "4271351_4598193",
              "name": "Solomon Islands",
              "has_children": False,
              "active": True
          },
          {
              "id": 5800373,
              "parents": "4292987_4357508",
              "name": "Somalia",
              "has_children": True,
              "active": True
          },
          {
              "id": 5851119,
              "parents": "4292987_4474765",
              "name": "South Africa",
              "has_children": True,
              "active": True
          },
          {
              "id": 6454499,
              "parents": "1463712_3889079",
              "name": "South Korea",
              "has_children": True,
              "active": True
          },
          {
              "id": 5904018,
              "parents": "4292987_4486913",
              "name": "South Sudan",
              "has_children": True,
              "active": True
          },
          {
              "id": 6911830,
              "parents": "1219916_2259346",
              "name": "Spain",
              "has_children": True,
              "active": True
          },
          {
              "id": 6476468,
              "parents": "1463712_3911048",
              "name": "Sri Lanka",
              "has_children": True,
              "active": True
          },
          {
              "id": 5908946,
              "parents": "4292987_4487820",
              "name": "Sudan",
              "has_children": True,
              "active": True
          },
          {
              "id": 5919327,
              "parents": "4024368_4156602",
              "name": "Suriname",
              "has_children": True,
              "active": True
          },
          {
              "id": 5913114,
              "parents": "4292987_4488772",
              "name": "Swaziland",
              "has_children": True,
              "active": True
          },
          {
              "id": 6970613,
              "parents": "1219916_2318129",
              "name": "Sweden",
              "has_children": True,
              "active": True
          },
          {
              "id": 7014684,
              "parents": "1219916_2362200",
              "name": "Switzerland",
              "has_children": True,
              "active": True
          },
          {
              "id": 5023757,
              "parents": "1463712_3991737",
              "name": "Syria",
              "has_children": True,
              "active": True
          },
          {
              "id": 5771916,
              "parents": "4292987_4498072",
              "name": "São Tomé and Príncipe",
              "has_children": True,
              "active": True
          },
          {
              "id": 6481253,
              "parents": "1463712_3915833",
              "name": "Taiwan",
              "has_children": True,
              "active": True
          },
          {
              "id": 6502545,
              "parents": "1463712_3937125",
              "name": "Tajikistan",
              "has_children": True,
              "active": True
          },
          {
              "id": 5919073,
              "parents": "4292987_4492722",
              "name": "Tanzania",
              "has_children": True,
              "active": True
          },
          {
              "id": 6503996,
              "parents": "1463712_1508507",
              "name": "Thailand",
              "has_children": True,
              "active": True
          },
          {
              "id": 5937887,
              "parents": "4292987_4544904",
              "name": "The Gambia",
              "has_children": True,
              "active": True
          },
          {
              "id": 5942465,
              "parents": "4292987_4488868",
              "name": "Togo",
              "has_children": True,
              "active": True
          },
          {
              "id": 5949068,
              "parents": "4292987_4489605",
              "name": "Tunisia",
              "has_children": True,
              "active": True
          },
          {
              "id": 7028016,
              "parents": "1219916_2375532",
              "name": "Turkey",
              "has_children": True,
              "active": True
          },
          {
              "id": 6520631,
              "parents": "1463712_3938576",
              "name": "Turkmenistan",
              "has_children": True,
              "active": True
          },
          {
              "id": 5969711,
              "parents": "4292987_4498504",
              "name": "Uganda",
              "has_children": True,
              "active": True
          },
          {
              "id": 7084353,
              "parents": "1219916_2431869",
              "name": "Ukraine",
              "has_children": True,
              "active": True
          },
          {
              "id": 5094948,
              "parents": "1463712_4598195",
              "name": "United Arab Emirates",
              "has_children": False,
              "active": True
          },
          {
              "id": 6320926,
              "parents": "1219916_1800795",
              "name": "United Kingdom",
              "has_children": True,
              "active": True
          },
          {
              "id": 4923589,
              "parents": "1869197_1869198",
              "name": "United States",
              "has_children": True,
              "active": True
          },
          {
              "id": 5920946,
              "parents": "4024368_4156787",
              "name": "Uruguay",
              "has_children": True,
              "active": True
          },
          {
              "id": 6521300,
              "parents": "1463712_4018092",
              "name": "Uzbekistan",
              "has_children": True,
              "active": True
          },
          {
              "id": 6527336,
              "parents": "4271351_4598196",
              "name": "Vanuatu",
              "has_children": False,
              "active": True
          },
          {
              "id": 5934503,
              "parents": "4024368_4157704",
              "name": "Venezuela",
              "has_children": True,
              "active": True
          },
          {
              "id": 6529535,
              "parents": "1463712_1525142",
              "name": "Vietnam",
              "has_children": True,
              "active": True
          },
          {
              "id": 4690573,
              "parents": "1869197_4606663",
              "name": "Virgin Islands, British",
              "has_children": False,
              "active": True
          },
          {
              "id": 4690583,
              "parents": "1869197_4606662",
              "name": "Virgin Islands, U.S.",
              "has_children": False,
              "active": True
          },
          {
              "id": 5122296,
              "parents": "1463712_3944250",
              "name": "Yemen",
              "has_children": True,
              "active": True
          },
          {
              "id": 5996714,
              "parents": "4292987_4507589",
              "name": "Zambia",
              "has_children": True,
              "active": True
          },
          {
              "id": 5999327,
              "parents": "4292987_4508240",
              "name": "Zimbabwe",
              "has_children": True,
              "active": True
          }
      ]
    },
    "industry_focus": {
        "name": "industry_focus",
        "values": [
        {
            "id": 4564019,
            "parents": "4564019",
            "name": "Agriculture",
            "has_children": True,
            "active": True
        },
        {
            "id": 4564002,
            "parents": "4564002",
            "name": "Automotive",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563183,
            "parents": "4563183",
            "name": "Beverages",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563824,
            "parents": "4563824",
            "name": "Business Services",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563526,
            "parents": "4563526",
            "name": "Chemicals",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563848,
            "parents": "4563848",
            "name": "Construction & Real Estate",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563891,
            "parents": "4563891",
            "name": "Consulting",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563865,
            "parents": "4563865",
            "name": "Consumer Goods & Services",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563580,
            "parents": "4563580",
            "name": "Defence & Security",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563215,
            "parents": "4563215",
            "name": "Education & Training",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563976,
            "parents": "4563976",
            "name": "Energy & Utilities",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563927,
            "parents": "4563927",
            "name": "Finance & Insurance",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563323,
            "parents": "4563323",
            "name": "Food",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563684,
            "parents": "4563684",
            "name": "Government",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563630,
            "parents": "4563630",
            "name": "Hire & Rental",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563679,
            "parents": "4563679",
            "name": "Human Resources",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563106,
            "parents": "4563106",
            "name": "Information Technology",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563176,
            "parents": "4563176",
            "name": "Legal",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563082,
            "parents": "4563082",
            "name": "Leisure & Entertainment",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563600,
            "parents": "4563600",
            "name": "Manufacturing",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563477,
            "parents": "4563477",
            "name": "Marketing, Sales & PR",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563149,
            "parents": "4563149",
            "name": "Media",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563698,
            "parents": "4563698",
            "name": "Metals",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563445,
            "parents": "4563445",
            "name": "Mining & Minerals",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563314,
            "parents": "4563314",
            "name": "Nonprofit Organisations",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563288,
            "parents": "4563288",
            "name": "Oil & Gas",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563801,
            "parents": "4563801",
            "name": "Paper, Wood & Furniture",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563742,
            "parents": "4563742",
            "name": "Pharmaceutical & Medical",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563294,
            "parents": "4563294",
            "name": "Retail",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563815,
            "parents": "4563815",
            "name": "Telecommunication",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563495,
            "parents": "4563495",
            "name": "Textile",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563165,
            "parents": "4563165",
            "name": "Tourism",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563227,
            "parents": "4563227",
            "name": "Transport & Logistics",
            "has_children": True,
            "active": True
        },
        {
            "id": 4563648,
            "parents": "4563648",
            "name": "Wholesale",
            "has_children": True,
            "active": True
        }
    ]
  }
}
#     {
#       "name": "Seniority",
#       "method": "GET",
#       "path": "/nomenclatures/seniority",
#       "description": "Retrieve a list of seniority levels.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of seniority nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Department",
#       "method": "GET",
#       "path": "/nomenclatures/department",
#       "description": "Retrieve a list of departments.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of department nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Activity Type",
#       "method": "GET",
#       "path": "/nomenclatures/activity-type",
#       "description": "Retrieve a list of activity types.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of activity type nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Company Type",
#       "method": "GET",
#       "path": "/nomenclatures/company-type",
#       "description": "Retrieve a list of company types.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of company type nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Company Status",
#       "method": "GET",
#       "path": "/nomenclatures/company-status",
#       "description": "Retrieve a list of company statuses.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of company status nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Legal Form",
#       "method": "GET",
#       "path": "/nomenclatures/legal-form",
#       "description": "Retrieve a list of legal forms.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of legal form nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Industry Focus",
#       "method": "GET",
#       "path": "/nomenclatures/industry-focus",
#       "description": "Retrieve a list of industry focuses.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of industry focus nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "International SIC Code",
#       "method": "GET",
#       "path": "/nomenclatures/isic",
#       "description": "Retrieve a list of international SIC codes.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of international SIC code nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "NACE Rev. 2",
#       "method": "GET",
#       "path": "/nomenclatures/nace",
#       "description": "Retrieve NACE Rev. 2 codes.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of NACE Rev. 2 nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Country SIC Codes",
#       "method": "GET",
#       "path": "/nomenclatures/country-sic-codes",
#       "description": "Retrieve country-specific SIC codes.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of country SIC code nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Countries",
#       "method": "GET",
#       "path": "/nomenclatures/countries",
#       "description": "Retrieve a list of countries.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of countries."
#         }
#       }
#     },
#     {
#       "name": "Regions",
#       "method": "GET",
#       "path": "/nomenclatures/regions",
#       "description": "Retrieve a list of regions.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of regions."
#         }
#       }
#     },
#     {
#       "name": "States US & CA",
#       "method": "GET",
#       "path": "/nomenclatures/states",
#       "description": "Retrieve states for US & Canada.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of states for US & CA."
#         }
#       }
#     },
#     {
#       "name": "Technologies",
#       "method": "GET",
#       "path": "/nomenclatures/technologies",
#       "description": "Retrieve a list of technologies.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of technology nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Currency",
#       "method": "GET",
#       "path": "/nomenclatures/currency",
#       "description": "Retrieve a list of currencies.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of currency nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Advance contacts",
#       "method": "GET",
#       "path": "/nomenclatures/advance-contacts",
#       "description": "Retrieve a list of advance contact options.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of advance contacts nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Trading Activity",
#       "method": "GET",
#       "path": "/nomenclatures/trading-activity",
#       "description": "Retrieve a list of trading activities.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of trading activity nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Ownership Parents",
#       "method": "GET",
#       "path": "/nomenclatures/ownership-parents",
#       "description": "Retrieve a list of ownership parent companies.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of ownership parent nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Website monthly visits",
#       "method": "GET",
#       "path": "/nomenclatures/website-monthly-visits",
#       "description": "Retrieve website monthly visit data classifications.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of website monthly visits nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Alexa ranking",
#       "method": "GET",
#       "path": "/nomenclatures/alexa-ranking",
#       "description": "Retrieve Alexa ranking data classifications.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of Alexa ranking nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Only Select Companies That",
#       "method": "GET",
#       "path": "/nomenclatures/only-select-companies-that",
#       "description": "Retrieve options for filtering companies.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of filtering options."
#         }
#       }
#     },
#     {
#       "name": "Foreign Parent",
#       "method": "GET",
#       "path": "/nomenclatures/foreign-parent",
#       "description": "Retrieve foreign parent company data classifications.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of foreign parent nomenclatures."
#         }
#       }
#     },
#     {
#       "name": "Consolidated Accounts",
#       "method": "GET",
#       "path": "/nomenclatures/consolidated-accounts",
#       "description": "Retrieve consolidated accounts data classifications.",
#       "parameters": [],
#       "responses": {
#         "200": {
#           "description": "List of consolidated accounts nomenclatures."
#         }
#       }
#     }
#   ]
# }