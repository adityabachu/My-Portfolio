import streamlit as st 
import streamlit.components.v1 as components
from PIL import Image
import pandas as pd
import webbrowser
from bokeh.models.widgets import Div
import random

def main():
        st.sidebar.title("Navigation")
        page = st.sidebar.selectbox("Go to", ["About", "Certifications", "Projects", "Extra-Curricular Activities", "Contact"])
        
    
        if page == "About":
            show_about_section()
        elif page == "Extra-Curricular Activities":
            show_activities()
        elif page == "Certifications":
            show_certifications_section()
        elif page == "Contact":
            show_contact_section()
        elif page == "Projects":
            show_projects_section()
        with st.sidebar:
            components.html('<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="adityabachu" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/adityabachu?trk=profile-badge"></a></div>', height = 360 )
            st.title("[LeetCode](https://leetcode.com/user6785Rn/)")
            st.title("[GitHub](https://github.com/adityabachu)")
            with open("Portfolio/Aditya Bachu Resume.pdf", "rb") as file:
                 btn = st.download_button(
                    label="Download Resume 📥",
                    data=file,
                    file_name="ADITYA BACHU RESUME.pdf"
        )
    

def show_about_section():
    st.title("About Me")
    st.write("👋 Hello there! 🌟 I'm a passionate tech enthusiast from Anurag University, and I'm thrilled to share my journey with you! 🚀")
    st.write("In 2020, I embarked on my educational journey at Anurag University, specializing in the dynamic field of Artificial Intelligence and Machine Learning. Along this academic path, I actively participated in numerous community events, fostering connections and contributing to the vibrant tech community. 🤝🎓")
    st.write("Joining the Google DSC Core Team'22 was a game-changing experience! 🌐 It allowed me to collaborate with brilliant minds, organize impactful events, and cultivate a thriving tech ecosystem. 🎉")
    st.write("In the coding realm, I take immense pride in conquering 75+ challenges on LeetCode and Geeks for Geeks. 💻 This not only fuels my passion for solving intricate coding problems but also serves as a tangible validation of my skills. 🔥")
    st.write("Artificial Intelligence and Machine Learning are the beating heart of my pursuits. 🧠🤖 Delving into the boundless possibilities of these cutting-edge technologies captivates me endlessly. Whether it's unraveling the intricacies of natural language processing or demystifying the secrets of computer vision, I'm unwaveringly committed to pushing the boundaries of AI and ML. 🌐")
    st.write("So, here's a snapshot of who I am: a Google DSC Core Team'22 member, a dedicated problem solver, a tech enthusiast with an insatiable passion for AI and ML, and an active participant in community events during my academic journey at Anurag University. 🌟✨ I'm thrilled to continue my journey, welcome new challenges with open arms, and leave a lasting impact in the dynamic world of technology! 🚀💡")
        
def show_activities():        
    st.subheader("Google DSC Core Team - Data Analytics Lead")    
    image = Image.open('Portfolio/Images/GDSC (3).jpg')
    st.image(image, width = 200)
    st.write("As a core team member of Google DSC, I played a vital role in organizing and leading various tech-related events, workshops, and sessions for students in collaboration with Google and the local developer community. I contributed to event planning, content creation, and mentoring participants in coding and technology skills. This experience enhanced my leadership, communication, and technical skills, and allowed me to foster a vibrant tech community on campus.")    

    st.subheader('[Website](https://gdsc.community.dev/anurag-university-hyderabad/)')  
    st.subheader('[My Badge ✅](https://developers.google.com/profile/badges/community/dsc/2022/core-member?authuser=2)')  

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

    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


