import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

def run_ab_test():
    np.random.seed(42)
    n = 5000

    df = pd.DataFrame({
        "group": np.random.choice(["A", "B"], size=n)
    })

    df["converted"] = df["group"].apply(
        lambda x: np.random.binomial(1, 0.12 if x == "A" else 0.15)
    )

    conversions = df.groupby("group")["converted"].sum()
    visitors = df.groupby("group")["converted"].count()

    stat, p_value = proportions_ztest(conversions, visitors)

    return {
        "conversion_A": float(conversions["A"] / visitors["A"]),
        "conversion_B": float(conversions["B"] / visitors["B"]),
        "p_value": float(p_value),
        "decision": "B wins" if p_value < 0.05 else "No difference"
    }
