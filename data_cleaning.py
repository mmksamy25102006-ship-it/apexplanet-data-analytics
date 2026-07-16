import pandas as pd

# Load dataset
df = pd.read_csv("../data/Superstore.csv", encoding="latin1")

# Display dataset shape
print("Original Dataset Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("../data/Superstore_Cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("New Dataset Shape:", df.shape)