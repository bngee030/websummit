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


csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTmf4TjSXyG3y_GqrAuRTNjg58cT-D2mhOLPoGJSZQj4HL3SmtDgsTDOfU702lcGY79lcZ-dYIPtrwb/pub?gid=0&single=true&output=csv"


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
if st.button("Refresh Data"):
    # Reload the data and set session state to force a rerun
    df = load_data()
    st.session_state.df = df
    st.session_state.data_loaded = False


# Check if 'Name' and 'Age' columns exist, and then create a bar chart
if "Company" in df.columns and "Ubiscore" in df.columns:
    chart = (
        alt.Chart(df)
        .mark_text(
            align="left",
            dx=5,  # Adjust text position to the right of the bar
            fontSize=14,
            color="#fff",
        )
        .mark_bar(color="#1e88e5")
        .configure_axis(
            labelColor="#07e5a6",  # Color for axis labels
            titleColor="#07e5a6",  # Color for axis titles
        )
        .encode(x="Ubiscore", y=alt.Y("Company", sort="-x"), text=alt.Text("value:Q"))
        .properties(height=300)
    )

    # Display the chart in Streamlit, using full container width
    st.altair_chart(chart, use_container_width=True)

    # df['Ubiscore'] = pd.to_numeric(df['Ubiscore'], errors='coerce')

    # # Create the base chart
    # base = alt.Chart(df).transform_fold(
    #     ['Ubiscore'],
    #     as_=['column', 'value']
    # )
    
    # # Create the bars
    # bars = base.mark_bar(color="#1e88e5").encode(
    #     y=alt.Y('Company', sort='-x'),  # Company names on the y-axis
    #     x=alt.X('value:Q'),  # Ubiscore values on the x-axis (the length of the bars)
    #     color=alt.Color('column:N', scale=alt.Scale(range=["#1e88e5"])),  # Color for bars
    #     tooltip=['Company', 'value']
    # )
    
    # # Add text on top of the bars
    # text = base.mark_text(
    #     align='center',
    #     baseline='middle',
    #     color='#07e5a6',
    #     dx=0, dy=-8  # Position text above the bars
    # ).encode(
    #     y=alt.Y('Company', sort='-x'),
    #     x=alt.X('value:Q'),
    #     text=alt.Text('value:Q', format='.0f')  # Display the Ubiscore value
    # )
    
    # # Combine bars and text
    # final_chart = (bars + text).properties(width=500, height=300)

    # # Display the chart in Streamlit, using full container width
    # st.altair_chart(final_chart, use_container_width=True)

else:
    st.error("The CSV file does not contain 'Company' and 'Ubiscore' columns.")
