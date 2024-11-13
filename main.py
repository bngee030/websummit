# streamlit_google_sheet_csv.py

import streamlit as st
import pandas as pd
import altair as alt

# Google Sheets CSV URL (Replace with your own link)

csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTmf4TjSXyG3y_GqrAuRTNjg58cT-D2mhOLPoGJSZQj4HL3SmtDgsTDOfU702lcGY79lcZ-dYIPtrwb/pub?gid=0&single=true&output=csv"

def load_data():
    return pd.read_csv(csv_url)

# Title and refresh button
st.title("Horizontal Bar Graph of Names and Ages from Google Sheets")
# if 'data_loaded' not in st.session_state or st.session_state.data_loaded is False:
#     # Load data initially or when refreshed
#     df = load_data()
#     st.session_state.df = df
#     st.session_state.data_loaded = True
# else:
#     df = st.session_state.df

# # Button to refresh data
# if st.button("Refresh Data"):
#     # Reload the data and set session state to force a rerun
#     df = load_data()
#     st.session_state.df = df
#     st.session_state.data_loaded = False

# st.write("Data:", df)


# Check if 'Name' and 'Age' columns exist, and then create a bar chart
# if 'Company' in df.columns and 'Ubiscore' in df.columns:
#     chart = alt.Chart(df).mark_bar().encode(
#         x='Ubiscore',
#         y=alt.Y('Company', sort='-x')
#     ).properties(
#         height=300
#     )

#     # Display the chart in Streamlit, using full container width
#     st.altair_chart(chart, use_container_width=True)
# else:
#     st.error("The CSV file does not contain 'Company' and 'Ubiscore' columns.")