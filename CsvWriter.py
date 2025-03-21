import csv
import os
import pandas as pd

def save_financial_ratios_to_csv(stock_ratios_map, file_path):
    """
    Saves a dictionary of StockName -> FinancialRatios objects to a CSV file.

    Parameters:
    - stock_ratios_map: dict[str, FinancialRatios] - Mapping of stock names to financial ratio objects.
    - file_path: str - Relative or absolute path to save the CSV file.
    """
    # Get the full path relative to the script location
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    full_path = os.path.join(base_dir, file_path)  # Append relative path
    print(f"Saving CSV at: {full_path}")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # Extract field names dynamically
    field_names = ["Name"] + list(vars(next(iter(stock_ratios_map.values()))).keys())

    # Write to CSV
    with open(full_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()

        for stock_name, ratios in stock_ratios_map.items():
            row = {"Name": stock_name, **vars(ratios)}
            writer.writerow(row)

    print(f"CSV file saved at: {full_path}")

def read_csv(file_path):
    """Reads CSV file and returns stock data as a dictionary with headers dynamically detected."""
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames  # Dynamically get headers
        stock_data = [row for row in reader]  # Read all rows into a list
    return headers, stock_data

def format_csv_string(headers, stock_data):
    """Converts stock data into a CSV-formatted string for efficient token usage."""
    csv_string = ",".join(headers) + "\n"
    csv_string += "\n".join([",".join(row[h] for h in headers) for row in stock_data])
    return csv_string