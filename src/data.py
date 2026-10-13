import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_pipeline(n=1500, seed=42):
    np.random.seed(seed)
    sources = ["LinkedIn", "Referral", "HH.ru", "Agency", "Career Site", "Telegram"]
    stages = ["applied", "screening", "interview1", "interview2", "offer", "hired"]

    rows = []
    for i in range(n):
        applied_date = datetime(2024, 1, 1) + timedelta(days=int(np.random.randint(0, 300)))
        source = np.random.choice(sources, p=[0.3, 0.15, 0.25, 0.1, 0.1, 0.1])
        # проходимость по этапам
        pass_rate = {"Referral": 0.75, "LinkedIn": 0.45, "HH.ru": 0.35,
                     "Agency": 0.55, "Career Site": 0.4, "Telegram": 0.5}
        p = pass_rate[source]
        stage = "applied"
        current_date = applied_date
        for s in stages:
            if s == "applied":
                continue
            if np.random.random() < p:
                stage = s
                current_date += timedelta(days=int(np.random.randint(2, 8)))
            else:
                break
        rows.append({
            "candidate_id": f"C{i:05d}",
            "source": source,
            "applied_date": applied_date.date().isoformat(),
            "final_stage": stage,
            "days_to_final": (current_date - applied_date).days,
            "quality_score": round(np.random.normal(3.5, 0.8), 2),
        })
    return pd.DataFrame(rows)
