import pandas as pd

# Read raw data
portfolio_data = pd.read_csv('data/pf_export.csv')

# Extract relevant columns
transactions = portfolio_data[['Category', 'Amount']]

# Filter transactions with negative amounts
expenses = transactions[transactions['Amount'] < 0]

# Set source for personal transactions
expenses['source'] = 'Personal'

# Convert negative amounts to positive
expenses['Amount'] = expenses['Amount'] * -1

# Rename columns for clarity
expenses = expenses.rename(columns={"Category": "target",
                                    "Amount": "value"})

# Group expenses by source and target
grouped_expenses = expenses.groupby(['source', 'target'])

# Summarize and save grouped data
grouped_expenses.sum().reset_index().to_csv('./data/grouped_personal.csv',
                                            index=False, columns=['source', 'target', 'value'])

# Read additional data
manual_portfolio_data = pd.read_csv('data/man_pf.csv')
sumval = manual_portfolio_data[~manual_portfolio_data['source'].isin(['Income', 'Planned Outgoing', 'Personal Addons'])].sum(
)

# Create a copy for further processing
processed_data = manual_portfolio_data.copy()

# Calculate percentage values based on the total value
processed_data['value'] = (
    manual_portfolio_data['value'] / sumval['value']) * 100

# Round the percentage values to one decimal place
processed_data['value'] = processed_data['value'].round(1)

# Reset index and save the results
processed_data.reset_index().to_csv('./data/result.csv',
                                    index=False, columns=['source', 'target', 'value'])
