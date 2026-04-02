# -------------------------------
# Import libraries
# -------------------------------
import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

# -------------------------------
# Load Data
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/cleaned_data.csv")
    df['Stop DateTime'] = pd.to_datetime(df['Stop DateTime'])
    return df

df = load_data()

# -------------------------------
# Sidebar Filters (ALL HERE)
# -------------------------------
st.sidebar.header("Filters")

# Date filter
min_date = df['Stop DateTime'].min().date()
max_date = df['Stop DateTime'].max().date()

start_date = st.sidebar.date_input("Start Date", min_date)
end_date = st.sidebar.date_input("End Date", max_date)

# Other filters
category = st.sidebar.multiselect("Violation Category", df['Violation Category'].unique())
vehicle = st.sidebar.multiselect("Vehicle Type", df['VehicleType'].unique())
gender = st.sidebar.multiselect("Gender", df['Gender'].unique())
race = st.sidebar.multiselect("Race", df['Race'].unique())

# 🔥 Location filter (MOVED HERE)
location = st.sidebar.multiselect(
    "Location",
    df['Location'].value_counts().head(50).index
)

# -------------------------------
# Apply Filters (ONE BLOCK ONLY)
# -------------------------------
filtered_df = df[
    (df['Stop DateTime'].dt.date >= start_date) &
    (df['Stop DateTime'].dt.date <= end_date)
]

if category:
    filtered_df = filtered_df[filtered_df['Violation Category'].isin(category)]

if vehicle:
    filtered_df = filtered_df[filtered_df['VehicleType'].isin(vehicle)]

if gender:
    filtered_df = filtered_df[filtered_df['Gender'].isin(gender)]

if race:
    filtered_df = filtered_df[filtered_df['Race'].isin(race)]

if location:
    filtered_df = filtered_df[filtered_df['Location'].isin(location)]

# Safety check
if filtered_df.empty:
    st.warning("No data available for selected filters")
    st.stop()

# -------------------------------
# TITLE
# -------------------------------
st.title("🚦 Traffic Violations Dashboard")

# -------------------------------
# KPI Section
# -------------------------------
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

col1.metric("Total Violations", f"{len(filtered_df):,}")
col2.metric("Total Accidents", f"{int(filtered_df['Accident'].sum()):,}")
col3.metric("Accident Rate (%)", round(filtered_df['Accident'].mean()*100, 2))

col4.metric("High Risk (%)", round((filtered_df['Violation Category']=='High Risk').mean()*100, 2))

top_make = filtered_df['Make'].mode()[0] if not filtered_df['Make'].mode().empty else "N/A"
col5.metric("Top Vehicle", top_make)


# -------------------------------
# Trend Analysis
# -------------------------------
st.subheader("📊 Violations by Hour")

hour_data = filtered_df['Hour'].value_counts().sort_index()
st.bar_chart(hour_data)

# -------------------------------
# Category Distribution
# -------------------------------
st.subheader("⚠️ Violation Category Distribution")

category_data = filtered_df['Violation Category'].value_counts()
st.bar_chart(category_data)

# -------------------------------
# Weekday Analysis
# -------------------------------
st.subheader("📅 Violations by Weekday")

weekday_data = filtered_df['Weekday'].value_counts()
st.bar_chart(weekday_data)

# -------------------------------
# Location Insights
# -------------------------------
st.subheader("📍 Top Locations")

top_locations = filtered_df['Location'].value_counts().head(10)
st.bar_chart(top_locations)

st.info("Peak violations occur during late-night and evening hours, indicating higher risk periods.")

# -------------------------------
# Vehicle Insights
# -------------------------------
st.subheader("🚗 Vehicle Analysis")

top_makes = filtered_df['Make'].value_counts().head(10)
st.bar_chart(top_makes)

vehicle_type = filtered_df['VehicleType'].value_counts()
st.bar_chart(vehicle_type)

# -------------------------------
# Map
# -------------------------------
st.subheader("🗺️ Violation Hotspots")

map_data = filtered_df[['Latitude','Longitude']].dropna()
map_data = map_data.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})

st.map(map_data)

# -------------------------------
# High Risk Locations
# -------------------------------
st.subheader("🚨 High Risk Locations")

high_risk_loc = filtered_df[filtered_df['Violation Category']=='High Risk'] \
    ['Location'].value_counts().head(10)

st.bar_chart(high_risk_loc)

# Added INSIGHTS PANEL
st.subheader("🧠 Key Insights")

st.markdown("""
- 🚨 High-risk violations show significantly higher accident probability  
- 🕒 Peak violations occur during late-night and commute hours  
- 📍 Major violations are concentrated in key arterial corridors  
- 🍺 Alcohol involvement is higher in high-risk categories  
""")


# Added DOWNLOAD BUTTON
st.subheader("⬇️ Download Data")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_traffic_data.csv",
    mime="text/csv"
)

st.divider()

