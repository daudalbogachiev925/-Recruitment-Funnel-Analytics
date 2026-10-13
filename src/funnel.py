import pandas as pd

STAGES = ["applied", "screening", "interview1", "interview2", "offer", "hired"]

def funnel_counts(df):
    counts = {}
    for i, s in enumerate(STAGES):
        counts[s] = (df["final_stage"].apply(lambda x: STAGES.index(x) >= i)).sum()
    return counts

def conversion_rates(df):
    counts = funnel_counts(df)
    rates = {}
    for i in range(1, len(STAGES)):
        prev = counts[STAGES[i-1]]
        curr = counts[STAGES[i]]
        rates[f"{STAGES[i-1]}→{STAGES[i]}"] = curr / prev if prev else 0
    return rates

def source_breakdown(df):
    return df.groupby("source").agg(
        candidates=("candidate_id", "count"),
        hires=("final_stage", lambda x: (x == "hired").sum()),
        avg_quality=("quality_score", "mean"),
    ).reset_index()
