import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read Excel file
def read_excel():
    file_path = "data.xlsx"  # Update with your Excel file name
    df = pd.read_excel(file_path)
    return df

# Function to create line chart
def line_chart(data, x_column, y_column):
    st.subheader("Line Chart")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=x_column, y=y_column)
    st.pyplot()

# Function to create pie chart
def pie_chart(data, column):
    st.subheader("Pie Chart")
    plt.figure(figsize=(8, 8))
    data[column].value_counts().plot.pie(autopct='%1.1f%%')
    st.pyplot()

# Function to create bar chart
def bar_chart(data, x_column, y_column):
    st.subheader("Bar Chart")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x=x_column, y=y_column)
    st.pyplot()

# Main function
def main():
    st.title("Graphs from Excel Data")
    df = read_excel()  # Read the Excel file
    
    st.write(df.head())  # Displaying the first few rows of the dataframe
    
    x_column = 'company_placed'  # Update x_column to 'company_placed'
    y_column = 'package'         # Update y_column to 'package'
    
    line_chart(df, x_column, y_column)
    pie_chart(df, x_column)  # Using x_column for pie chart
    bar_chart(df, x_column, y_column)

# Run the app
if __name__ == "__main__":
    main()
