import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

# Set page configuration
st.set_page_config(page_title="Text to PDF Converter", layout="wide")

# Logo
st.image("jb.png", width=250)  # Replace with your logo URL

# Navbar
st.markdown("""
<div class="navbar">
  <a href="#Home">Home</a>
  <a href="#About">About</a>
  <a href="#BackToWebsite">Back To Website</a>
</div>
""", unsafe_allow_html=True)

# Add navigation to different sections
menu = ["Home", "About"]
choice = st.sidebar.selectbox("Navigate", menu)

if choice == "Home":
    # Home Page
    st.title("Text to PDF Converter")
    st.write("Enter your text below to convert it into a PDF document.")

    # Text input
    text_input = st.text_area("Enter text here", height=300)

    if st.button("Convert to PDF"):
        if text_input:
            # Create PDF
            buffer = io.BytesIO()
            c = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter

            # Set font and size
            c.setFont("Helvetica", 12)

            # Split text into lines and add to PDF
            lines = text_input.splitlines()
            y = height - 40
            for line in lines:
                if y < 40:  # Move to the next page if necessary
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y = height - 40
                c.drawString(40, y, line)
                y -= 14

            c.save()
            buffer.seek(0)

            # Download button for the PDF document
            st.download_button(
                label="📥 Download PDF Document",
                data=buffer,
                file_name="converted_text.pdf",
                mime="application/pdf"
            )
        else:
            st.error("Please enter some text before converting to PDF.")

elif choice == "About":
    # About Page
    st.title("About Text to PDF Converter")
    st.write("""
    This tool allows you to convert plain text into a PDF document.

    **Features**:
    - Enter text in a text area.
    - Convert the text into a PDF document.
    - Download the generated PDF.

    **Technology Stack**:
    - Streamlit (for building the web app)
    - ReportLab (for creating PDF documents)
    """)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2024 Text to PDF Converter | TechieHelp</p>
    <a href="https://www.linkedin.com/in/techiehelp" style="color:white; margin-right: 10px;">LinkedIn</a>
    <a href="https://www.twitter.com/techiehelp" style="color:white; margin-right: 10px;">Twitter</a>
    <a href="https://www.instagram.com/techiehelp2" style="color:white;">Instagram</a>
</div>
""", unsafe_allow_html=True)
