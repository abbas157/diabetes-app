import streamlit as st
import pandas as pd
import plotly.express as px

st.title("ذیابیطس ٹریکر 🩺")
st.subheader("Your Glucose Trend")

# Yeh function data banayega taake graph khali na rahe
def load_data():
    return pd.DataFrame({
        "Date": ["2026-06-20", "2026-06-21", "2026-06-22", "2026-06-23", "2026-06-24"],
        "Glucose_Level": [120, 135, 110, 140, 115],
        "Category": ["Fasting", "Random", "Fasting", "Random", "Fasting"]
    })

df_display = load_data()

if not df_display.empty:
    # Convert date column to datetime for proper sorting
    df_display['Date'] = pd.to_datetime(df_display['Date'])
    df_display = df_display.sort_values('Date')

    # Interactive Graph using Plotly
    fig = px.line(df_display, x="Date", y="Glucose_Level", color="Category",
                  title="Blood Sugar Levels Over Time",
                  markers=True,
                  labels={"Glucose_Level": "Glucose (mg/dL)", "Date": "Date"})

    st.plotly_chart(fig)

    # Show Table
    with st.expander("View History Table"):
        st.dataframe(df_display)
else:
    st.info("Abhi tak koi data enter nahi kiya gaya. Please upar form fill karein.")
