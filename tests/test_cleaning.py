import pandas as pd
from src.data_cleaning import clean_transactions

def test_clean_transactions():
    raw = pd.DataFrame({
        "Invoice_ID": ["I1"], "Order_Date": ["2026-01-01"], "Customer_ID": [None],
        "Customer_Type": [" Member "], "Gender": ["F"], "Product_Line": [" Food "],
        "Unit_Price": ["₹ 100.50"], "Quantity": ["2"], "Total_Sales": ["₹ 201.00"],
    })
    result = clean_transactions(raw)
    assert result.loc[0, "Customer_ID"] == "C000"
    assert result.loc[0, "Product_Category"] == "Food"
    assert result.loc[0, "Unit_Price"] == 100.50
