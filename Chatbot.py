from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)


class SimpleMultilingualTranslator:
    def __init__(self):
        self.translator = pipeline("translation", model="facebook/m2m100_418M")

        self.language_codes = {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Chinese": "zh",
            "Japanese": "ja",
            "Korean": "ko",
            "Russian": "ru",
            "Arabic": "ar"
        }

    def translate(self, text, source_lang, target_lang):
        src_code = self.language_codes.get(source_lang, source_lang)
        tgt_code = self.language_codes.get(target_lang, target_lang)

        result = self.translator(text, src_lang=src_code, tgt_lang=tgt_code)
        return result[0]['translation_text']


translator = SimpleMultilingualTranslator()

# Simulated customer support responses
support_responses = {
    "greeting": "Hello! How can I help you today?",
    "product": "Our product comes with a 30-day warranty. What specific information do you need?",
    "pricing": "Our pricing starts at $9.99 per month. Would you like to know about our different plans?",
    "contact": "You can reach our support team at support@example.com or call us at 1-800-123-4567.",
    "default": "I'm not sure about that. Could you please rephrase your question?"
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['message']
    user_language = data.get('language', 'English')

    # Simple keyword-based response selection
    response_key = 'default'
    for key in support_responses:
        if key in user_message.lower():
            response_key = key
            break

    response = support_responses[response_key]

    # Translate response if needed
    if user_language != 'English':
        response = translator.translate(response, 'English', user_language)

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)