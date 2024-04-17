import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector
st.set_page_config(page_title="Home", page_icon="", layout="wide")

# Function to connect to the database
def connect_to_database():
    endpoint = "localhost"  # MySQL server endpoint
    username = "root"       # MySQL username
    password = ""           # MySQL password (leave empty if no password)
    database = "Placement"      # MySQL database name
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
st.sidebar.image("cutm-logo.png",width=100)
st.sidebar.markdown("<p style='text-align: center;'>Placement Dashboard</p>", unsafe_allow_html=True)
st.title("Department Selector")
# Define the list of departments
departments = ["Engineering", "Optometry", "Anesthesia ", "Radiology", "Forensic", "ECE"]
# Add a sidebar
st.sidebar.title("Select Department")
# Add a dropdown in the sidebar for department selection
selected_department = st.sidebar.selectbox("", departments)
# Display the selected department
st.write(f"You selected: {selected_department}")

# Streamlit code
def main():
    st.title("Overview for Placement Dashboard")

    # Write your SQL query here
    query = "SELECT Company_placed, COUNT(*) as num_placed FROM placement_data GROUP BY Company_placed"
    query2 = "SELECT Company_registered, COUNT(*) as num_registered FROM placement_data GROUP BY Company_registered"
    query_placed = "SELECT Gender, COUNT(*) as num_placed FROM placement_data WHERE Placed='Yes' GROUP BY Gender"
    query_all = "SELECT Gender, COUNT(*) as total FROM placement_data GROUP BY Gender"

    # Fetch data
    placed_data = fetch_data(query)
    registered_data = fetch_data(query2)
    placed_data_gender = fetch_data(query_placed)
    all_data_gender = fetch_data(query_all)

    # Convert data to DataFrames
    placed_df = pd.DataFrame(placed_data, columns=["Company_placed", "num_placed"])  
    registered_df = pd.DataFrame(registered_data, columns=["Company_registered", "num_registered"])
    placed_df_gender = pd.DataFrame(placed_data_gender, columns=["Gender", "num_placed"])
    all_df_gender = pd.DataFrame(all_data_gender, columns=["Gender", "total"])

    # Plotting
    #st.subheader("Data Visualization")

    # Arrange plots side by side in five containers
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
         # Bar plot for placements
         st.markdown("## <span style='font-size:18px'></span>", unsafe_allow_html=True)  # Adjust the font size as needed
         fig1 = px.bar(placed_df, x='Company_placed', y='num_placed', title='Placements by Company', width=800)
         fig1.update_layout(height=550)  # Set your desired height
         st.plotly_chart(fig1, use_container_width=True, height=400)



    with col2:
        # Pie chart for placements by gender
        st.markdown("## <span style='font-size:18px'></span>", unsafe_allow_html=True)  # Adjust the font size as needed
        fig2 = px.pie(placed_df_gender, values='num_placed', names='Gender', title='Placements by Gender', color_discrete_sequence=['blue','yellow'], width=800)
        fig2.update_traces(textposition='inside', textinfo='percent+label')
        fig2.update_layout(height=600)  # Set your desired height
        st.plotly_chart(fig2, use_container_width=True, height=600)

    with col3:
        # Pie chart for placements distribution
        st.markdown("## <span style='font-size:18px'></span>", unsafe_allow_html=True)  
        fig3 = px.pie(placed_df, values='num_placed', names='Company_placed', title='Placements Distribution', width=800)
        fig3.update_traces(textposition='inside', textinfo='percent+label')
        fig3.update_layout(height=600)  # Set your desired height
        st.plotly_chart(fig3, use_container_width=True, height=600)



    with col4:
        # Pie chart for registrations distribution
        st.markdown("## <span style='font-size:15px'></span>", unsafe_allow_html=True)
        fig4 = px.pie(registered_df, values='num_registered', names='Company_registered', title='Registrations Distribution',
                      color_discrete_sequence=['red', 'yellow'], width=800)
        fig4.update_traces(textposition='inside', textinfo='percent+label')
        fig4.update_layout(height=600)  # Set your desired height
        st.plotly_chart(fig4, use_container_width=True, height=600)

    
    with col5:
        # Bar plot for registrations
        st.markdown("## <span style='font-size:18px'></span>", unsafe_allow_html=True)
        fig5 = px.bar(registered_df, x='Company_registered', y='num_registered', title='Registrations by Company', width=1200)
        fig5.update_traces(textposition='inside')
        fig5.update_layout(height=600)  # Set your desired height
        st.plotly_chart(fig5, use_container_width=True, height=600)



if __name__ == "__main__":
    main()
