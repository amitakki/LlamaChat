# 🦙 Llama Chat Application

A scalable and modular chat application built with Streamlit and Hugging Face's Llama 2 model. This application provides an intuitive interface for interacting with the Llama 2 language model, with configurable parameters and a clean, professional UI.

## 🌟 Features

- Clean and intuitive chat interface
- Real-time response generation
- Configurable model parameters
- Persistent chat history
- Support for Hugging Face authentication
- Modular and scalable architecture
- Proper error handling
- Mobile-responsive design

## 🏗️ Project Structure

```
ChatApp/
├── .env
├── requirements.txt
├── run.py
└── src/
    ├── __init__.py
    ├── app/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── main.py
    │   └── components/
    │       ├── __init__.py
    │       ├── chat.py
    │       └── sidebar.py
    ├── models/
    │   ├── __init__.py
    │   └── llama_model.py
    └── utils/
        ├── __init__.py
        └── helpers.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A Hugging Face account with access to Llama 2
- CUDA-capable GPU (optional but recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/amitakki/LlamaChat.git
cd LlamaChat
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Get your Hugging Face token:
   - Go to https://huggingface.co/settings/tokens
   - Create a new token with read access
   - Accept the Llama 2 terms of use at https://huggingface.co/meta-llama/Llama-2-7b-chat-hf

5. Create a `.env` file in the root directory:
```env
HUGGING_FACE_TOKEN=your_token_here
```

### Running the Application

Run the application using Streamlit:
```bash
streamlit run run.py
```

The application will be available at `http://localhost:8501`

## 🎮 Usage

1. The chat interface will appear once you start the application
2. If you haven't set the Hugging Face token in `.env`, you can enter it in the sidebar
3. Adjust model parameters in the sidebar:
   - Temperature (controls response randomness)
   - Max Length (controls response length)
4. Type your message in the chat input and press Enter
5. The model will generate a response, which will appear in the chat

## ⚙️ Configuration

You can modify the default configuration in `src/app/config.py`:

```python
@dataclass
class ModelConfig:
    model_name: str = "meta-llama/Llama-2-7b-chat-hf"
    max_length: int = 1000
    temperature: float = 0.7
```

## 🛠️ Customization

The modular structure allows for easy customization:

1. Add new UI components in `src/app/components/`
2. Modify the model configuration in `src/app/config.py`
3. Add new helper functions in `src/utils/helpers.py`
4. Extend the model functionality in `src/models/llama_model.py`

## 📈 Roadmap

- [ ] Add support for conversation history persistence
- [ ] Implement user authentication
- [ ] Add support for multiple language models
- [ ] Enhance error handling and recovery
- [ ] Add unit tests and integration tests
- [ ] Implement conversation export functionality
- [ ] Add support for system prompts

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing access to Llama 2
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Meta AI](https://ai.meta.com/) for developing Llama 2

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
Made with ❤️ and 🦙
