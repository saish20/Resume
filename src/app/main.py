import streamlit as st
from streamlit_timeline import st_timeline
import pandas as pd

# Set page title
st.set_page_config(layout="wide",page_title='My Resume')

# Set page header and profile picture
# Create sidebar navigation with profile picture
# Define the CSS styling for the circular profile picture
css = """
    <style>
    img {
        border-radius: 50%;
        width: 80%;
        margin: 10% 10%;
    }
    </style>
"""

# Add the circular profile picture to the sidebar
st.sidebar.markdown(css, unsafe_allow_html=True)
st.sidebar.image('src/data/pp.jpg', use_column_width=False, width=100)
st.sidebar.title('Saish Mayekar')
st.sidebar.markdown("saishmayekar51@gmail.com")
st.sidebar.markdown("+44 7585710321")
st.sidebar.markdown("Manchester")

st.sidebar.markdown("[GitHub Repository](https://github.com/saish20)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/saish-mayekar-a9505121/)")

st.sidebar.download_button(
    label="Download Resume",
    data=open('src/data/SaishMayekar_June23.pdf', "rb").read(),
    file_name="SaishMayekar.pdf",
    mime="application/pdf",
)

st.header('About')
st.write("""
Saish is a highly skilled postgraduate with a specialization in Data Science and Machine Learning, focusing on PA's Analytics capability. With a strong background in Engineering and Mathematics, Saish demonstrates proficiency in Python, SQL, and Excel. He possesses a comprehensive understanding of data science techniques and has hands-on experience with visualization tools such as Tableau and Google Looker.

Saish has gained valuable experience in the financial regulation domain, where he successfully developed a quality assurance tool. This involved utilizing various techniques including data extraction, web scraping, and text comparison. Additionally, he undertook the task of enhancing a global market screening tool by transitioning it from Excel to Python and Streamlit. Furthermore, Saish has worked on Azure Data Factory, where he built the client and standard pipeline for two Hospital Trusts, and on Azure Functions, creating a PDF encrypting tool through Microsoft Power Automate. Currently, Saish is engaged in an exciting project involving Generative AI, where he is implementing Natural Language Query (NLQ) techniques.

During his university coursework, Saish showcased his expertise by implementing Active Learning strategies for a Lifelong Learning Machine Translation system. This involved working with the English-German corpus and resulted in significant improvements in the translation system. Furthermore, Saish has built end-to-end machine learning pipelines through various projects, showcasing his ability to deliver comprehensive solutions.
""")

st.header('Education')
text = f"**{'Masters'}**, *{'Data Analytics'}*"
st.markdown(f"{text}, \n The University of Sheffield, 2021")

text = f"**{'Bachelor of Engineering'}**, *{'Electronics & Telecommunications'}*"
st.markdown(f"{text}, \n Mumbai University, 2014")

st.header('Work Experience')

df_exp = pd.read_excel("src/data/Experience.xlsx")
df_exp['Description'] = df_exp['Description'].str.replace('•', '\n•')

# convert the date column to string format with yyyy-mm-dd format
df_exp['Start_Date'] = df_exp['Start_Date'].dt.strftime('%Y-%m-%d')

timeline_data = []
i =0
for index, row in df_exp.iterrows():
    i += 1
    timeline_data.append({
        "id": i, "content": row["Company"], "start": row["Start_Date"]
    })

timeline = st_timeline(timeline_data, groups=[], options={}, height="300px")
if timeline:  
    st.session_state["timeline"]  = timeline
    df_filtered = df_exp[df_exp["Company"] == timeline["content"]]    
    formatted_string = f"**{df_filtered.iloc[0,0]}**, *{df_filtered.iloc[0,1]}*"
    st.header(formatted_string)
    st.subheader("Responsibilities: \n",)
    st.markdown(f"{df_filtered.iloc[0,-1]}")
else:
    st.write('Select an item to view in detail')

st.header('Projects')
st.subheader('[Lyrics Search App](https://github.com/saish20/FindLyrics)')
st.write('A simple Streamlit app that allows users to search for song lyrics using the Genius API.')

st.subheader('[Generative AI demo](https://github.com/saish20/Generative-AI)')
st.write('App demonstrating the use of the GPT-2 language model with Streamlit to generate coherent text based on user input, showcasing the potential of generative AI.')