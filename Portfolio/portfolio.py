import streamlit as st 
import streamlit.components.v1 as components
from PIL import Image
import pandas as pd
import webbrowser
from bokeh.models.widgets import Div
import random

def main():
        st.sidebar.title("Navigation")
        page = st.sidebar.selectbox("Go to", ["About", "Work Experience", "Certifications", "Projects", "Contact"])
        
    
        if page == "About":
            show_about_section()
        elif page == "Work Experience":
            show_work_experience()
        elif page == "Certifications":
            show_certifications_section()
        elif page == "Contact":
            show_contact_section()
        elif page == "Projects":
            show_projects_section()
        with st.sidebar:
            components.html('<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="adityabachu" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/adityabachu?trk=profile-badge"></a></div>', height = 360 )
            if st.button("Github 👨‍💻"):
                js = "window.open('https://github.com/adityabachu')"
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)  
            with open("C:/Users/varun/OneDrive/Desktop/Resume/Aditya Bachu Resume.pdf", "rb") as file:
                 btn = st.download_button(
                    label="Download Resume 📥",
                    data=file,
                    file_name="ADITYA BACHU RESUME.pdf"
        )
    

def show_about_section():
    st.title("About Me")
    st.write("👋 Hey there! I'm a passionate tech enthusiast from Anurag University, and I can't wait to share my journey with you! 🚀")
    st.write("As a GSSoC Contributor'23, I had the incredible opportunity to work on exciting projects and contribute to the tech community. 🌟 Being a part of the Google DSC Core Team'22 was an absolute game-changer for me. It allowed me to collaborate with brilliant minds, organize impactful events, and foster a vibrant tech ecosystem. 🎉")
    st.write("When it comes to coding, I take immense pride in being recognized as a 5 ⭐ Coder at HackerRank. 💻 Solving challenging coding problems has always been my passion, and this achievement truly validates my skills. 🔥")
    st.write("But what truly sets my heart on fire is Artificial Intelligence and Machine Learning. 🧠🤖 Exploring the endless possibilities of these cutting-edge technologies fascinates me beyond words. From diving into natural language processing to unraveling the mysteries of computer vision, I'm constantly driven to push the boundaries of AI and ML. 🌐")
    st.write("So, that's a glimpse of who I am—a GSSoC Contributor'23, Google DSC Core Team'22 member, 5 ⭐ Coder at HackerRank, and a tech enthusiast with an insatiable passion for Artificial Intelligence and Machine Learning. 🌟✨ I'm excited to continue my journey, embrace new challenges, and make a lasting impact in the world of technology! 🚀💡")
def show_work_experience():
    image = Image.open('Portfolio/Images/GDSC (3).jpg')
    st.image(image, caption='Image Caption', use_column_width=True)
    

def show_contact_section():
    st.header("Contact")
    st.write("Feel free to reach out to me:")
    
    st.markdown(
        """
        <div>
            <a href="mailto:aditya.abhi03@gmail.com" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg" alt="Gmail" width="32" height="32">Gmail
            </a>
            
        </div>
        <div>
        <a href="https://www.linkedin.com/in/adityabachu" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="32" height="32">LinkedIn
            </a>
        </div>
        
        """,
        unsafe_allow_html=True
    )

