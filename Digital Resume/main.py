from pathlib import Path

import streamlit as st
from PIL import Image

# Look into adding other CSS features to change up the resume
# such as changing the color of the text. Possible drop-down
# menu for project showcase and creating another area
# to showcase my art (possibly?)

# Editing on main2.py file with added custom functions

# --- PATH ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.jpg"

# --- GENERAL ---
page_title = "Digital Resume | Eliza Angela Diaz"
page_icon = ":wave:"
name = "Eliza Angela Diaz"
description = """
I am a Quantitative Analyst (Data Scientist) working in model governance for
AI/ML in-house models at Bank of America. At the same time, I am undertaking my
Bachelor's in Computer Science with a focus on Artifical Intelligence at Colorado
State University Global.
"""
email = "elizaangelad@gmail.com"
social_media = {
    "Github": "https://github.com/elizacodes",
    "LinkedIn": "https://www.linkedin.com/in/elizaangelad/"
}

st.set_page_config(page_title=page_title, page_icon=page_icon)
st.title("Hi, I'm Eliza.")

# --- LOAD CSS & PROFILE PIC ---
with open(css_file) as o:
    st.markdown("<style>{}</style>".format(o.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)

# --- SECTION 1 ---
col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(profile_pic, width=260)
    
with col2:
    st.title(name)
    st.write(description)
    st.write(":email:", email)

# --- SOCIAL ---
st.write("#")
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f"{platform} {link}")
    
# --- EDUCATION --- 
st.write("#")
st.markdown("## Education")
st.write("**Harper College**")
st.markdown("""
         - Associate's in Science, Computer Science
         - Associate's in Arts, Computer Science
         """)