def show_projects_section():
    st.title('Projects')

    st.subheader('Spam Detection')
    st.write("The Spam Detection System project is designed to automatically identify and filter out spam. Using machine learning algorithms and natural language processing techniques, the system analyzes the content and context of the input, determining whether it is legitimate or spam. By accurately categorizing and flagging spam")

    st.subheader("[Show Project](https://colab.research.google.com/drive/1Ut6uHN9oGJudzqqFUyqHsoga7BUp7M7S?usp=sharing)")   

    st.subheader('Tic-Tac-Toe')
    st.write("The Java Tic Tac Toe Game project is a console-based application that allows two players to play the classic Tic Tac Toe game.")
    st.write("Developed in Java, the project features a user-friendly interface for players to take turns and make their moves on the game board.") 
    st.write("The game includes win-detection logic and ensures valid moves, providing an engaging and interactive experience for players.")
    st.write("This project serves as an ideal way to practice Java programming fundamentals while enjoying a timeless game.")

    st.subheader("[Show Project](https://replit.com/@BachuAditya/Tic-Tac-Toe)")

    st.subheader('Covid Data Visualization')

    st.write("The overwhelming amount of data available on Covid-19 and its spread is beyond the ability of humans to absorb. A visualization can make that data more approachable, helping identify patterns and trends in large amounts of information.")

   
    st.subheader("[Show Project](https://github.com/adityabachu/Covid-Data-Visualization-using-R/tree/main/)") 

    st.subheader('Screen Time Analysis')

    st.write('This project is focused on analyzing and visualizing the screen time usage of individuals. The dataset used in this project was sourced from the internet and includes information about the amount of time spent by individuals on screens')
    st.write('The analysis is performed using Python programming language with the help of numpy and pandas libraries for data manipulation and analysis. The plotly library is used for data visualization and creating interactive visualizations that help in understanding the data more effectively.')
    st.write('Furthermore, the project includes an interactive web application created using streamlit library that allows users to explore and interact with the data.')

    st.subheader("[Show Project](https://screen-time-analysis.streamlit.app/)")

def show_certifications_section():
    st.title("Certifications")
    
    certifications = [
        {
            "id": 1,
            "title": "Google Data Analytics Professional Certification",
            "issuer": "Google",
            "link": "https://www.coursera.org/account/accomplishments/professional-cert/XR9BAGR3PREC",
            "image": "Portfolio/Images/google.jpg"
        },
        {
            "id": 2,
            "title": "IBM Data Science Professional Certification",
            "issuer": "IBM",
            "link": "https://www.coursera.org/account/accomplishments/specialization/certificate/49ZMZL9GQ4ZQ",
            "image": "Portfolio/Images/IBM_logo_in.jpg"
        },
        {
            "id": 3,
            "title": "Java Programming",
            "issuer": "Great Learning",
            "link": "https://olympus.mygreatlearning.com/courses/12385/certificate",
            "image": "Portfolio/Images/great_learning.jpeg"
        },
        {
            "id": 4,
            "title": "Natural Language Processing",
            "issuer": "Udemy",
            "link": "https://www.udemy.com/certificate/UC-0fce24d7-5327-497c-b4d5-0c992be16a83/",
            "image": "Portfolio/Images/udemy.jpeg"
        },
        {
            "id": 5,
            "title": "Python Programming With Data Science",
            "issuer": "Udemy",
            "link": "https://www.udemy.com/certificate/UC-11bdda97-d4f6-43c0-9695-7f4331034d06/",
            "image": "Portfolio/Images/udemy.jpeg"
        },
        {
            "id": 6,
            "title": "Become a Data Analyst",
            "issuer": "LinkedIn",
            "link": "https://www.linkedin.com/learning/certificates/c2dbddcd098471c2e3a82425cd0b6c639d84b0406fbce4545d0a226213530401?trk=backfilled_certificate",
            "image": "Portfolio/Images/linkedin.jpeg"
        },
        {
            "id": 7,
            "title": "Master In-Demand Professional Soft Skills",
            "issuer": "LinkedIn",
            "link": "https://www.linkedin.com/learning/certificates/8812255cdb2b50c1c2953c040998575c19cbf27b4bba2107e2bb50c0d14be524?trk=backfilled_certificate",
            "image": "Portfolio/Images/linkedin.jpeg"
        },
        
        

    ]
    for cert in certifications:
        st.subheader(f"**{cert['title']}**")
        st.write(f"Issued by: {cert['issuer']}")
        image = Image.open(cert['image'])
        st.image(image, width = 100)
        st.subheader("[View Certificate](%s)" % cert['link'])
        st.write("-----")


            
        
     
    

if __name__ == '__main__':
    main()
