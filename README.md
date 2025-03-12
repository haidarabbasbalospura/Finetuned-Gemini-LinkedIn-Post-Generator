# Itzhb-GEMINI: LinkedIn Post Generator

A Streamlit web application that generates professional LinkedIn posts using Google's Gemini AI models. The app uses both the base Gemini model and a fine-tuned model specialized for LinkedIn content generation.

## 🌟 Features

- Generate LinkedIn posts on any topic
- Dual model comparison (base vs fine-tuned)
- User-friendly interface
- Real-time generation
- Optimized for AI/ML content

## 🔧 Prerequisites

- Python 3.8 or higher
- Google AI API key
- Required Python packages

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/haidarabbasbalospura/Finetuned-Gemini-LinkedIn-Post-Generator.git
cd Finetuned-Gemini-LinkedIn-Post-Generator
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google AI API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

## 🚀 Usage

1. Start the Streamlit app:

```bash
streamlit run main.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Enter a topic in the text input field

4. Click "Generate Posts" to create LinkedIn posts

## 🛠️ Configuration

The application uses the following models:

- Base Model: `gemini-2.0-flash`
- Fine-tuned Model: Custom LinkedIn post generator

Generation parameters:

- Temperature: 1.0
- Top-p: 0.95
- Top-k: 40
- Max output tokens: 8192

## 📝 Example Topics

- Explain Transformers Architecture
- How does RAG work?
- Latest AI trends
- Machine Learning basics

## 👥 Contributing

Feel free to open issues and pull requests. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

## 👤 Author

[ITZHB](https://www.github.com/haidarabbasbalospura/)

## 🙏 Acknowledgments

- Google Generative AI
- Streamlit
- LangChain
