import yfinance as yf
import pandas as pd

ticker_symbol = "^NSEI"

start_date = "2015-04-01"
end_date = "2025-03-31"

print("Downloading Monthly Historical Data for NIFTY 50...")
try:
    monthly_data = yf.download(ticker_symbol,
                               start=start_date,
                               end=end_date,
                               interval="1mo",
                               progress=False)

    if not monthly_data.empty:
        print("Monthly Data Download Complete.")
        
        monthly_data.to_csv('nifty50_monthly_data.csv')
        print("Monthly data has been saved")

        print("\n--- First 5 Rows of Monthly Data ---")
        print(monthly_data.head(5))
        print("\n--- Last 5 Rows of Monthly Data ---")
        print(monthly_data.tail(5))
    else:
        print("No monthly data found for the specified date range.")

except Exception as e:
    print(f"An error occurred while downloading monthly data: {e}")