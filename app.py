import streamlit as st
import pandas as pd
import plotly.express as px
from src.data import generate_pipeline
from src.funnel import funnel_counts, conversion_rates, source_breakdown
from src.sources import source_effectiveness
from src.metrics import time_to_hire, quality_of_hire, offer_acceptance_rate

st.set_page_config(page_title="Recruitment Funnel", layout="wide")
st.title("🎯 Recruitment Funnel Analytics")

@st.cache_data
def load():
    return generate_pipeline()

df = load()

c1, c2, c3 = st.columns(3)
c1.metric("Time to Hire", f"{time_to_hire(df):.1f} дней")
c2.metric("Quality of Hire", f"{quality_of_hire(df):.2f}")
c3.metric("Offer Acceptance", f"{offer_acceptance_rate(df)*100:.1f}%")

st.subheader("Воронка найма")
counts = funnel_counts(df)
st.plotly_chart(px.funnel(y=list(counts.keys()), x=list(counts.values())),
                use_container_width=True)

st.subheader("Конверсии между этапами")
st.json({k: f"{v*100:.1f}%" for k, v in conversion_rates(df).items()})

st.subheader("Эффективность источников")
eff = source_effectiveness(df)
st.dataframe(eff)

st.subheader("Cost per Hire по источникам")
st.plotly_chart(px.bar(eff, x="source", y="cost_per_hire", color="hire_rate"),
                use_container_width=True)
