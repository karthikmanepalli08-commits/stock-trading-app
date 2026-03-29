import pandas as pd

def analyze_fund(data):
    returns = data['Close'].pct_change().mean() * 252
    risk = data['Close'].pct_change().std() * (252**0.5)

    if returns > 0.15:
        rating = "High Growth 🚀"
    elif returns > 0.08:
        rating = "Moderate 👍"
    else:
        rating = "Low ⚠️"

    return returns, risk, rating
