import pandas as pd
import random
import numpy as np

# Define NSE stocks
nse_stocks = ["KCB", "KPLC", "SCOM", "EABL", "EQTY", "KUKZ", "SCBK", "TCL", "LMT", "JUB"]

# Generate random transaction data
num_transactions = 1000  # 1000 transactions
num_traders = 200  # 200 unique traders

trader_ids = [f"T{str(i).zfill(4)}" for i in range(1, num_traders + 1)]  # 200 unique trader IDs

# Generate transaction dataset
transactions_data = {
    "Transaction_ID": [f"TX{str(i).zfill(5)}" for i in range(1, num_transactions + 1)],
    "Trader_ID": np.random.choice(trader_ids, num_transactions),
    "Stock_Ticker": np.random.choice(nse_stocks, num_transactions),
    "Trade_Type": np.random.choice(["BUY", "SELL"], num_transactions),
    "Volume": np.random.randint(10, 1000, num_transactions),
    "Price_per_Share": np.round(np.random.uniform(10, 500, num_transactions), 2),
    "Transaction_Date": pd.date_range(start="2024-01-01", periods=num_transactions, freq="T").strftime("%Y-%m-%d %H:%M:%S")
}

# Create DataFrame
df_transactions = pd.DataFrame(transactions_data)

# Calculate total transaction amount
df_transactions["Total_Amount"] = df_transactions["Volume"] * df_transactions["Price_per_Share"]

# Save as CSV
df_transactions.to_csv("nse_broker_transactions_final.csv", index=False)

# Generate unique trader names
first_names = ["James", "John", "Mary", "Jane", "Peter", "Grace", "David", "Daniel", "Lucy", "Joseph",
               "Catherine", "Paul", "Samuel", "Anne", "Stephen", "Caroline", "Michael", "Alice", "Patrick", "Mercy"]
last_names = ["Mwangi", "Ochieng", "Kariuki", "Odhiambo", "Mutua", "Wanjiru", "Kimani", "Atieno", "Kipchoge", "Muthoni",
              "Njoroge", "Onyango", "Kamau", "Wambui", "Omolo", "Chebet", "Okoth", "Waithera", "Otieno", "Ndungu"]

kenyan_names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(num_traders)]

# Create DataFrame for traders' account names
account_data_kenyan = pd.DataFrame({
    "Trader_ID": trader_ids,
    "Account_Name": kenyan_names
})

# Save as CSV
account_data_kenyan.to_csv("nse_trader_accounts_kenyan.csv", index=False)

print("Datasets generated successfully: 'nse_broker_transactions_final.csv' and 'nse_trader_accounts_kenyan.csv'")
