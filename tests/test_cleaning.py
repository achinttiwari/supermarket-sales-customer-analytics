import pandas as pd
from src.data_cleaning import clean_customer_shopping_data

def test_clean_customer_shopping_data_derives_fields():
    raw=pd.DataFrame({"customer_id":[1],"age":[25],"gender":[" Female "],"item_purchased":[" Jacket "],"category":[" Outerwear "],"purchase_amount":["₹ 100.50"],"location":[" Delhi "],"size":["M"],"color":["Blue"],"season":["Winter"],"review_rating":[4.2],"subscription_status":[1],"shipping_type":["Express"],"discount_applied":[0],"previous_purchases":[8],"payment_method":["Cash"],"frequency_of_purchases":["Weekly"]})
    result=clean_customer_shopping_data(raw)
    assert len(result)==1
    assert result.loc[0,"gender"]=="Female"
    assert result.loc[0,"purchase_amount"]==100.50
    assert result.loc[0,"purchase_frequency_days"]==7
    assert result.loc[0,"age_group"]=="18-25"
