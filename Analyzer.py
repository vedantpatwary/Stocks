import openai
import json
import CsvWriter
import Keys

AZURE_OPENAI_ENDPOINT = Keys.AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_KEY = Keys.AZURE_OPENAI_KEY
DEPLOYMENT_NAME = Keys.DEPLOYMENT_NAME

openai.client = openai.AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-15-preview",  # Update if needed
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def get_stock_analysis(file_path):


    headers, stock_data = CsvWriter.read_csv(file_path)

    # Convert stock data into CSV string format
    csv_data = CsvWriter.format_csv_string(headers, stock_data)

    print("---------")
    print(csv_data)
    print("---------")
    prompt = f"""
    Analyze the following stock market data and provide insights in JSON format.
    For each stock, highlight:
    - Profit growth
    - Debt level
    - Valuation (P/E ratio, P/B ratio)
    - Promoter holding
    - Key observations.

    ## Stock Data (CSV Format)
    ```
    {csv_data}
    ```

    **Response Format:**
    ```json
    [
        {{
            "StockName": "Stock Name",
            "Analysis": ["Observation 1", "Observation 2", ...],
            "Recommendation": "StrongBuy/Buy/Hold/Sell/StrongSell",
        }}
    ]
    ```
    """
    
    response = openai.client.chat.completions.create(
        model=DEPLOYMENT_NAME,  
        messages=[{"role": "system", "content": "You are an expert financial analyst."},
                  {"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content