##Invoice Extractor
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

##cinfiguraing google generative ai
genai.configure(api_key=os.getenv("GOOGLE_APIKEY"))

## functioon to load gemine pro vision model and get respose

def get_gemine_pro_vision_response(input,image,prompt):
    model = genai.Model.get("gemini-pro-vision")
    response = model.generate(
        inputs=[
            genai.Inputs.TextInput(content=input),
            genai.Inputs.ImageInput(content=image, mime_type="image/png"),
            genai.Inputs.TextInput(content=prompt)
        ]
    )
    return response 
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts =[
            {  "mine_type": uploaded_file.type,
            "data": bytes_data
            }
            ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
## initializing streamlit app
import streamlit as st
from PIL import Image

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit=st.button("tell me about the invoice")

input_prompt="""  
you are an expert in understanding invoice.you will recieve input image as invoice and you will have to anser questions based on the input image"""

## if submit is clicked
if submit:
    image_data=input_image_setup(uploaded_file)
    response=vision_response(input_prompt,image_data,input)

    
   
   