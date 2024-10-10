# Multilingual Customer Support Chatbot

A Flask-based customer support chatbot with real-time multilingual translation capabilities using the M2M100 model.

## Features

- Real-time chat interface
- Support for 10 languages:
  - English
  - Spanish
  - French
  - German
  - Italian
  - Chinese
  - Japanese
  - Korean
  - Russian
  - Arabic
- Keyword-based response system
- Modern, responsive UI design
- Real-time translation of responses

## Prerequisites

Before running this project, make sure you have Python 3.7+ installed. You'll also need pip for installing dependencies.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multilingual-support-chatbot.git
cd multilingual-support-chatbot
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install required dependencies:
```bash
pip install flask transformers torch
```

## Project Structure

```
multilingual-support-chatbot/
├── app.py
├── templates/
│   └── index.html
├── README.md
└── requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open a web browser and navigate to `http://localhost:5000`

3. Select your preferred language from the dropdown menu

4. Start chatting! The chatbot will respond to your queries in the selected language

## How It Works

1. **Frontend**: The UI is built using HTML, CSS, and JavaScript (jQuery). It provides a chat interface where users can type messages and see responses.

2. **Backend**: Flask handles the server-side logic, receiving messages and returning appropriate responses.

3. **Translation**: The M2M100 model translates between languages in real-time, allowing for multilingual support.

4. **Response System**: A keyword-based system matches user input to predefined responses. The response is then translated if necessary.

## Customization

### Adding New Responses

To add new responses, modify the `support_responses` dictionary in `app.py`:

```python
support_responses = {
    "greeting": "Hello! How can I help you today?",
    "your_new_key": "Your new response here",
}
```

### Adding New Languages

To add a new language, add it to the `language_codes` dictionary in the `SimpleMultilingualTranslator` class:

```python
self.language_codes = {
    "New Language": "language_code",
}
```

Also, update the language selector in `index.html`:

```html
<select id="language">
    <option value="New Language">New Language</option>
</select>
```

## Limitations

- The translation model is large and may take time to load initially
- Keyword-based response system is simple and may not handle complex queries
- No persistent storage for chat history

## Future Improvements

- Implement more sophisticated natural language processing
- Add database support for chat history and user sessions
- Optimize translation for better performance
- Add user authentication
- Implement typing indicators and read receipts

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Hugging Face for the M2M100 translation model
- Flask team for the excellent web framework

---

For any questions or issues, please open an issue on the GitHub repository.
