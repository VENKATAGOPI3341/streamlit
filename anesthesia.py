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

def main():
    st.title("Placement Dashboard for Anesthesia Department")
    
    # Fetch data for placed and unplaced students in the Anesthesia department
    query_ane_placed_unplaced = "SELECT Placed, COUNT(*) AS Count FROM placement_data WHERE Branch = 'ANESTHSIA' GROUP BY Placed"
    ane_placed_unplaced_data = fetch_data(query_ane_placed_unplaced)

    # Create DataFrame for Anesthesia department
    df_ane_placed_unplaced = pd.DataFrame(ane_placed_unplaced_data, columns=['Placed', 'Count'])

    # Visualize the data with a pie chart
    fig_ane_placed_unplaced_pie = px.pie(df_ane_placed_unplaced, values='Count', names='Placed', title='Placement Status for ANESTHESIA Department')
    fig_ane_placed_unplaced_pie.update_traces(marker=dict(colors=['#1f77b4', '#ff7f0e']))
    st.plotly_chart(fig_ane_placed_unplaced_pie)

    # Fetch data for packages offered to Anesthesia department students
    query_ane_packages = "SELECT Package FROM placement_data WHERE Branch = 'ANESTHSIA'"
    ane_packages_data = fetch_data(query_ane_packages)

    # Create DataFrame for Anesthesia department packages
    df_ane_packages = pd.DataFrame(ane_packages_data, columns=['Package'])

    # Visualize the data with a histogram or box plot
    # Here, I'll use a histogram to show the distribution of packages
    fig_ane_packages_hist = px.histogram(df_ane_packages, x='Package', title='Distribution of Packages for ANESTHESIA Department', color_discrete_sequence=['#2ca02c'])
    st.plotly_chart(fig_ane_packages_hist)

    # Query to fetch data for students with backlogs, from Anesthesia department, and with a package
    query = """
            SELECT Name, Branch, Package 
            FROM placement_data 
            WHERE Backlogs > 0 AND Branch = 'ANESTHSIA' AND Package IS NOT NULL
        """
    backlog_ane_package_data = fetch_data(query)

    # Create DataFrame from fetched data
    df_backlog_ane_package = pd.DataFrame(backlog_ane_package_data, columns=['Name', 'Branch', 'Package'])

    # Display DataFrame
    # st.write(df_backlog_ane_package)
    
    # Visualize the data with a scatter plot
    fig_backlog_ane_package = px.scatter(df_backlog_ane_package, x='Name', y='Package', color='Branch',
                                         title='Packages for Anesthesia Department with Backlogs',
                                         labels={'Name': 'Student Name', 'Package': 'Package Amount'},
                                         hover_name='Name')
    fig_backlog_ane_package.update_traces(marker=dict(size=12))
    fig_backlog_ane_package.update_layout(showlegend=True)
    st.plotly_chart(fig_backlog_ane_package)

    # Define the query to fetch data for Domain Count Bar Chart
    query_domain_count = """
        SELECT Domain, COUNT(*) AS Count 
        FROM placement_data 
        WHERE Branch = 'ANESTHSIA' 
        GROUP BY Domain
    """

    # Fetch data for Domain Count Bar Chart
    domain_count_data = fetch_data(query_domain_count)

    # Create DataFrame for Domain Count Bar Chart
    df_domain_count = pd.DataFrame(domain_count_data, columns=['Domain', 'Count'])

    # Visualize the data with a bar chart
    fig_domain_count_bar = px.bar(df_domain_count, x='Domain', y='Count', 
                                  title='Domain-wise Student Count for ANESTHESIA Department',
                                  labels={'Domain': 'Domain', 'Count': 'Student Count'},
                                  color='Domain')
    st.plotly_chart(fig_domain_count_bar)

    # Define the query to fetch data for Package vs. CGPA Scatter Plot
    query_package_cgpa = """
        SELECT CGPA, Package
        FROM placement_data
        WHERE Branch = 'ANESTHSIA' AND Placed = 'Yes' AND CGPA IS NOT NULL AND Package IS NOT NULL
    """

    # Fetch data for Package vs. CGPA Scatter Plot
    package_cgpa_data = fetch_data(query_package_cgpa)

    # Create DataFrame for Package vs. CGPA Scatter Plot
    df_package_cgpa = pd.DataFrame(package_cgpa_data, columns=['CGPA', 'Package'])

    # Visualize the data with a scatter plot
    fig_package_cgpa_scatter = px.scatter(df_package_cgpa, x='CGPA', y='Package', 
                                          title='Package vs. CGPA for Placed Students in Anesthesia Department',
                                          labels={'CGPA': 'CGPA', 'Package': 'Package Amount'},
                                          trendline='ols')
    st.plotly_chart(fig_package_cgpa_scatter)

    # Define the query to fetch data for Company Placement Bar Chart
    query_company_placement = """
        SELECT Company_placed, COUNT(*) AS Placement_Count
        FROM placement_data
        WHERE Branch = 'ANESTHSIA' AND Placed = 'Yes' AND Company_placed IS NOT NULL
        GROUP BY Company_placed
    """
    # Fetch data for Company Placement Bar Chart
    company_placement_data = fetch_data(query_company_placement)
    # Create DataFrame for Company Placement Bar Chart
    df_company_placement = pd.DataFrame(company_placement_data, columns=['Company_placed', 'Placement_Count'])
    # Visualize the data with a horizontal bar chart
    fig_company_placement_bar_horizontal = px.bar(df_company_placement, y='Company_placed', x='Placement_Count', 
                                                   title='Company-wise Placement Count for ANESTHESIA Department',
                                                   labels={'Company_placed': 'Company', 'Placement_Count': 'Placement Count'},
                                                   color='Company_placed',
                                                   orientation='h')
    st.plotly_chart(fig_company_placement_bar_horizontal)


if __name__ == "__main__":
    main()
