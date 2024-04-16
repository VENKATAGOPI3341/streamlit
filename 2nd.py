import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

# Function to connect to the database
def connect_to_database():
    endpoint = "localhost"
    username = "root"
    password = ""
    database = "placement"
    connection = mysql.connector.connect(
        host=endpoint,
        user=username,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    return connection, cursor

# Fetch data from MySQL database
def fetch_data(query):
    connection, cursor = connect_to_database()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# Streamlit code
def main():
    st.title("overview for placement dashboard")

    # Write your SQL query here
    query = "SELECT Company_placed, COUNT(*) as num_placed FROM placement_data GROUP BY Company_placed"
    query2 = "SELECT Company_registered, COUNT(*) as num_registered FROM placement_data GROUP BY Company_registered"
    
    # Fetch data
    placed_data = fetch_data(query)
    registered_data = fetch_data(query2)

    # Convert data to DataFrames
    placed_df = pd.DataFrame(placed_data, columns=["Company_placed", "num_placed"])  
    registered_df = pd.DataFrame(registered_data, columns=["Company_registered", "num_registered"])

    # Display the DataFrames
    st.write("Placements Data:", placed_df)
    st.write("Registrations Data:", registered_df)

    # Plotting
    st.subheader("Data Visualization")

    # Bar plot for placements
    st.subheader("Placements")
    fig1 = px.bar(placed_df, x='Company_placed', y='num_placed', title='Placements by Company')
    st.plotly_chart(fig1)

    # Pie chart for placements
    st.subheader("Placements Distribution")
    fig3 = px.pie(placed_df, values='num_placed', names='Company_placed', title='Placements Distribution')
    st.plotly_chart(fig3)

    # Bar plot for registrations
    st.subheader("Registrations")
    fig2 = px.bar(registered_df, x='Company_registered', y='num_registered', title='Registrations by Company')
    st.plotly_chart(fig2)

    # Pie chart for registrations
    st.subheader("Registrations Distribution")
    fig4 = px.pie(registered_df, values='num_registered', names='Company_registered', title='Registrations Distribution',
                  color_discrete_sequence=['red', 'yellow'])  # Set colors
    st.plotly_chart(fig4)

    query_placed = "SELECT Gender, COUNT(*) as num_placed FROM placement_data WHERE Placed='Yes' GROUP BY Gender"
    query_all = "SELECT Gender, COUNT(*) as total FROM placement_data GROUP BY Gender"
    
    # Fetch data
    placed_data = fetch_data(query_placed)
    all_data = fetch_data(query_all)

    # Convert data to DataFrames
    placed_df = pd.DataFrame(placed_data, columns=["Gender", "num_placed"])  
    all_df = pd.DataFrame(all_data, columns=["Gender", "total"])

    # Display the DataFrames
    st.write("Placements Data by Gender:", placed_df)
    st.write("Total Students Data by Gender:", all_df)

    # Plotting
    st.subheader("Data Visualization")

    # Pie chart for placements by gender
    st.subheader("Placements by Gender")
    fig1 = px.pie(placed_df, values='num_placed', names='Gender', title='Placements by Gender', color_discrete_sequence=['blue','yellow'])
    st.plotly_chart(fig1)

    # Pie chart for all students by gender
    st.subheader("Total Students by Gender")
    fig2 = px.pie(all_df, values='total', names='Gender', title='Total Students by Gender', color_discrete_sequence=['blue', 'yellow'])
    st.plotly_chart(fig2)

if __name__ == "__main__":
    main()
