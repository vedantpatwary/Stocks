import requests
import openai
import os

# Set your Azure OpenAI credentials
AZURE_OPENAI_ENDPOINT = "https://fhlhack.openai.azure.com/"
AZURE_OPENAI_KEY = ""
DEPLOYMENT_NAME = "gpt-4o-mini"  # Model name (e.g., "gpt-4", "gpt-35-turbo")

openai.client = openai.AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-15-preview",  # Update if needed
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def fetch_html(url):
    """Fetches the raw HTML content from the Screener page."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": f"https://www.screener.in/company/6596661/"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch the page")
        return None
    return response.text

def extract_stock_data_with_llm(html_content):
    """Uses Azure OpenAI to extract stock details from HTML."""
    prompt = f"""
    Extract the following stock details from the HTML below:
    - Profit Var 5Yrs
    - ROCE
    - 52-Week High
    - Market Cap
    - Current Price

    Provide the response in a structured JSON format.

    HTML Content:
    {html_content[:5000]}  # Truncate to stay within token limits
    """

    response = openai.client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You extract financial data from raw HTML."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# Example Usage
url = "https://www.screener.in/api/company/6596661/quick_ratios/"
html_content = fetch_html(url)

if html_content:
    stock_data = extract_stock_data_with_llm(html_content)
    print(stock_data)
