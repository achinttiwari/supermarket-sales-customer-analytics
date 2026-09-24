# Data Dictionary

| Field | Type | Business meaning | Analysis use |
|---|---|---|---|
| Invoice_ID | Identifier | Unique transaction invoice number | Order auditing |
| Order_Date | Date | Date payment was processed | Time-series and seasonality |
| Customer_ID | Identifier | Unique customer account reference | Customer aggregation |
| Customer_Type | Categorical | Member vs Normal | Segment comparison |
| Gender | Categorical | Customer gender identification | Demographic analysis |
| Product_Category | Categorical | Merchandise line item | Inventory and sales split |
| Unit_Price | Numeric | Price per single item (INR) | Margin analysis |
| Quantity | Numeric | Number of units purchased | Volume calculation |
| Total_Sales | Numeric | Revenue generated per order | Financial performance |

The source guide also uses Branch and Rating in the demo/dashboard. The implementation treats these as optional fields. Product_Line is accepted as an alias for Product_Category.
