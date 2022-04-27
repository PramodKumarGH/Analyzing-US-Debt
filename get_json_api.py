import requests
import json
import csv

class c_us_debt:

    def __init__(self, out_file_nm, start_dt, end_dt):

        # Set the base URL.
        self.base_url = 'https://www.treasurydirect.gov/NP_WS/debt/search'

        # Set the parameter variables for the API request.
        self.out_file_nm = out_file_nm
        self.start_dt = start_dt
        self.end_dt = end_dt

        # Get data in JSON format
        self.get_data()

    def get_data(self):

        # Build the full URL. Then, request the data through the Debt Information API. 
        # Write the returned JSON structure to the specified folder and file.

        # Create full URL and retrieve data structure in JSON format by calling API with get() function.
        full_url = self.base_url + '?startdate=' + self.start_dt + '&enddate=' + self.end_dt + '&format=json'
        json_structure = requests.get(full_url)

        # Write JSON data structure to file.
        with open(self.out_file_nm, "w") as out_file:
            out_file.write(json_structure.text)
c_us_debt((r'C:\Users\pramo\Desktop\websitedata.json'), '2002-01-01', '2022-04-21')
