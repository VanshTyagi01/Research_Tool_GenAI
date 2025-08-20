# 🚀 Live App

[Try it on Streamlit!](https://papernest.streamlit.app/)

# Research Tool GenAI

A Streamlit-powered app for generating research paper explanations using Google Gemini (via LangChain).

## Features
- Summarize research papers by title
- Choose explanation style: Beginner-Friendly, Technical, Code-Oriented, Mathematical
- Select explanation length: Short, Medium, Long
- Powered by Google Gemini via LangChain

## Setup

1. **Clone the repository:**
	```sh
	git clone https://github.com/VanshTyagi01/Research_Tool_GenAI.git
	cd Research_Tool_GenAI
	```

2. **Install dependencies:**
	```sh
	pip install -r requirements.txt
	```

3. **Configure your API key:**
	- Create a `.env` file in the project root:
	  ```env
	  GOOGLE_API_KEY=your_actual_api_key
	  ```
	- **If deploying on Streamlit Cloud:**
	  - Add your API key in the app's Secrets settings as `GOOGLE_API_KEY`.
	  - Do not commit your `.env` file to the repository.

4. **Run the app locally:**
	```sh
	streamlit run app_ui.py
	```

## Usage
- Enter the title of a research paper.
- Select your preferred explanation style and length.
- Click "Summarize" to get a tailored explanation.

## File Structure
- `app_ui.py` — Main Streamlit app
- `prompt_generator.py` — Prompt generation logic
- `template.json` — Prompt template
- `requirements.txt` — Python dependencies

## Security
- **Never expose your API key in code or public repos.**
- Use environment variables or Streamlit Secrets for deployment.

## License
See `LICENSE` for details.
