import Constants
from bs4 import BeautifulSoup
import requests
from Model.FinancialRatios import FinancialRatios

class ScreenerController:
    def __init__(self):
        pass
    def get_quick_ratios(self, company_id, cookies_dict):
        api_url = f"https://www.screener.in/api/company/{company_id}/quick_ratios/"
        headers = Constants.headers
        response = ScreenerController.getApiResponse(api_url, headers,cookies_dict)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract all data
            ratios = {}
            for item in soup.find_all("li", class_="flex flex-space-between"):
                name_tag = item.find("span", class_="name")
                value_tag = item.find("span", class_="number")

                if name_tag and value_tag:
                    name = name_tag.get_text(strip=True)
                    value = value_tag.get_text(strip=True)
                    ratios[name] = value
            return FinancialRatios(ratios)
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
            print(response.text)  # Print error details if any
            return None
    
    def getApiResponse(api_url, headers,cookies):
        response = requests.get(api_url, headers=headers, cookies=cookies)
        return response