# Import necessary librariries
import streamlit as st
import pandas as pd
import numpy as np
import hydralit_components as hc
import seaborn as sns
import requests
import inspect
from streamlit_lottie import st_lottie
from numerize import numerize
from itertools import chain
import plotly.graph_objects as go
import plotly.express as px
import joblib
import statsmodels.api as sm
import sklearn
from PIL import Image
import matplotlib.pyplot as plt

data_ha = pd.read_csv("data_ha.csv")


# Set Page Icon,Title, and Layout
st.set_page_config(layout="wide",  page_title = "Cardiovascular Disease")

# Load css style file from local disk
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
# Load css style from url
def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">',unsafe_allow_html = True)

# Display lottie animations
def load_lottieurl(url):
    # get the url
    r = requests.get(url)
    # if error 200 raised return Nothing
    if r.status_code !=200:
        return None
    return r.json()

    # Navigation Bar Design
menu_data = [
{'label':"Home", 'icon': "bi bi-house"},
{'label':"EDA", 'icon': "bi bi-clipboard-data"},
{'label':'Analyses', 'icon' : "bi bi-graph-up-arrow"},
{'label':'Conlusion', 'icon' : "fa fa-brain"}]

# # Set the Navigation Bar
# menu_id = hc.nav_bar(menu_definition = menu_data,
#                     sticky_mode = 'sticky',
#                     sticky_nav = False,
#                     hide_streamlit_markers = False,
#                     override_theme = {'txc_inactive': 'white',
#                                         'menu_background' : '#0178e4',
#                                         'txc_active':'#0178e4',
#                                         'option_active':'white'})


over_theme = {'txc_inactive': 'white','menu_background':'#0178e4', 'option_active':'white'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    hide_streamlit_markers=True,
    sticky_nav=True,
    sticky_mode='sticky',
)

# Home Page
if menu_id == "Home":
    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: red;'>Cardiovascular Disease <i class='bi bi-heart-fill' style='color: red;'></i> Visualization</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)
   
# Splitting page into 2 columns
    col1, col2 = st.columns([1,2])
    with col1:
        image = Image.open("pic1.png")
    # Display the image in the dashboard
        st.image(image)

    with col2:
        st.markdown(" ")
        st.markdown(" ")
        
        st.markdown("<h2>Healthcare analytics project</h2>", unsafe_allow_html=True)   
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("<div style='text-align: justify'><h3><b>Cardiovascular disease is a leading cause of death globally, contributing to a significant number of fatalities each year. Early detection, lifestyle modifications, and appropriate medical interventions play a crucial role in preventing or managing cardiovascular disease. Regular exercise, maintaining a healthy diet, managing stress, avoiding tobacco use, and regular medical check-ups are essential for maintaining heart health and reducing the risk of developing cardiovascular disease.</b></h3></div>",
           unsafe_allow_html=True)
    #     st.markdown("""
    # <article>
    # <div class="container">
    #     <div class="column">
    #     </div>
    #     <div class="column">
    #     <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;">
    #         Cardiovascular disease is a leading cause of death globally, contributing to a significant number of fatalities each year.
    #     Early detection, lifestyle modifications, and appropriate medical interventions play a crucial role in preventing or managing cardiovascular disease.
    #       Regular exercise, maintaining a healthy diet, managing stress, avoiding tobacco use, and regular medical check-ups are essential for maintaining heart
    #         health and reducing the risk of developing cardiovascular disease. 
    #     </p>
    #     </div>
    # </div>
    # </article>
    # """, unsafe_allow_html=True)
        
   
  
     # File uploader
    file = st.file_uploader("Upload CSV file", type="csv")
    if file is not None:
    # Read the CSV file
      data_ha = pd.read_csv("C:\\Users\\Acer\\Desktop\\data_ha.csv")
    # Display the DataFrame
      st.dataframe(data_ha.head())
    else: print('Upload your data')
    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)

# EDA page
if menu_id == "EDA":  
  col1, col2, col3 = st.columns([3, 3, 3])