def show_projects_section():
    st.title('Projects')
    st.subheader('Covid Data Visualization')

    st.write('This project is focused on analyzing and visualizing the screen time usage of individuals. The dataset used in this project was sourced from the internet and includes information about the amount of time spent by individuals on screens')
    st.write('The analysis is performed using Python programming language with the help of numpy and pandas libraries for data manipulation and analysis. The plotly library is used for data visualization and creating interactive visualizations that help in understanding the data more effectively.')
    st.write('Furthermore, the project includes an interactive web application created using streamlit library that allows users to explore and interact with the data.')

    if st.button('Show Project', key = 54):
      js = "window.open('https://github.com/adityabachu/Covid-Data-Visualization-using-R/tree/main/')"  
      html = '<img src onerror="{}">'.format(js)
      div = Div(text=html)
      st.bokeh_chart(div) 

    st.subheader('Screen Time Analysis')

    st.write('This project is focused on analyzing and visualizing the screen time usage of individuals. The dataset used in this project was sourced from the internet and includes information about the amount of time spent by individuals on screens')
    st.write('The analysis is performed using Python programming language with the help of numpy and pandas libraries for data manipulation and analysis. The plotly library is used for data visualization and creating interactive visualizations that help in understanding the data more effectively.')
    st.write('Furthermore, the project includes an interactive web application created using streamlit library that allows users to explore and interact with the data.')

    if st.button('Show Project', key = 55):
      js = "window.open('https://screen-time-analysis.streamlit.app/')"  # New tab or window
      html = '<img src onerror="{}">'.format(js)
      div = Div(text=html)
      st.bokeh_chart(div) 

def show_certifications_section():
    st.title("Certifications")
    
    certifications = [
        {
            "id": 1,
            "title": "Google Data Analytics Professional Certification",
            "issuer": "Google",
            "link": "https://www.coursera.org/account/accomplishments/professional-cert/XR9BAGR3PREC",
            "image": "C:/Users/varun/OneDrive/Desktop/google.jpg"
        },
        {
            "id": 2,
            "title": "IBM Data Science Professional Certification",
            "issuer": "IBM",
            "link": "https://www.coursera.org/account/accomplishments/specialization/certificate/49ZMZL9GQ4ZQ",
            "image": "Images/IBM_logo_in.jpg"
        },
        {
            "id": 3,
            "title": "Java Programming",
            "issuer": "Great Learning",
            "link": "https://olympus.mygreatlearning.com/courses/12385/certificate",
            "image": "C:/Users/varun/OneDrive/Desktop/Portfolio/Images/great_learning.jpeg"
        },
        {
            "id": 4,
            "title": "Natural Language Processing",
            "issuer": "Udemy",
            "link": "https://www.udemy.com/certificate/UC-0fce24d7-5327-497c-b4d5-0c992be16a83/",
            "image": "C:/Users/varun/OneDrive/Desktop/Portfolio/Images/udemy.jpeg"
        },
        {
            "id": 5,
            "title": "Python Programming With Data Science",
            "issuer": "Udemy",
            "link": "https://www.udemy.com/certificate/UC-11bdda97-d4f6-43c0-9695-7f4331034d06/",
            "image": "C:/Users/varun/OneDrive/Desktop/Portfolio/Images/udemy.jpeg"
        },
        {
            "id": 6,
            "title": "Become a Data Analyst",
            "issuer": "LinkedIn",
            "link": "https://www.linkedin.com/learning/certificates/c2dbddcd098471c2e3a82425cd0b6c639d84b0406fbce4545d0a226213530401?trk=backfilled_certificate",
            "image": "C:/Users/varun/OneDrive/Desktop/Portfolio/Images/linkedin.jpeg"
        },
        {
            "id": 7,
            "title": "Master In-Demand Professional Soft Skills",
            "issuer": "LinkedIn",
            "link": "https://www.linkedin.com/learning/certificates/8812255cdb2b50c1c2953c040998575c19cbf27b4bba2107e2bb50c0d14be524?trk=backfilled_certificate",
            "image": "C:/Users/varun/OneDrive/Desktop/Portfolio/Images/linkedin.jpeg"
        },
        
        

    ]
    for cert in certifications:
        st.subheader(f"**{cert['title']}**")
        st.write(f"Issued by: {cert['issuer']}")
        image = Image.open(cert['image'])
        st.image(image, width = 100)

        if st.button('Show Certification', key = [cert['id']]):
          js = "window.open(link)"  
          html = '<img src onerror="{}">'.format(js)
          div = Div(text=html)
          st.bokeh_chart(div)
        st.write("----")
            
        
     
    

if __name__ == '__main__':
    main()