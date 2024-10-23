import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure Streamlit page first
st.set_page_config(page_title="GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

# Configure Google Gemini API
genai.configure(api_key="AIzaSyCdUCdCeqMrj_6mnkz1FQZgg34Cdt4MHbs")

# Function to load Google Gemini API and get response
def get_gemini_response(image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    try:
        response = model.generate_content(['Explain me about this image', image])
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Initialize Streamlit app
st.header("GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

# App description
text = ("Utilizing Gemini Pro AI, this project effortlessly extracts vital information "
        "from diverse multilingual documents, transcending language barriers with precision "
        "and efficiency for enhanced productivity and decision-making.")
styled_text = f"<span style='font-family:serif;'>{text}</span>"

st.markdown(styled_text, unsafe_allow_html=True)

# File uploader to upload an invoice image
uploaded_file = st.file_uploader("Choose an image of the document:", type=["jpg", "jpeg", "png"])

# If the file is uploaded, display the image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Submit button to process the image and extract information
submit = st.button("Tell me about the document")

# If submit button is clicked
if submit and uploaded_file is not None:
    response = get_gemini_response(image)
    st.subheader("The response is:")
    st.write(response)
else:
    st.write("Please upload an image.")