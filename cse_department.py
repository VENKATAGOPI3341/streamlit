import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

# Function to connect to the database
def connect_to_database():
    endpoint = "localhost"
    username = "root"
    password = ""
    database = "placement"
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

# Streamlit code
def main():
    st.title("Placement Dashboard for Computer Science Students")

    # Write your SQL queries here
    query_gender_distribution = "SELECT Gender, COUNT(*) as num_placements FROM placement_data WHERE Branch='Computer Science' AND Placed='Yes' GROUP BY Gender"
    query_cgpa_distribution = "SELECT CGPA FROM placement_data WHERE Branch='Computer Science' AND Placed='Yes'"
    query_backlogs_analysis = "SELECT Placed, AVG(Backlogs) as avg_backlogs FROM placement_data WHERE Branch='Computer Science' GROUP BY Placed"
    query_package_distribution = "SELECT Package FROM placement_data WHERE Branch='Computer Science' AND Placed='Yes'"

    # Fetch data
    gender_distribution_data = fetch_data(query_gender_distribution)
    cgpa_distribution_data = fetch_data(query_cgpa_distribution)
    backlogs_analysis_data = fetch_data(query_backlogs_analysis)
    package_distribution_data = fetch_data(query_package_distribution)

    # Convert data to DataFrames
    gender_distribution_df = pd.DataFrame(gender_distribution_data, columns=["Gender", "Placements"])
    cgpa_distribution_df = pd.DataFrame(cgpa_distribution_data, columns=["CGPA"])
    backlogs_analysis_df = pd.DataFrame(backlogs_analysis_data, columns=["Placed", "Average_Backlogs"])
    package_distribution_df = pd.DataFrame(package_distribution_data, columns=["Package"])

    # Visualization 1: Gender Distribution - Pie chart
    st.subheader("Gender Distribution of Placements")
    fig1 = px.pie(gender_distribution_df, values='Placements', names='Gender', title='Gender Distribution of Placements')
    st.plotly_chart(fig1)

    # Visualization 2: CGPA Distribution - Histogram
    st.subheader("CGPA Distribution of Placed Students")
    fig2 = px.histogram(cgpa_distribution_df, x='CGPA', title='CGPA Distribution of Placed Students')
    st.plotly_chart(fig2)

    # Visualization 3: Backlogs Analysis - Bar chart
    st.subheader("Backlogs Analysis")
    fig3 = px.bar(backlogs_analysis_df, x='Placed', y='Average_Backlogs', title='Average Backlogs Analysis')
    st.plotly_chart(fig3)

    # Visualization 4: Package Distribution - Box plot
    st.subheader("Package Distribution of Placed Students")
    fig4 = px.box(package_distribution_df, y='Package', title='Package Distribution of Placed Students')
    st.plotly_chart(fig4)


if __name__ == "__main__":
    main()
    

import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

# Function to connect to the database
def connect_to_database():
    endpoint= "localhost" # type: ignore
    username= "root" # type: ignore
    password= "" # type: ignore
    database= "dd_data" # type: ignore
    connection = mysql.connector.connect(
        host=endpoint,
        user=username,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    return connection, cursor

# Function to fetch data from the database
def fetch_data(cursor):
    query = """select year,
        students_percent_with_zero_backlog,
        students_percent_with_1to2_backlog,
        students_percent_with_3to5_backlog, 
        students_percent_with_more_than_5_backlog,
        exam_registered_percent,
        exam_pass_percent,
        students_percent_with_more_than_75_attendance,
        students_percent_with_65_75_attendance,
        students_percent_with_less_than_65_attendance,
        students_percent_meme from soet_data"""
    cursor.execute(query)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=[col[0] for col in cursor.description])
    return df

# Function to plot Backlog Analysis with year filter
def plot_backlog_analysis(data, selected_years):
    filtered_data = data[data['year'].isin(selected_years)]
    backlog_data = filtered_data[['students_percent_with_zero_backlog', 'students_percent_with_1to2_backlog',
                        'students_percent_with_3to5_backlog', 'students_percent_with_more_than_5_backlog']].sum()
    backlog_data.index=["Zero","One-Two","Three-Five","More than Five"]
    ticks = ('0','1-2','3-5','>5')
    fig = px.bar(y=backlog_data.index, x=backlog_data.values, color=backlog_data.index,
                 labels={'x':'Number of Students'},
                 orientation='h',
                 color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c','#d62728']
                )
    fig.update_layout(xaxis=dict(tickfont=dict(size=25)),yaxis=dict(categoryorder='total ascending',title=''),yaxis_showticklabels=False,xaxis_title_font=dict(size=25), legend=dict(font=dict(size=25),x=0.27,y=1.15,orientation='h'),legend_title=None, showlegend=True,height=600,width=800, hoverlabel=dict(font=dict(size=25,color="black")))
    fig.update_layout(dragmode=False, modebar_remove=['lasso', 'pan','zoom','box select'],colorway=['#1f77b4', '#ff7f0e', '#2ca02c','#d62728'])
    fig.update_traces(texttemplate='%{x}', textposition='inside', textfont_size=25)
    return fig

