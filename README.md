# Investment Mentor 🌱

An AI-powered chatbot app built with **Streamlit** that helps users learn about investment concepts interactively. Powered by OpenAI AGENTS SDK (Used for Production) and designed for easy configuration.

## 🚀 Features

- Conversational interface for asking investment questions
- Supports environment variables via `python-dotenv`
- Configurable OpenAI model usage
- Modular — easy to extend logic, prompts, or UI components

## 📦 Requirements

- Python 3.10 – 3.11 (recommended for full compatibility)
- `streamlit`
- `python-dotenv`
- `openai`
- `agents`
- (Optionally) `tensorflow` if using agent-based features

```bash
# Only if you're not using a virtual environment:
pip install -r requirements.txt
````

## 🔧 Quick Start

1. Clone the repo and navigate inside:

   ```bash
   git clone https://github.com/NehaCh11/investment-mentor.git
   cd investment-mentor
   ```

2. Set up a virtual environment (recommended):

   ```bash
   py -3.10 -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Run the app:

   ```bash
   streamlit run app.py
   ```

6. Open `http://localhost:8501` in your browser.

## ⚙️ Usage

* Select your **investment experience level**
* Choose your **preferred explanation style**
* Ask questions via chat — e.g., “What is a mutual fund?”
* The app tailors responses based on your selections

👉 Customize default options in `app.py` if needed.

## 🧩 Extensibility Ideas

* Add more **agent prompts** or custom AI flows in `agents.py`
* Integrate **live market data** via APIs
* Switch to **Docker deployment** for production hosting (Render, Hugging Face Spaces, etc.)

## 🛠 Troubleshooting

* **Dependency issues**: Python 3.12 isn’t supported by TensorFlow. Use Python 3.10 for compatibility.
* **Deployment**: Consider using Docker if you want to stay on Python 3.12.

## 🚧 Next Steps

* Improve UI or add data visualizations
* Add unit tests or CI workflows
* Deploy using Docker to a cloud provider

## 📄 License

This project is licensed under the MIT License — see the included `LICENSE` file.

---

**Feel free to open an issue or submit a pull request!** 😊

