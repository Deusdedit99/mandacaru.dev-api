from flask import Flask, request, jsonify
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

model = joblib.load('https://github.com/Deusdedit99/mandacaru.dev-api/blob/da6293f25686157664b85509d9c5e80a13b34e46/src/modelo_treinado.joblib')
vectorizer = joblib.load('https://github.com/Deusdedit99/mandacaru.dev-api/blob/f53c26c77412dc9be5b78d796670e5fedf1d9866/src/vectorizer.joblib')

app = Flask(__name__)

@app.route('/classificar', methods=['POST'])
def classificar():
    # Obter os dados da requisição
    data = request.get_json()

    # Extrair o texto a ser classificado da requisição
    texto = data['texto']

    # Vetorizar o texto usando o vetorizador treinado
    texto_vetorizado = vectorizer.transform([texto])

    # Fazer a predição usando o modelo treinado
    resultado = model.predict(texto_vetorizado)[0]

    # Retornar o resultado como JSON
    return jsonify({'sentimento': resultado})

if __name__ == '__main__':
    app.run(debug=True)