# Function to plot Exam Performance with year filter
def plot_exam_performance(data, selected_years=None):
    # Apply year filter if selected_years is provided
    if selected_years:
        data = data[data['year'].isin(selected_years)]
    
    # Calculate exam failed percentage
    data['exam_failed_percent'] = 100 - data['exam_pass_percent']
    
    # Aggregate data for plotting
    exam_data = data[['exam_failed_percent', 'exam_pass_percent']].sum().reset_index()
    exam_data.columns = ['Type', 'Count']
    exam_data['Type'] = ['Exam Fail', 'Exam Pass']
    
    # Plotting
    fig = px.pie(exam_data, values='Count', names='Type')
    fig.update_traces(textposition='inside', textinfo='percent', textfont_size=25)
    fig.update_layout(height=600,width=800, autosize=True,legend=dict(font=dict(size=25),x=0.75,y=0.50), hoverlabel=dict(font=dict(size=25,color="black")),colorway=['#1f77b4', '#ff7f0e', '#2ca02c'])
    
    return fig

# Function to plot Attendance Distribution with year filter
def plot_attendance_distribution(data, selected_years):
    filtered_data = data[data['year'].isin(selected_years)]
    attendance_data = filtered_data[['students_percent_with_more_than_75_attendance', 
                            'students_percent_with_65_75_attendance', 
                            'students_percent_with_less_than_65_attendance']].sum().reset_index()
    attendance_data.columns = ['Attendance Range', 'Count']
    attendance_data["Attendance Range"] = [">75%" , "65 - 75%" , "< 65%"]
    
    fig = px.pie(attendance_data, values='Count', names='Attendance Range')
    fig.update_traces(textposition='inside', textinfo='percent', textfont_size=25)
    fig.update_layout(height=600,width=800, autosize=True,legend=dict(font=dict(size=25),x=0.75,y=0.50), hoverlabel=dict(font=dict(size=25,color="black")),colorway=['#1f77b4', '#ff7f0e', '#2ca02c'])
    return fig

# Function to plot MEME Students Over Years with year filter
def plot_meme_students_over_years(data, selected_years):
    colors = ['#ff9999', '#ff6666', '#ff3333', '#ff0000']
    gradient_colors = [colors[int(x / len(data))] for x in range(len(data))]
    fig = px.bar(data, x='year', y='students_percent_meme')
    fig.update_traces(marker=dict(color=gradient_colors))
    fig.update_layout(xaxis=dict(tickfont=dict(size=25)),yaxis=dict(tickfont=dict(size=25)),yaxis_showticklabels=False,xaxis_title='Year', yaxis_title=None,xaxis_title_font=dict(size=25), legend=dict(font=dict(size=10)), showlegend=False,height=600,width=800, autosize=True, hoverlabel=dict(font=dict(size=25,color="black")))
    fig.update_traces(texttemplate='%{y}', textposition='inside', textfont_size=25)
    return fig  



def main():
    st.set_page_config(page_title="SOET - Academic Dashboard", page_icon="📊", layout="wide")

    # Add custom CSS for styling
    st.markdown(
        """
        <style>
        .main {
            background-color: #FFA500;
            padding: 1rem;
        }

        .card {
            background-color: white;
            padding: 1rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        [data-testid="stTable"]{
            font-size:30px;
            background-color:white;
        }
        .dashboard-title {
            background-color: #377eb8;
            color: white;
            padding: 1rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: -2rem;
            margin-top:-3rem;
        }

        [data-baseweb="tag"] {
            width:8rem;
            height:4rem;
        } 

        [data-title="Box Select"],[href="https://plotly.com/"],[data-title="Lasso Select"],[data-title="Pan"],[data-title="Zoom"]{
            display:None;
        }

        .st-ar{
            font-size:25px;
        }



        .st-ci{
            width:1.8rem;
            height:1.8rem;
        }

        .st-af{
            font-size:1.8rem;
        }

        [title="open"]{
            width:4rem;
            height:4rem;
            cursor:pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Fetch data from database
    connection, cursor = connect_to_database()
    df = fetch_data(cursor)
    connection.close()

    # Display sections
    st.markdown("<h1 class='dashboard-title' style='text-align:center;'>Academic Dashboard</h1>", unsafe_allow_html=True)

    # Sidebar for filtering
    years_filter = st.multiselect(label="",label_visibility='hidden', options=df["year"].unique(), default=df["year"][-1:])


    # st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h1 class='card' style='text-align:center;'>Backlog Analysis</h1><br>", unsafe_allow_html=True)
        st.plotly_chart(plot_backlog_analysis(df, years_filter), use_container_width=True)

        st.markdown("<h1 class='card' style='text-align:center;'>Attendance Distribution</h1><br>", unsafe_allow_html=True)
        st.plotly_chart(plot_attendance_distribution(df, years_filter), use_container_width=True)

    with col2:
        st.markdown("<h1 class='card' style='text-align:center;'>Exam Performance</h1><br>", unsafe_allow_html=True)
        st.plotly_chart(plot_exam_performance(df, years_filter), use_container_width=True)

        st.markdown("<h1 class='card' style='text-align:center;'>Multitple Entry And Multiple Exit</h1><br>", unsafe_allow_html=True)
        st.plotly_chart(plot_meme_students_over_years(df, years_filter), use_container_width=True)
    st.table(df)
if _name_ == "_main_":
    main()
