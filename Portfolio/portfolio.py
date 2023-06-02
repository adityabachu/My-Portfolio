import streamlit as st

def main():
    st.title("Aditya Bachu")
    
    st.header("About Me")
    st.write("I am a passionate web developer with experience in Python, JavaScript, and HTML/CSS.")
    
    st.header("Skills")
    st.write("Here are some of my key skills:")
    st.markdown("- Web Development (Python, JavaScript, HTML/CSS)")
    st.markdown("- Data Analysis (Python, Pandas, NumPy)")
    st.markdown("- Machine Learning (Scikit-learn, TensorFlow)")
    
    """
    st.header("Projects")
    st.write("Check out some of my projects below:")
    
    st.subheader("Project 1: Website Development")
    st.markdown("- Description: Developed a responsive website using HTML, CSS, and JavaScript.")
    st.markdown("- GitHub Repository: [Link](https://github.com/example/project1)")
    
    st.subheader("Project 2: Data Analysis")
    st.markdown("- Description: Analyzed a dataset using Python and presented findings using visualizations.")
    st.markdown("- GitHub Repository: [Link](https://github.com/example/project2)")
    
    st.subheader("Project 3: Machine Learning")
    st.markdown("- Description: Built a machine learning model for sentiment analysis using Python and Scikit-learn.")
    st.markdown("- GitHub Repository: [Link](https://github.com/example/project3)")
    """

  
    
    st.header("Contact")
    st.write("Feel free to reach out to me:")
    st.markdown(
        """
        <div>
            <a href="mailto:aditya.abhi03@gmail.com" target="_blank">
                <img src="gmail_logo.jpg" alt="Email" style="width: 30px;">
            </a>
            <a href="https://www.linkedin.com/in/adityabachu" target="_blank">
                <img src="linkedin_logo.png" alt="LinkedIn" style="width: 30px;">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    
if __name__ == '__main__':
    main()
