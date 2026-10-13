def source_effectiveness(df, cost_per_source=None):
    cost_per_source = cost_per_source or {
        "LinkedIn": 50000, "Referral": 20000, "HH.ru": 30000,
        "Agency": 200000, "Career Site": 5000, "Telegram": 10000,
    }
    grouped = df.groupby("source").agg(
        candidates=("candidate_id", "count"),
        hires=("final_stage", lambda x: (x == "hired").sum()),
    ).reset_index()
    grouped["cost"] = grouped["source"].map(cost_per_source)
    grouped["cost_per_hire"] = grouped.apply(
        lambda r: r["cost"] / r["hires"] if r["hires"] else 0, axis=1)
    grouped["hire_rate"] = grouped["hires"] / grouped["candidates"]
    return grouped.sort_values("cost_per_hire")
