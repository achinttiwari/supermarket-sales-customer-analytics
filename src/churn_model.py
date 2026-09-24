"""Leakage-safe Logistic Regression churn modeling."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from .rfm import add_risk_tier


@dataclass
class ChurnResult:
    model: Pipeline
    metrics: dict[str, float]
    predictions: pd.DataFrame


def train_churn_model(rfm_labeled: pd.DataFrame, random_state: int = 42) -> ChurnResult:
    required = {"Recency", "Frequency", "Monetary", "Churn_Status", "Customer_ID"}
    missing = required - set(rfm_labeled.columns)
    if missing:
        raise ValueError(f"Missing churn columns: {', '.join(sorted(missing))}")

    X = rfm_labeled[["Recency", "Frequency", "Monetary"]]
    y = rfm_labeled["Churn_Status"].astype(int)

    if y.nunique() < 2:
        raise ValueError("Churn training requires both churn classes.")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=random_state, stratify=y
    )
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000, random_state=random_state)),
    ])
    model.fit(X_train, y_train)

    probability = model.predict_proba(X_test)[:, 1]
    predicted = (probability >= 0.5).astype(int)
    metrics = {
        "accuracy": float(accuracy_score(y_test, predicted)),
        "precision": float(precision_score(y_test, predicted, zero_division=0)),
        "recall": float(recall_score(y_test, predicted, zero_division=0)),
    }

    predictions = X_test.copy()
    predictions["Customer_ID"] = rfm_labeled.loc[X_test.index, "Customer_ID"]
    predictions["Churn_Probability"] = probability
    predictions["Churn_Prediction"] = predicted
    predictions["Risk_Tier"] = add_risk_tier(predictions["Churn_Probability"])
    return ChurnResult(model=model, metrics=metrics, predictions=predictions)
