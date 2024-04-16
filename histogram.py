import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to read Excel file
def read_excel():
    file_path = "data.xlsx"  # Update with your Excel file name
    df = pd.read_excel(file_path)
    return df

# Function to create histogram
def plot_histogram(data):
    st.subheader("Histogram: CGPA Distribution")
    plt.figure(figsize=(10, 6))
    sns.histplot(data['CGPA'], kde=False, color='skyblue', bins=20)
    plt.title("CGPA Distribution")
    plt.xlabel("CGPA")
    plt.ylabel("Frequency")
    st.pyplot()

# Function to create KDE plot
def plot_kde_plot(data):
    st.subheader("KDE Plot: CGPA Distribution")
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data['CGPA'], color='orange', fill=True)
    plt.title("CGPA Distribution")
    plt.xlabel("CGPA")
    plt.ylabel("Density")
    st.pyplot()

# Main function
def main():
    st.title("Visualization of CGPA Distribution")
    df = read_excel()  # Read the Excel file
    
    # st.write(df.head())  # Displaying the first few rows of the dataframe
    
    plot_histogram(df)  # Plot the histogram
    plot_kde_plot(df)   # Plot the KDE plot

# Run the app
if __name__ == "__main__":
    main()
