import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to read Excel file
def read_excel():
    file_path = "data.xlsx"  # Update with your Excel file name
    df = pd.read_excel(file_path)
    return df

# Function to create count plot
def plot_count_plot(data):
    st.subheader("Count Plot: Domain by Gender")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Domain', hue='Gender')
    plt.title("Domain by Gender")
    plt.xlabel("Domain")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot()

# Main function
def main():
    st.title("Domain by Gender Visualization")
    df = read_excel()  # Read the Excel file
    
    # st.write(df.head())  # Displaying the first few rows of the dataframe
    
    plot_count_plot(df)  # Plot the count plot

# Run the app
if __name__ == "__main__":
    main()
