import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read Excel file
def read_excel():
    file_path = "data.xlsx"  # Update with your Excel file name
    df = pd.read_excel(file_path)
    return df

# Function to create pie chart
def plot_pie_chart(data):
    st.subheader("Pie Chart: Distribution of Placed vs Unplaced Students")
    plt.figure(figsize=(8, 8))
    data['Placed'].value_counts().plot.pie(autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
    plt.title("Distribution of Placed vs Unplaced Students")
    plt.ylabel("")
    st.pyplot()

# Function to create count plot
def plot_count_plot(data):
    st.subheader("Count Plot: Distribution of Placed vs Unplaced Students")
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x='Placed', palette=['lightblue', 'lightcoral'])
    plt.title("Distribution of Placed vs Unplaced Students")
    plt.xlabel("Placement Status")
    plt.ylabel("Count")
    st.pyplot()

# Main function
def main():
    st.title("Visualization of Placed vs Unplaced Students")
    df = read_excel()  # Read the Excel file
    
    # st.write(df.head())  # Displaying the first few rows of the dataframe
    
    plot_pie_chart(df)  # Plot the pie chart
    plot_count_plot(df)  # Plot the count plot

# Run the app
if __name__ == "__main__":
    main()
