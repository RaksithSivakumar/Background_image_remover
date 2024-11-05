import rembg as rb
from PIL import Image
import streamlit as st
from io import BytesIO
import time

# Set page configuration
st.set_page_config(page_title="Background Remover", layout="wide")

# Custom CSS for dark theme and styling
st.markdown(
    """
    <style>
    /* Dark Background with Gradient */
    body {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        font-family: Arial, sans-serif;
    }
    .main {
        background-color: #2b2b2b;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.3);
    }
    
    /* Header Styling */
    h1 {
        background-color: #0093E9;
        background-image: linear-gradient(160deg, #0093E9 0%, #80D0C7 100%);
        font-size: 2.5em;
        text-align: center;
        margin-top: 20px;
    }
    h2 {
        color: #dddddd;
        font-size: 1.5em;
        text-align: center;
        margin-bottom: 10px;
    }

    /* Sidebar Styling */
    .sidebar {
        background-color: #333333;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
    }
    .sidebar-content {
        text-align: center;
        color: #ffffff;
    }
    .sidebar-content a {
        text-decoration: none;
        color: #4a90e2;
        font-weight: bold;
    }
    
    /* Image Columns Styling */
    .stImage {
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.4);
    }

    /* Download Button Styling */
    .stDownloadButton {
        background-color: #4a90e2;
        color: #ffffff;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
    }
    .stDownloadButton:hover {
        background-color: #356bb3;
        color: #ffffff;
    }

    /* Footer Styling */
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
        color: #aaaaaa;
    }
    .footer p {
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("🌌 Background Remover")
st.markdown("<h2>Remove backgrounds from your images effortlessly!</h2>", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
    st.write("### About the Developer")
    st.write("Raksith")
    st.caption("Follow me here ↓")
    st.write("[LinkedIn](https://www.linkedin.com/in/raksith-s-s-2aa49928b/)", unsafe_allow_html=True)
    st.write("[GitHub](https://github.com/RaksithSivakumar)", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# File uploader
img_inp = st.file_uploader("Upload your image here", type=["jpg", "png", "jpeg"], accept_multiple_files=False)

# Function to convert image to downloadable format
def downloadable(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Add a placeholder for the cancel button
cancel_placeholder = st.empty()

# Main content
if img_inp is not None:
    # Show a cancel button
    cancel_button = cancel_placeholder.button("Cancel Upload")
    
    if cancel_button:
        st.warning("Upload canceled.")
        st.stop()
    
    # Show processing message
    with st.spinner("Processing..."):
        image = Image.open(img_inp)
        time.sleep(2)  # Simulate processing time
        fixed = rb.remove(image)
        downloadable_image = downloadable(fixed)
    
    # Clear the cancel button once processing is done
    cancel_placeholder.empty()
    
    # Display results
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("📥 Your Uploaded Image")
        st.image(image, use_column_width=True)
        
    with col2:
        st.header("📤 Background Removed Image")
        st.image(downloadable_image, use_column_width=True)

    st.download_button("⬇️ Download Background Removed Image", downloadable_image, key="download_button", file_name="bgremoved.png")

# Footer section
st.markdown(
    """
    <div class="footer">
        <p>Created by Raksith</p>
    </div>
    """,
    unsafe_allow_html=True,
)
