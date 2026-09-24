# Data Dictionary

The repository is aligned to the supplied customer shopping behavior CSV.

| Field | Type | Business meaning | Analysis use |
|---|---|---|---|
| customer_id | Integer | Customer identifier | Customer-level analysis |
| age | Integer | Customer age | Demographic segmentation |
| gender | Categorical | Customer gender | Demographic analysis |
| item_purchased | Categorical | Purchased item | Product analysis |
| category | Categorical | Product category | Revenue analysis |
| purchase_amount | Numeric | Purchase value | Revenue and basket-value analysis |
| location | Categorical | Customer location/state | Geographic analysis |
| size | Categorical | Purchased size | Preference analysis |
| color | Categorical | Purchased color | Preference analysis |
| season | Categorical | Season | Seasonal analysis |
| review_rating | Numeric | Customer review rating | Experience analysis |
| subscription_status | Binary | Subscription indicator | Subscription analysis |
| shipping_type | Categorical | Shipping option | Fulfillment analysis |
| discount_applied | Binary | Whether a discount was applied | Promotion analysis |
| previous_purchases | Integer | Historical purchase count in snapshot | Engagement analysis |
| payment_method | Categorical | Payment method | Payment behavior |
| frequency_of_purchases | Categorical | Purchase-frequency label | Engagement segmentation |
| age_group | Categorical | Derived age band | Demographic segmentation |
| purchase_frequency_days | Integer | Numeric interval represented by frequency label | Engagement-risk heuristic |

## Data quality

- 500 rows
- 19 columns
- No missing values
- customer_id is unique

## Modeling limitation

There is no purchase date and no repeated transaction history. Classical Recency and a true 180-day churn label therefore cannot be computed from this file alone.
