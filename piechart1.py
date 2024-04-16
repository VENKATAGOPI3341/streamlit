import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to read Excel file
def read_excel():
    file_path = "data.xlsx"  # Update with your Excel file name
    df = pd.read_excel(file_path)
    return df

# Function to create pie chart
def pie_chart(data, column):
    st.subheader("Pie Chart")
    plt.figure(figsize=(8, 8))
    data[column].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title(f"Distribution of {column}")
    plt.ylabel("")
    st.pyplot()

# Main function
def main():
    st.title("Pie Chart from Excel Data")
    df = read_excel()  # Read the Excel file
    
    st.write(df.head())  # Displaying the first few rows of the dataframe
    
    column_to_plot = 'Gender'  # Specify the column for pie chart
    
    pie_chart(df, column_to_plot)  # Plot the pie chart based on the specified column

# Run the app
if __name__ == "__main__":
    main()
