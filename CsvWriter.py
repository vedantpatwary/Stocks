import csv
import os

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
