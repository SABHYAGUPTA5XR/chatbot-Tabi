# Tabi Chatbot

Tabi Chatbot is a friendly, modern chatbot built with Flask, HTML, CSS, and JavaScript that leverages the Mistral AI API to generate conversational responses. Tabi is designed to be approachable and efficient, offering concise responses for common phrases such as "Thanks", "Bye", or "Okay" while engaging in more detailed conversations when needed.
![Tabi Chatbot UI](img/screenshot.png)

---
## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Notes](#notes)
- [License](#license)

## Features

- **Modern Chat UI:** A sleek, responsive user interface with HTML, CSS, and JavaScript.
- **Conversational AI:** Powered by Mistral AI using the latest model `"mistral-large-latest"`.
- **Custom Prompting:** Preloaded system messages instruct Tabi on how to provide concise and varied responses to common inputs.
- **API Integration:** Utilizes the Mistral AI API via the [mistralai](https://pypi.org/project/mistralai/) package.
- **Flask Backend:** Simple Flask server to handle API requests and serve the web application.

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- Virtual environment tool (recommended)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SABHYAGUPTA5XR/chatbot-tabi.git
cd chatbot-tabi
```

### 2. Create and Activate a Virtual Environment

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, create one with the following content:

```txt
Flask
mistralai
python-dotenv
```

---

## Configuration

### Mistral API Key:

1. Create a `.env` file in the project root directory.
2. Add your Mistral API key to the file:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

The application will load this variable at startup using `python-dotenv`.

---

## Project Structure

```
tabi-chatbot/
├── app.py              # Main Flask application
├── .env                # Environment variables (contains MISTRAL_API_KEY)
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # HTML file for the chatbot UI
├── static/
│   ├── styles.css      # CSS file for styling the UI
│   └── script.js       # JavaScript file for chatbot functionality
└── img/
    └── ss.png  # Screenshot image of the chatbot UI
```

---

## Usage

### Run the Flask Application:

```bash
python app.py
```

### Access the Chatbot UI:

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

### Interacting with Tabi:

- Type your message in the input field and press **Send**.
- Tabi uses the **Mistral AI API** to generate responses based on your input and preloaded instructions.

---

## Notes

### Cost Management:
- Each API call to Mistral AI will consume your credits.
- Monitor your usage and consider implementing **rate limiting** or **caching** for high-traffic deployments.

### Customization:
- Feel free to modify the **HTML, CSS, or JavaScript** files to enhance Tabi's user interface and behavior.

### Response Handling:
- The system prompt in `app.py` includes **few-shot examples** for common phrases like "Thanks" and "Bye" to ensure concise responses.

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

