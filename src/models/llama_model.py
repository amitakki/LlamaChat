from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import streamlit as st

class LlamaModel:
    def __init__(self, model_config):
        self.config = model_config
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = None
        self.model = None
        
        if not self.config.hf_token:
            raise ValueError(
                "Hugging Face token not found. Please set the HUGGING_FACE_TOKEN environment variable."
            )
        
    def load_model(self):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.config.model_name,
                token=self.config.hf_token
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                self.config.model_name,
                token=self.config.hf_token,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                device_map="auto"
            )
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            st.error("Please check your Hugging Face token and ensure you have access to Llama 2.")
            st.stop()