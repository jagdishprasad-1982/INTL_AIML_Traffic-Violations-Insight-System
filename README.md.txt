> 🚦 Traffic Violations Analytics Dashboard

>> 📌 Project Overview

I am Jagdish Prasad a student of AIML and experienced professional, my batch id # INT-AIML-C-WE-E-B2, this project focuses on analyzing large-scale traffic violation data to uncover patterns related to risk, accidents, and enforcement opportunities.

The goal was not just to clean and explore the data, but to build an end-to-end solution — from raw data processing to an interactive dashboard that enables decision-making.

---

>> 🎯 Objectives

 Clean and preprocess high-volume traffic violation data
 Identify high-risk violation patterns
 Analyze trends across time, location, and demographics
 Build an interactive dashboard for exploration and insights
 Support data-driven decision-making for traffic enforcement

---

>> 🛠️ Tools & Technologies

 Python (Pandas, NumPy)
 Streamlit (Interactive Dashboard)
 VS Code
 Excel / CSV Data Handling

---

>> 🔄 Data Processing & Approach

>>> 1. Data Cleaning & Preparation

 Standardized date and time into a unified datetime format
 Converted Yes/No fields into boolean values
 Handled missing values in search-related columns
 Removed duplicate records using `SeqID + Charge` logic
 Validated geographic coordinates

---

>>> 2. Feature Engineering

 Created Violation Count per stop
 Built Violation Category:

   Single
   Low Multiple
   Medium Multiple
   High Risk
 Derived time-based features:

   Hour
   Weekday
   Month

---

>>> 3. Exploratory Data Analysis

Analysis was performed across multiple dimensions:

 Time Patterns → Hourly and weekday trends
 Location Insights → High-frequency and high-risk hotspots
 Vehicle Analysis → Most common vehicle types and makes
 Risk Analysis → Violation severity vs accident likelihood
 Demographics (descriptive) → Variation across groups

---

>> 📊 Key Insights

 🚨 High-risk violations (multiple offenses) show significantly higher accident probability
 🕒 Violations peak during late-night and commute hours
 📍 Traffic violations are concentrated in specific arterial corridors (hotspots)
 🍺 Alcohol involvement, though low overall, is higher in high-risk cases

---

>> 📈 Dashboard Features

The Streamlit dashboard allows users to:

>>> 🔍 Interactive Filters

 Date range
 Location
 Vehicle type
 Gender
 Race
 Violation category

---

>>> 📊 Visualizations

 Violations by hour and weekday
 Violation category distribution
 Top locations (hotspots)
 Vehicle analysis
 High-risk location analysis

---

>>> 🗺️ Map View

 Geographic visualization of violation hotspots using latitude/longitude

---

>>> 📌 Key Metrics

 Total violations
 Total accidents
 Accident rate (%)
 High-risk percentage
 Most common vehicle

---

>>> ⬇️ Additional Features

 Download filtered dataset
 Insight panel summarizing key findings

---

>> 🧠 Business Value

This project demonstrates how data can be used to:

 Enable targeted enforcement instead of uniform policing
 Identify high-risk zones and time windows
 Support preventive interventions for repeat offenders
 Improve road safety decision-making using data

---

>> 🚀 How to Run

```bash
> Step 1: Run data pipeline
python src/data_cleaning.py

> Step 2: Launch dashboard
streamlit run src/streamlit_app.py
```

---

>> 📌 Final Note

This project reflects a structured, end-to-end approach — from raw data to actionable insights — with a strong focus on real-world applicability and decision support.

Created by Jagdish Prasad, focused on data-driven process improvement and analytics.
