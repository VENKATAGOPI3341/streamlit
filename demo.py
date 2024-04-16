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
    
    def fetch_data(cursor):
        query = """select Sl_No,
        REGISTRATION _NUMBER,
        Name,
        Email,
        Gender,
        School,
        Branch,
        CGPA,
        Backlogs,
        Domain,
        Placed,
        Unplaced,
        Company_placed,
        Company_registered,
        Package"""
    cursor.execute(query)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=[col[0] for col in cursor.description])
    return df

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
    st.title("Data Visualization from MySQL Database")

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
    fig1 = px.bar(placed_df, x='Company_placed', y='num_placed', title='Placements by Company')
    st.plotly_chart(fig1)

    # Bar plot for registrations
    fig2 = px.bar(registered_df, x='Company_registered', y='num_registered', title='Registrations by Company')
    st.plotly_chart(fig2)

if __name__ == "__main__":
    main()
