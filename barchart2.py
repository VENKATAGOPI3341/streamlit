import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read Excel file
def read_excel():
    file_path = "data.xlsx"  # Update with your Excel file name
    df = pd.read_excel(file_path)
    return df

# Function to create stacked bar chart
def plot_stacked_bar_chart(data):
    st.subheader("Stacked Bar Chart: Placed vs Package")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='package', hue='Placed')
    plt.title("Placed vs Package")
    plt.xlabel("Package")
    plt.ylabel("Count")
    plt.xticks(rotation=50)
    st.pyplot()

# Main function
def main():
    st.title("Visualization of Placed vs Package")
    df = read_excel()  # Read the Excel file
    
    # st.write(df.head())  # Displaying the first few rows of the dataframe
    
    plot_stacked_bar_chart(df)  # Plot the stacked bar chart

# Run the app
if __name__ == "__main__":
    main()
