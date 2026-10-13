def time_to_hire(df):
    hired = df[df["final_stage"] == "hired"]
    return hired["days_to_final"].mean() if len(hired) else 0

def quality_of_hire(df):
    hired = df[df["final_stage"] == "hired"]
    return hired["quality_score"].mean() if len(hired) else 0

def offer_acceptance_rate(df):
    offers = (df["final_stage"].apply(lambda x: ["applied","screening","interview1","interview2","offer","hired"].index(x) >= 4)).sum()
    hires = (df["final_stage"] == "hired").sum()
    return hires / offers if offers else 0
