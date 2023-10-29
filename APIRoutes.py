from flask import Flask, request, jsonify
from Infraestructure.APIManager import APIManager
from Infraestructure.APIValidator import APIValidator
import binascii

app = Flask(__name__)


@app.route('/ProcessaCalagem', methods=['POST'])
def processa_calagem():
    try:
        data = request.get_json()
        validador = APIValidator()
        entrada, mensagem = validador.valida_chamada_calagem(data)

        if mensagem == 'OK':
            manager = APIManager()
            tonelada_calc, forma = manager.processa_calagem(entrada)

            if tonelada_calc == -1:
                return jsonify({'status': 'success', 'message': 'Não é preciso aplicar Calcário.'})

            return jsonify({'status': 'success', 'message':
                            f'É preciso adicionar {tonelada_calc} toneladas de Calcário por hectare de forma {forma}.'})
        else:
            return jsonify({'status': 'error', 'message': entrada})

    except Exception as e:
        print(f'Erro: {str(e)}')
        print('Traceback:')
        import traceback
        traceback.print_exc()
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/ProcessaAdubacao', methods=['POST'])
def processa_adubacao():
    try:
        data = request.get_json()
        validador = APIValidator()
        entrada, mensagem = validador.valida_chamada_adubacao(data)

        if mensagem == 'OK':
            manager = APIManager()
            message_N, message_P, message_K = manager.processa_adubacao(entrada)

            return jsonify({'status': 'success', 'message': {'N': message_N, 'P': message_P, 'K': message_K}})

        else:
            return jsonify({'status': 'error', 'message': entrada})

    except Exception as e:
        print(f'Erro: {str(e)}')
        print('Traceback:')
        import traceback
        traceback.print_exc()
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/', methods=['GET'])
def process_server_default_message():
    if request.method == 'GET':
        return jsonify({'api_message': 'Bem-Vindo a API de análise de Calagem e Adubação',
                        'api_status': 'online'})
    else:
        return jsonify({'erro': 'Esta rota só aceita solicitações POST'}), 400