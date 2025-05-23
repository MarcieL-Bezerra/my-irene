from flask import Flask, render_template, request, jsonify
import open
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pergunta = request.form.get('pergunta')
        return jsonify({'resposta': pergunta})
    return render_template('index.html')

@app.route('/enviar_pergunta', methods=['POST'])
def enviar_pergunta():
    type = " assistente virtual inteligente capaz de fornecer informações precisas e úteis sobre uma ampla gama de tópicos."
    data = request.get_json()
    pergunta = data['pergunta']
    response = open.get_ai_response(pergunta, type )
    return jsonify({'resposta': response})

if __name__ == '__main__':
    app.run(debug=True)