# Assuming you have a variable named 'data_ha' containing your data
  number_of_males = len(data_ha[data_ha["gender"] == "2"])
  number_of_females = len(data_ha[data_ha["gender"] == "1"])
  data_length = len(data_ha) - 1
  with col1:
    theme = {'bgcolor': '#FFFFFF', 'content_color': 'darkred', 'progress_color': 'darkred'}
    hc.info_card(title="Observations: 69,385", bar_value=70000, theme_override=theme)
  with col2:
    hc.info_card(title="Number of Male:  24,272", bar_value="number_of_males", theme_override=theme)            
  with col3:
    hc.info_card(title="Number of Female: 45,113", bar_value=data_length, theme_override=theme)

  
 # Group the data by age bracket and calculate the count of ages for each bracket
    age_counts = data_ha.groupby('age_bracket_number')['age_in_years'].count().reset_index()
    
    # Create a bar chart using Plotly
    fig = px.bar(age_counts, x='age_bracket_number', y='age_in_years')
    
    # Set the labels and title
    fig.update_layout(xaxis_title='Age Bracket', yaxis_title='Count of Ages', title='Count of Ages for Each Age Bracket')
    
    # Rotate the x-axis labels if needed
    fig.update_layout(xaxis_tickangle=-45)
    
    # Display the plot aligned to the left
    col1.plotly_chart(fig, use_container_width=True)

# Add text box to the right
  with col2:
    st.markdown("**Population Distribution:**", unsafe_allow_html=True)
    # Empty row
    st.text(" ")
    st.text(" ")
    st.text("Age 30-34 years: Young Adults (Category 4)")
    st.text("Age 35-39 years: Adults (Category 5)")
    st.text("Age 40-44 years: Adults (Category 6)")
    st.text("Age 45-49 years: Middle-Aged Adults (Category 7)")
    st.text("Age 50-54 years: Middle-Aged Adults (Category 8)")
    st.text("Age 55-59 years: Older Adults (Category 9)")
    st.text("Age 60-64 years: Older Adults (Category 10)")
    st.text("Age 65-69 years: Senior Citizens (Category 11)")


# Add pei chartto the right
  with col3:
    st.markdown("**Percentage of Individuals suffering from Cardiovascular disease:**", unsafe_allow_html=True)
    st.markdown("0: Individuals not suffering from cardiovascular disease")
    st.markdown ("1: Individuals suffering from cardiovascular disease")      
# Calculate the count of individuals with cardio values 0 and 1
    cardio_counts = data_ha['cardio'].value_counts().reset_index()
    cardio_counts.columns = ['Cardio', 'Count']
# Create a pie chart using Plotly
    fig = px.pie(cardio_counts, values='Count', names='Cardio')
# Display the chart using Streamlit
    st.plotly_chart(fig)

  col1, col2 = st.columns([3, 3])
  with col1:
  # Select the columns of interest
    blood_pressure = data_ha[['ap_hi', 'ap_lo']]
  # Create a box plot using Plotly Express
    fig = px.box(blood_pressure, title='Comparison of Systolic and Diastolic Blood Pressure')
  # Set the labels
    fig.update_layout(
      xaxis=dict(title='Blood Pressure'),
      yaxis=dict(title='mmHg'))
  # Display the plot using Streamlit
    st.plotly_chart(fig) 
  with col2:
    # Group data by 'gluc' and 'cardio' columns
    grouped = data_ha.groupby(['gluc', 'cardio']).size().unstack()

    # Create the stacked bar chart using Plotly
    fig = go.Figure()

    # Adjusted 'gluc' category labels
    gluc_labels = ['Normal', 'Above Normal', 'Well Above Normal']

    # Add stacked bar traces for each category of 'gluc'
    for i, category in enumerate(grouped.index):
        fig.add_trace(go.Bar(
            x=['No', 'Yes'],  # Replace 0 with 'No' and 1 with 'Yes'
            y=grouped.loc[category],
            name=f'gluc {gluc_labels[i]}',
            marker_color=f'rgba(31, 119, 180, {(i + 1) / (len(grouped.index) + 1)})',  # Adjust the colors as desired
        ))

    # Customize the chart layout
    fig.update_layout(
        title='Cardiovascular disease Cases by Glucose Category',
        xaxis_title='Cardio',
        yaxis_title='Count',
        barmode='stack'
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)


# Analyses page
if menu_id == "Analyses": 
  st.markdown("  ")
  st.markdown("  ")
  st.markdown("<h2 style='text-align: center;'>Anlaysis with the target variable 'Cardio'<i class='bi bi-heart-fill' style='color: #87CEFA;'</h2>", unsafe_allow_html=True)
# Define the features
  features = ['smoke', 'alco', 'active']
