 st.subheader("Your Glucose Trend")

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
