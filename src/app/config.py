from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class ModelConfig:
    model_name: str = "meta-llama/Llama-2-7b-chat-hf"
    max_length: int = 1000
    temperature: float = 0.7
    hf_token: str = os.getenv("HUGGING_FACE_TOKEN")
    
@dataclass
class AppConfig:
    title: str = "Llama Chat Assistant"
    page_icon: str = "🦙"