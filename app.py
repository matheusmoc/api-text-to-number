from flask import Flask, request, jsonify

app = Flask(__name__)

def number_to_text(number):
    number_mapping = {
        '0': 'zero',
        '1': 'um',
        '2': 'dois',
        '3': 'três',
        '4': 'quatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'sete',
        '8': 'oito',
        '9': 'nove',
        '10': 'dez',
        '11': 'onze',
        '12': 'doze',
        '13': 'treze',
        '14': 'quatorze',
        '15': 'quinze',
        '16': 'dezesseis',
        '17': 'dezessete',
        '18': 'dezoito',
        '19': 'dezenove',
        '20': 'vinte',
        '30': 'trinta',
        '40': 'quarenta',
        '50': 'cinquenta',
        '60': 'sessenta',
        '70': 'setenta',
        '80': 'oitenta',
        '90': 'noventa',
        '100': 'cem',
        '200': 'duzentos',
        '300': 'trezentos',
        '400': 'quatrocentos',
        '500': 'quinhentos',
        '600': 'seiscentos',
        '700': 'setecentos',
        '800': 'oitocentos',
        '900': 'novecentos'
    }

    if str(number) in number_mapping:
        return number_mapping[str(number)]

    elif 0 < number < 1000:
        units = str(number)
        if len(units) == 2: 
            if units[0] == '1':  # Números de 10 a 19 são especiais
                return number_mapping[units]
            else:
                return number_mapping[units[0] + '0'] + ' e ' + number_mapping[units[1]]
        elif len(units) == 3:  # Números de 100 a 999
            if units[1:] == '00':  # Números como 100, 200, etc.
                return number_mapping[units]
            else:
                if units[1] == '0':  # Números como 101, 202, etc.
                    number_mapping[units[0] + '00'] == 'cento'
                    return number_mapping[units[0] + '00'] + ' e ' + number_to_text(int(units[1:]))
                else:  # Números como 123, 456, etc.
                    return number_mapping[units[0] + '00'] + ' e ' + number_to_text(int(units[1:]))
    else:
        return 'Número fora do intervalo suportado'

@app.route('/', methods=['GET'])
def index():
    mock_data = {
        "instrucoes": "Para usar esta API, faça uma solicitação POST para a rota '/convert' com o número a ser convertido em texto no corpo da solicitação em formato JSON.",
        "exemplo": {
            "numero": 123,
            "texto_esperado": "cento e vinte e três"
        }
    }

    return jsonify(mock_data)

@app.route('/convert', methods=['POST'])
def convert_number_to_text():
    data = request.get_json()
    number = data.get('number', None)
    
    if number is None:
        return jsonify({'error': 'Número não encontrado'}), 404
    
    try:
        number = int(number)
    except ValueError:
        return jsonify({'error': 'Número inválido'}), 400
    
    text = number_to_text(number)
    
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(host='0.0.0.0')