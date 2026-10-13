from src.data import generate_pipeline
from src.funnel import funnel_counts, conversion_rates

def test_funnel_monotonic():
    df = generate_pipeline(500)
    counts = funnel_counts(df)
    vals = list(counts.values())
    assert all(vals[i] >= vals[i+1] for i in range(len(vals)-1))
