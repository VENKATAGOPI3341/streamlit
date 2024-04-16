import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read Excel file
def read_excel():
    file_path = "data.xlsx"  # Update with your Excel file name
    df = pd.read_excel(file_path)
    return df

# Function to create bar chart
def bar_chart(data, x_column, y_column):
    st.subheader("Bar Chart")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x=x_column, hue=y_column)
    plt.title("Gender-wise Distribution of Placed Students")
    plt.xlabel("Gender")
    plt.ylabel("Number of Students")
    st.pyplot()

# Main function
def main():
    st.title("Gender-wise Placed Students Visualization")
    df = read_excel()  # Read the Excel file
    
    st.write(df.head())  # Displaying the first few rows of the dataframe
    
    x_column = 'Gender'       # X-axis: Gender
    y_column = 'Placed'       # Y-axis: Placed (binary column indicating placement status)
    
    bar_chart(df, x_column, y_column)  # Plot the bar chart

# Run the app
if __name__ == "__main__":
    main()