# Create three columns
  col1, col2, col3 =  st.columns([3, 3, 3])

  # Visualize each feature with the target variable
  for idx, feature in enumerate(features):
    # Calculate the count for each category
    counts = data_ha.groupby([feature, 'cardio']).size().unstack(fill_value=0)
    # Create the bar chart using Plotly
    fig = go.Figure()
    for col in counts.columns:
        fig.add_trace(go.Bar(x=['No', 'Yes'], y=counts[col], name=str(col).replace('0', 'No').replace('1', 'Yes')))
    # Update the layout
    fig.update_layout(
        barmode='stack',
        xaxis_title=feature,
        yaxis_title='Count',
        title=f'{feature.capitalize()} vs. Cardiovascular Disease'
    )
    # Display the plot in Streamlit
    if idx % 3 == 0:
        col1.plotly_chart(fig)
    elif idx % 3 == 1:
        col2.plotly_chart(fig)
    else:
        col3.plotly_chart(fig)

  col1, col2 =  st.columns([3,2])
  with col1:
    # Define the features
    features = ['bmi', 'gender']
    # Create a scatter plot
    fig = px.scatter(data_ha, x='bmi', y='gender', color='cardio', title='BMI and Gender Patterns with Cardiovascular Disease')
    # Display the plot in Streamlit
    st.plotly_chart(fig)

  with col2:
    # Create a colormap with two colors for cardio health
    colors = ['rgb(255, 0, 0)', 'rgb(0, 128, 0)']
    # Create the scatter plot using Plotly
    fig = px.scatter(data_ha, x='age_in_years', y='bmi', color='cardio', color_discrete_sequence=colors)

    # Set the labels and title
    fig.update_layout(
        xaxis_title='Age',
        yaxis_title='BMI',
        title='Timeline - BMI, Age, and Cardio Health'
    )
    # Add a colorbar to show the mapping between color and cardio health
    fig.update_layout(coloraxis=dict(colorbar=dict(title='Cardio Health')))

    # Display the plot using Streamlit
    st.plotly_chart(fig)

  with col1:
    # Calculate the mean pulse for each gender, pulse, and cardio combination
    group_means = data_ha.groupby(['gender', 'cardio']).agg({'pulse': 'mean'}).reset_index()
    group_means.rename(columns={'pulse': 'Mean Pulse'}, inplace=True)

    # Map gender values to corresponding labels
    group_means['Gender'] = group_means['gender'].map({1: 'Male', 2: 'Female'})

    # Create a grouped bar chart
    fig = go.Figure(data=[
        go.Bar(name='Male', x=group_means[group_means['Gender'] == 'Male']['cardio'], y=group_means[group_means['Gender'] == 'Male']['Mean Pulse']),
        go.Bar(name='Female', x=group_means[group_means['Gender'] == 'Female']['cardio'], y=group_means[group_means['Gender'] == 'Female']['Mean Pulse'])
    ])

    # Customize the bar chart layout
    fig.update_layout(
        xaxis_title='Cardio',
        yaxis_title='Mean Pulse',
        title='Gender and Cardio Distribution (Mean Pulse)',
        template="plotly_white",
        barmode='group'
    )

    # Display the grouped bar chart
    st.plotly_chart(fig)

  with col2:  
    st.markdown("")
    image = Image.open("C:\\Users\\Acer\\Desktop\\AUB\\Summer 23\\Healthcare\\Individual project\\pic4.png")
    # Display the image in the dashboard
    st.image(image)  
# Conlusion page
if menu_id == "Conlusion": 
    st.markdown(" ")
    st.markdown(" ")   
   # Splitting page into 2 columns
    col1, col2,col3 = st.columns([3,3,3])
    with col1:
      image = Image.open("C:\\Users\\Acer\\Desktop\\AUB\\Summer 23\\Healthcare\\Individual project\\heart.png")
    # Display the image in the dashboard
      st.image(image)   
    with col2:
      st.markdown(" ")
      st.markdown(" ")
      st.markdown(" ")
      st.markdown(" ")
      st.markdown(" ")
      st.markdown(" ")
      st.markdown(" ")
      st.markdown(" ")
      st.markdown(" ")
      st.markdown(" ")
      st.markdown(" ")
      st.markdown(" ")
      st.markdown("<div style='text-align: justify'><h3><b> The findings in the Visualization and results paragraph underscore the importance of lifestyle modifications, including maintaining healthy blood pressure and cholesterol levels, quitting smoking, engaging in regular physical activity, managing weight, and monitoring pulse rates, in reducing the risk of cardiovascular disease. These findings contribute to our understanding of the complex interplay between various factors and cardiovascular health, providing a basis for future research and informing public health interventions aimed at preventing and managing cardiovascular disease.</b></h3></div>",
           unsafe_allow_html=True)
      st.markdown(" ")
      st.markdown(" ")
    with col3:
      image = Image.open("C:\\Users\\Acer\\Desktop\\AUB\\Summer 23\\Healthcare\\Individual project\\pic2.png")
    # Display the image in the dashboard
      st.image(image)   

   
