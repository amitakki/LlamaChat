import streamlit as st
from src.app.config import AppConfig, ModelConfig
from src.app.components.chat import init_chat_state, display_chat_messages, get_user_input
from src.app.components.sidebar import render_sidebar
from src.models.llama_model import LlamaModel
from src.utils.helpers import format_conversation

def main():
    # Initialize configurations
    app_config = AppConfig()
    model_config = ModelConfig()
    
    # Set up page configuration
    st.set_page_config(
        page_title=app_config.title,
        page_icon=app_config.page_icon
    )
    
    # Render sidebar and update model config
    temperature, max_length = render_sidebar()
    model_config.temperature = temperature
    model_config.max_length = max_length
       
    # Check for token before proceeding
    if not model_config.hf_token:
        st.warning("Please provide your Hugging Face token in the .env to access Llama 2.")
        st.stop()
    
    # Initialize chat state
    init_chat_state()
    
    # Display chat title
    st.title(app_config.title)
    
    # Initialize model
    @st.cache_resource
    def get_model(token):
        model_config.hf_token = token
        model = LlamaModel(model_config)
        model.load_model()
        return model
    
    try:
        model = get_model(model_config.hf_token)
    except Exception as e:
        st.error(f"Error initializing model: {str(e)}")
        st.stop()
    
    # Rest of the main function remains the same...
    # Display existing chat messages
    display_chat_messages()
    
    # Handle user input
    if prompt := get_user_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                conversation = format_conversation(st.session_state.messages)
                response = model.generate_response(conversation)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
