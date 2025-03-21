
from Model.FinancialRatios import FinancialRatios
import Auth.chromeDriver as chromeDriver
import Constants
import CsvWriter
from Controller.ScreenerController import ScreenerController

api_url = "https://www.screener.in/api/company/6596661/quick_ratios/"

headers = Constants.headers

cookies_dict = chromeDriver.getCookies()

controller = ScreenerController()
responseMap = {}
for stock_name, company_id in Constants.stock_to_company_id.items():
    responseMap[stock_name] = controller.get_quick_ratios(company_id, cookies_dict)
# Loop through the stock_to_company_id dictionary
financial = controller.get_quick_ratios(6596661, cookies_dict)
print(financial)

CsvWriter.save_financial_ratios_to_csv(responseMap,"/Users/vedantpatwary/Desktop/PersonalProjects/Stocks/results/quick_ratios.csv")

