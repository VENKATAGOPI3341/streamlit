import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to read Excel file
def read_excel():
    file_path = "data.xlsx"  # Update with your Excel file name
    df = pd.read_excel(file_path)
    return df

# Main function
def main():
    st.title("Best Visualization for Your Data")
    df = read_excel()  # Read the Excel file
    
    st.write(df.head())  # Displaying the first few rows of the dataframe
    
    # Selecting only numerical columns for heatmap
    numerical_df = df.select_dtypes(include='number')
    
    # Compute the correlation matrix
    corr_matrix = numerical_df.corr()
    
    # Create a heatmap
    st.subheader("Correlation Heatmap")
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    st.pyplot()

# Run the app
if __name__ == "__main__":
    main()
