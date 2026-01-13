import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss, brier_score_loss, roc_auc_score

NUM_FEATURES = [
    "down", "ydstogo", "yardline_100", "qtr",
    "time_remaining", "score_diff_home", "is_home_possession"
]

def make_pipeline():
    num = Pipeline([
        ("imp", SimpleImputer(strategy="median")),
        ("sc", StandardScaler())
    ])
    pre = ColumnTransformer([("num", num, NUM_FEATURES)])
    clf = LogisticRegression(max_iter=200)
    return Pipeline([("pre", pre), ("clf", clf)])

def evaluate_binary(y_true, y_prob):
    return {
        "log_loss": log_loss(y_true, y_prob),
        "brier": brier_score_loss(y_true, y_prob),
        "auc": roc_auc_score(y_true, y_prob),
    }
