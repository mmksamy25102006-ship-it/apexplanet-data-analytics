# Import required libraries
import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("../data/Superstore.db")

print("Database Connected Successfully!")

# Load the cleaned dataset
df = pd.read_csv("../data/Superstore_Cleaned.csv")

# Rename columns (replace spaces with underscores)
df.columns = df.columns.str.replace(" ", "_")

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Store data into SQLite database
df.to_sql(
    "superstore",
    conn,
    if_exists="replace",
    index=False
)

print("Data Imported Successfully!")

# Display first 5 rows
print(df.head())

# Close the connection
conn.close()

print("Database Connection Closed.")