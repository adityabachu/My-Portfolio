import streamlit as st
import streamlit.components.v1 as components
from bokeh.models.widgets import Div

def main():
        st.sidebar.title("Navigation")
        page = st.sidebar.selectbox("Go to", ["About", "Skills", "Contact"])
        
    
        if page == "About":
            show_about_section()
        elif page == "Skills":
            show_skills_section()
        elif page == "Contact":
            show_contact_section()
        with st.sidebar:
            components.html('<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="adityabachu" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/adityabachu?trk=profile-badge"></a></div>', height = 360 )
            if st.button("Github 👨‍💻"):
                js = "window.open('https://github.com/adityabachu')"  # New tab or window
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)  
            with open("Portfolio/Aditya Bachu Resume.pdf", "rb") as file:
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

def show_skills_section():
    st.title("Skills")
    

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

if __name__ == '__main__':
    main()
