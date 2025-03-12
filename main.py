import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Title and description
st.title("🤖 Itzhb-GEMINI")
st.markdown("🚀 Generate LinkedIn posts on Generative AI like [ITZHB](https://www.github.com/haidarabbasbalospura/)") 
st.markdown("❤️ Powered by Gemini-1.5-flash fine-tuned model.")

# Text input for topic
topic = st.text_input("Please enter the topic")

st.code("""
            Try:
            Explain Transformers Architecture
            How does RAG work?
            """, language= None)


genai.configure()

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}




# Initialize the models
base_model = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash")
ft_model = genai.GenerativeModel(
  model_name="tunedModels/linkedin-post-generator-m6wv3amfoj0l",
  generation_config=generation_config,
)


def generate_linkedin_post(prompt, base_model=base_model, ft_model=ft_model):
    response1 = base_model.invoke(prompt)
    response2 = ft_model.generate_content(prompt)
    
    # Method 1: Manual traversal (verbose)
    manual_way = response2.candidates[0].content.parts[0].text
    
    # Method 2: Using built-in property (clean)
    automatic_way = response2.text  # Does the same traversal internally
    
    return response1.content, automatic_way

if st.button("Generate Posts"):
    if topic:
        with st.spinner("Generating posts..."):
            base_response, ft_response = generate_linkedin_post(f"Generate a LinkedIn post about {topic}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Base Model (gemini-2.0-flash) 🔗")
            st.markdown(f'<div class="output-text">{base_response}</div>', unsafe_allow_html=True)
        
        with col2:
            st.subheader("Itzhb-GEMINI (Fine-tuned Model)")
            st.markdown(f'<div class="output-text">{ft_response}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a topic before generating posts.")

