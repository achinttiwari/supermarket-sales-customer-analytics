import pandas as pd

from src.data_cleaning import clean_customer_shopping_data


def test_clean_customer_shopping_data_derives_fields():
    raw = pd.DataFrame({
        "customer_id": [1],
        "age": [25],
        "gender": [" Female "],
        "item_purchased": [" Jacket "],
        "category": [" Outerwear "],
        "purchase_amount": ["₹ 100.50"],
        "location": [" Delhi "],
        "size": ["M"],
        "color": ["Blue"],
        "season": ["Winter"],
        "review_rating": [4.2],
        "subscription_status": ["Yes"],
        "shipping_type": ["Express"],
        "discount_applied": ["No"],
        "previous_purchases": [8],
        "payment_method": ["Cash"],
        "frequency_of_purchases": ["Weekly"],
    })
    result = clean_customer_shopping_data(raw)
    assert len(result) == 1
    assert result.loc[0, "gender"] == "Female"
    assert result.loc[0, "purchase_amount"] == 100.50
    assert result.loc[0, "purchase_frequency_days"] == 7
    assert result.loc[0, "age_group"] == "18-25"
    assert result.loc[0, "subscription_status"] == 1
    assert result.loc[0, "discount_applied"] == 0


def test_cleaning_preserves_subscription_and_discount_rates():
    raw = pd.DataFrame({
        "customer_id": [1, 2],
        "age": [25, 30],
        "gender": ["Female", "Male"],
        "item_purchased": ["Jacket", "Shoes"],
        "category": ["Outerwear", "Footwear"],
        "purchase_amount": [100, 200],
        "location": ["Delhi", "Mumbai"],
        "size": ["M", "L"],
        "color": ["Blue", "Black"],
        "season": ["Winter", "Summer"],
        "review_rating": [4, 3],
        "subscription_status": ["Yes", "No"],
        "shipping_type": ["Express", "Standard"],
        "discount_applied": ["Yes", "No"],
        "previous_purchases": [5, 10],
        "payment_method": ["Cash", "Card"],
        "frequency_of_purchases": ["Weekly", "Monthly"],
    })
    result = clean_customer_shopping_data(raw)
    assert result["subscription_status"].mean() == 0.5
    assert result["discount_applied"].mean() == 0.5
