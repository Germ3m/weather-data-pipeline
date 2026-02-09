import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

# --- Configuration ---
DB_CONFIG = {
    "host": "localhost",
    "database": "weather_db",
    "user": "postgres",
    "password": "20021980"
}

# --- Function 1: Get Data (ONLY connects to DB) ---
def get_data():
    """
    Connects to the PostgreSQL database and fetches daily weather data.
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        
        # Query for Daily Data
        query = "SELECT * FROM weather_data ORDER BY date ASC"
        
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return pd.DataFrame()

# --- Function 2: Main App (ONLY handles the UI) ---
def main():
    # 1. Page Config must be the very first Streamlit command
    st.set_page_config(page_title="Weather Pipeline", page_icon="🌦️", layout="wide")
    
    st.title("🌦️ Daily Weather Pipeline")
    st.markdown("Monitoring daily weather summaries extracted from Open-Meteo.")

    # 2. Call Function 1 to get the data
    df = get_data()

    if df.empty:
        st.warning("No data found! Please run `python app.py` to ingest data.")
        return

    # Ensure date column is datetime format for Plotly
    df['date'] = pd.to_datetime(df['date'])

    # 3. Key Metrics (Most Recent Day)
    latest = df.iloc[-1]
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Date", latest['date'].strftime('%Y-%m-%d'))
    with col2:
        st.metric("Max Temp", f"{latest['max_temperature']} °C")
    with col3:
        st.metric("Precipitation", f"{latest['precipitation']} mm")
    with col4:
        st.metric("Max Wind", f"{latest['max_wind_speed']} km/h")

    st.divider()

    # 4. Visualization Section
    
    # Chart 1: Temperature Range (Max & Min)
    st.subheader("Temperature Range (Max vs Min)")
    fig_temp = px.line(df, x='date', y=['max_temperature', 'min_temperature'], 
                       markers=True, title="Daily Temperature Highs & Lows")
    st.plotly_chart(fig_temp, use_container_width=True)

    col_left, col_right = st.columns(2)
    
    # Chart 2: Precipitation
    with col_left:
        st.subheader("Daily Rainfall (mm)")
        fig_rain = px.bar(df, x='date', y='precipitation', 
                          title="Precipitation", color_discrete_sequence=['#00CC96'])
        st.plotly_chart(fig_rain, use_container_width=True)
        
    # Chart 3: Wind Speed
    with col_right:
        st.subheader("Max Wind Speed (km/h)")
        fig_wind = px.line(df, x='date', y='max_wind_speed', 
                           markers=True, title="Wind Gusts", color_discrete_sequence=['#AB63FA'])
        st.plotly_chart(fig_wind, use_container_width=True)

    with st.expander("View Raw Database Records"):
        st.dataframe(df.sort_values(by='date', ascending=False))

    # Refresh Button
    if st.button("Refresh Data"):
        st.rerun()

if __name__ == "__main__":
    main()