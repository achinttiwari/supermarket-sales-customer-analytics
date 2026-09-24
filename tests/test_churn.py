import pandas as pd
from src.churn_model import train_churn_model

def test_churn_model_module_remains_reusable():
    rows=[{"Customer_ID":f"C{i}","Recency":20+i*5,"Frequency":10-(i%5),"Monetary":1000-i*20,"Churn_Status":int(i>=10)} for i in range(20)]
    result=train_churn_model(pd.DataFrame(rows))
    assert set(result.metrics)=={"accuracy","precision","recall"}
    assert "Risk_Tier" in result.predictions.columns
