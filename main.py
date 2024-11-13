# streamlit_google_sheet_csv.py

import streamlit as st
import pandas as pd
import altair as alt

# Google Sheets CSV URL (Replace with your own link)

st.markdown(
    """
    <style>
    * {
    color:#07e5a6;
    }

    .streamlit-expanderHeader {
        color: #07e5a6;
    }
    .css-1v3fvcr {
        color: #07e5a6;
    }
    .css-ffhzg2 {
        color: #07e5a6;
    }
    .css-12ft8du {
        color: #07e5a6;
    }
    .css-15yvdyj {
        color: #07e5a6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRZQuJUXz3YsejJJWpuX1JnDd5Em3mHhrClM7R--wcu4JBVNL4DvEEvWsduYVZED6zxi4yxCWIua3nJ/pub?gid=0&single=true&output=csv"


def load_data():
    return pd.read_csv(csv_url)


# Title and refresh button
st.title("Ubiscore Leaderboard")
if "data_loaded" not in st.session_state or st.session_state.data_loaded is False:
    # Load data initially or when refreshed
    df = load_data()
    st.session_state.df = df
    st.session_state.data_loaded = True
else:
    df = st.session_state.df

# Button to refresh data
if st.button("Refresh"):
    # Reload the data and set session state to force a rerun
    df = load_data()
    st.session_state.df = df
    st.session_state.data_loaded = False


# Check if 'Name' and 'Age' columns exist, and then create a bar chart
if 'Company' in df.columns and 'Ubiscore' in df.columns:
    # Ensure 'Ubiscore' is numeric
    df['Ubiscore'] = pd.to_numeric(df['Ubiscore'], errors='coerce')

    df = df.nlargest(10, 'Ubiscore')

    # Create the base chart
    bars = alt.Chart(df).mark_bar(color="#1e88e5").encode(
        y=alt.Y('Company', sort='-x'),  # Company names on the y-axis
        x=alt.X('Ubiscore:Q'),  # Ubiscore values on the x-axis (the length of the bars)
        tooltip=['Company', 'Ubiscore']  # Tooltip displaying Company and Ubiscore
    )

    # Add text on top of the bars
    texts = bars.mark_bar(color="#07e5a6").mark_text(
        align='left',
        baseline='middle',
        dx=3,
        dy=-5  # Nudges text to right so it doesn't appear on top of the bar
    ).encode(
        text='Company:N'  # Display the Ubiscore value
    )

    # Combine bars and text labels
    chart = alt.layer(bars, texts).properties(width=500, height=300)

    # Display the chart in Streamlit, using full container width
    st.altair_chart(chart, use_container_width=True)
else:
    st.error("The CSV file does not have 'Company' and 'Ubiscore' columns.")
