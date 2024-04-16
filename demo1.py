import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_excel("final data.xlsx")

# Sidebar
st.sidebar.title("Placement Dashboard")
department = st.sidebar.selectbox("Select Department", sorted(data['Branch'].unique()))
backlog_range = st.sidebar.slider("Select Number of Backlogs Range", 0, 10, (0, 10))

# Filter data based on department and backlog range
filtered_data = data[(data['Branch'] == department) & 
                    (data['Backlogs'].between(backlog_range[0], backlog_range[1]))]

# Main content
st.title("Placement Dashboard")
st.write(f"### {department} Placement Dashboard")

st.write("### Placed vs Unplaced Students")
placement_chart = px.histogram(filtered_data, x='Placed', color='Placed', title="Placed vs Unplaced Students")
st.plotly_chart(placement_chart)

st.write("### GPA Distribution of Placed Students")
placed_gpa_chart = px.histogram(filtered_data[filtered_data['Placed'] == 'Yes'], x='CGPA', 
                                title="GPA Distribution of Placed Students", marginal="box")
st.plotly_chart(placed_gpa_chart)

st.write("### Number of Backlogs of Placed Students")
placed_backlogs_chart = px.histogram(filtered_data[filtered_data['Placed'] == 'Yes'], x='Backlogs', 
                                     title="Number of Backlogs of Placed Students")
st.plotly_chart(placed_backlogs_chart)
