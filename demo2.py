import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_excel("final data.xlsx")

# Sidebar
st.sidebar.title("Placement Dashboard")
department = st.sidebar.selectbox("Select Department", sorted(data['Branch'].unique()))

# Filter data based on department
filtered_data = data[data['Branch'] == department]

# Main content
st.title("Placement Dashboard")
st.write(f"### {department} Placement Dashboard")

st.write("### Placed vs Unplaced Students")
placement_chart = px.histogram(filtered_data, x='Placed', color='Placed', title="Placed vs Unplaced Students")
st.plotly_chart(placement_chart)

# Calculate the counts of placed and unplaced students
placement_counts = filtered_data['Placed'].value_counts().reset_index()
placement_counts.columns = ['Status', 'Count']

# Plot a pie chart based on placed and unplaced students
fig = px.pie(placement_counts, values='Count', names='Status', title='Placed vs Unplaced Students')
st.plotly_chart(fig)


# Filter the data to include only placed students
placed_data = filtered_data[filtered_data['Placed'] == 'Yes']

# Calculate the counts of male and female students among placed students
gender_counts = placed_data['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']


# Plot a pie chart for placed male and female students
fig = px.pie(gender_counts, values='Count', names='Gender', title='Placed Male vs Female Students')
st.plotly_chart(fig)




st.write("### Number of Backlogs of Placed Students")
placed_backlogs_chart = px.histogram(filtered_data[filtered_data['Placed'] == 'Yes'], x='Backlogs', 
                                     title="Number of Backlogs of Placed Students")
st.plotly_chart(placed_backlogs_chart)

st.write("### Package Distribution by Branch")
package_by_branch_chart = px.box(filtered_data, x='Branch', y='package', title="Package Distribution by Branch")
st.plotly_chart(package_by_branch_chart)


# Calculate the total number of packages for each branch
package_by_branch = filtered_data.groupby('Branch')['package'].sum().reset_index()

# Create a pie chart showing the proportion of packages for each branch
fig = px.pie(package_by_branch, values='package', names='Branch', title='Package Distribution by Branch')
st.plotly_chart(fig)


st.write("### Scatter Plot: GPA vs Package")
# Generate a scatter plot for GPA vs Package
scatter_plot = px.scatter(filtered_data, x='CGPA', y='package', color='Placed', 
                          title="Scatter Plot: GPA vs Package", 
                          labels={'CGPA': 'CGPA', 'package': 'Package (in Lakhs)'})
st.plotly_chart(scatter_plot)

st.write("### Package Distribution by Branch")

package_by_branch_chart = px.box(filtered_data, x='Branch', y='package', title="Package Distribution by Branch")
st.plotly_chart(package_by_branch_chart)


st.write("### Package Distribution by Branch")
# Create a line chart for package distribution by branch
package_distribution_chart = px.line(filtered_data, x='Branch', y='package', 
                                      title="Package Distribution by Branch", 
                                      labels={'package': 'Package (in Lakhs)'})
st.plotly_chart(package_distribution_chart)


st.title("Placement Dashboard")
st.write(f"### {department} Placement Dashboard")

# Create a heatmap for package distribution by branch and CGPA
heatmap_chart = px.density_heatmap(filtered_data, x='CGPA', y='package', 
                                    title="Heatmap: CGPA vs Package", 
                                    labels={'CGPA': 'CGPA', 'package': 'Package (in Lakhs)'})
st.plotly_chart(heatmap_chart)

st.write("### CGPA Distribution (Box Plot)")
cgpa_boxplot = px.box(filtered_data, y='CGPA', title="CGPA Distribution",
                      labels={'CGPA': 'CGPA'})
st.plotly_chart(cgpa_boxplot)


# Define package ranges
package_ranges = [(0, 3), (3, 6), (6, 9), (9, 12)]

# Create a new column in the DataFrame to categorize packages into ranges
filtered_data['Package Range'] = pd.cut(filtered_data['package'], bins=[0, 3, 6, 9, 12], labels=['0-3', '3-6', '6-9', '9-12'])

# Create a box plot for package distribution by branch and package range
package_by_branch_and_range_chart = px.box(filtered_data, x='Branch', y='package', color='Package Range', 
                                            title="Package Distribution by Branch and Range",
                                            labels={'package': 'Package (in Lakhs)', 'Package Range': 'Package Range'})
st.plotly_chart(package_by_branch_and_range_chart)


# Define package ranges
package_ranges = [(0, 3), (3, 6), (6, 9), (9, 12)]

# Create a new column in the DataFrame to categorize packages into ranges
filtered_data['Package Range'] = pd.cut(filtered_data['package'], bins=[0, 3, 6, 9, 12], labels=['0-3', '3-6', '6-9', '9-12'])

# Check if there are any missing values in 'Branch' column
if filtered_data['Branch'].isnull().any():
    st.error("There are missing values in the 'Branch' column.")
else:
    # Create a box plot for package distribution by branch and package range
    package_by_branch_and_range_chart = px.box(filtered_data, x='Branch', y='package', color='Package Range', 
                                                title="Package Distribution by Branch and Range",
                                                labels={'package': 'Package (in Lakhs)', 'Package Range': 'Package Range'})
    st.plotly_chart(package_by_branch_and_range_chart)
