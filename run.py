from flask import Flask, jsonify, request
from app.translate import Translator
from app.summarize import Summarizer

app = Flask(__name__)
translator = Translator()
summarizer = Summarizer()

@app.route('/functions', methods=['GET'])
def get_functions():
    functions = ['translate_to_english', 'translate_to_chinese', 'summarize_text']
    return jsonify(functions)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data['text']
    function = data['function']
    
    if function == 'translate_to_english':
        result = translator.translate_to_english(text)
    elif function == 'translate_to_chinese':
        result = translator.translate_to_chinese(text)
    else:
        result = "Invalid function"
    
    return jsonify({'result': result})

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.json
    text = data['text']
    summary = summarizer.summarize_text(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
