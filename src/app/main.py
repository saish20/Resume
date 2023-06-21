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
    data=open('src/data/SaishMayekar_Nov22.pdf', "rb").read(),
    file_name="SaishMayekar.pdf",
    mime="application/pdf",
)

st.header('About')
st.write('Saish is a Consulting Analyst at PA Consulting working in a Data Scientist capacity. He has over 6 years of experience as a software developer and has an MSc in Data Analytics from the University of Sheffield. With his background in engineering, coupled with his advanced data science education and experience, he is able to approach complex data problems with both a technical and analytical mindset. He is am passionate about using data to drive business decisions and improve processes, and is always looking for new challenges and opportunities to grow my skills.')

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


st.header('Education')
text = f"**{'Masters'}**, *{'Data Analytics'}*"
st.markdown(f"{text}, \n The University of Sheffield, 2021")

text = f"**{'Bachelor of Engineering'}**, *{'Electronics & Telecommunications'}*"
st.markdown(f"{text}, \n Mumbai University, 2014")



st.header('Projects')
st.subheader('[Lyrics Search App](https://github.com/saish20/FindLyrics)')
st.write('A simple Streamlit app that allows users to search for song lyrics using the Genius API.')

st.subheader('[Generative AI demo](https://github.com/saish20/Generative-AI)')
st.write('App demonstrating the use of the GPT-2 language model with Streamlit to generate coherent text based on user input, showcasing the potential of generative AI.')
