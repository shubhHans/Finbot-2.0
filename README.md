# Finbot-2.0
This project presents a Proof of Concept for a Financial Advisor Chatbot built using LangChain, OpenAI, and Streamlit. The chatbot enables financial advisors to interact with client portfolio data and target asset allocations using natural language queries, delivering accurate and explainable responses in a user-friendly chat interface.
## Data

The chatbot uses two CSV files - that must be upload on the page - to answer questions from:

### Client Target Allocations ('client_target_allocations.csv')

This dataset contains information about the target allocations for various clients. Each row represents a specific asset class allocation target for a particular client. The columns in this dataset are:

- **Client**: The name or identifier of the client.
- **Target Portfolio**: The type of portfolio (e.g., Balanced) the client is aiming for.
- **Asset Class**: The category of assets (e.g., Bonds, ETFs, Cash, Stocks).
- **Target Allocation (%)**: The percentage of the total portfolio that should be allocated to the specified asset class.

### Financial Advisor Clients ('financial_advisor_clients.csv')

This dataset contains detailed information about the current holdings of various clients. Each row represents a specific holding for a client. 
The columns in this dataset are:

- **Client Symbol**: The identifier for the client.
- **Name**: The name of the asset or stock.
- **Sector**: The sector to which the asset belongs (e.g., Technology, Communication Services).
- **Quantity**: The number of shares or units held.
- **Buy Price**: The price at which the asset was purchased.
- **Current Price**: The current market price of the asset.
- **Market Value**: The total market value of the holding (Quantity * Current Price).
- **Purchase Date**: The date the asset was purchased.
- **Dividend Yield**: The dividend yield of the asset.
- **P/E Ratio**: The price-to-earnings ratio of the asset.
- **52-Week High**: The highest price of the asset in the past 52 weeks.
- **52-Week Low**: The lowest price of the asset in the past 52 weeks.
- **Analyst Rating**: The current analyst rating for the asset (e.g., Buy, Hold).
- **Target Price**: The target price set by analysts.
- **Risk Level**: The risk level associated with the asset (e.g., Low, Medium).
## Usage

- Set environment
```
streamlit run app.py
```
- Enter your OpenAI API key.
- Upload CSV files
- Start asking questions in the chat interface.
## Example questions

- "What is the portfolio for Client 1?"
- "How much does Client 1 allocate to ETFs"
- "What is the target allocation by sector for Client 1?"
- "What is the current market value of Amazon.com Inc. for Client 1?"
- "What are the target allocations for Client 2?"
- "Can you provide the sector distribution for Client 1's portfolio?"
- "What is the risk level of Client 1's holdings?"
- "What is the total dividend yield for Client 1's portfolio?"
- "What are the analyst ratings for the stocks in Client 2's portfolio?"
- "What is the 52-week high and low for Alphabet Inc. in Client 1's portfolio?"
- "When was Tesla Inc. purchased by Client 1?"
