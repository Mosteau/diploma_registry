from flask import Flask, render_template, request, jsonify
from .blockchain import DiplomaBlockchain
import json
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__, template_folder='../templates', static_folder='../static')
blockchain = None

try:
    blockchain = DiplomaBlockchain()
except Exception as e:
    logger.error(f"Erreur d'initialisation de la blockchain: {str(e)}")

def check_blockchain():
    """Vérifie si la blockchain est initialisée"""
    if not blockchain:
        raise Exception("La connexion à la blockchain n'est pas disponible")

@app.route('/')
def index():
    """Page d'accueil"""
    try:
        check_blockchain()
        network_info = blockchain.get_network_info()
        accounts = blockchain.get_accounts()
        return render_template('index.html', 
                            network_info=network_info,
                            accounts=accounts,
                            blockchain=blockchain)
    except Exception as e:
        return f"Erreur: {str(e)}", 500

@app.route('/issue', methods=['GET', 'POST'])
def issue_diploma():
    """Page d'émission de diplôme"""
    try:
        check_blockchain()
        if request.method == 'POST':
            data = request.get_json()
            result = blockchain.issue_diploma(
                data['student_name'],
                data['diploma_name'],
                data['issuer_address']
            )
            return jsonify(result)
        return render_template('issue.html', blockchain=blockchain)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/verify', methods=['GET', 'POST'])
def verify_diploma():
    try:
        check_blockchain()
        if request.method == 'POST':
            data = request.get_json()
            logger.debug(f"Données reçues: {data}")
            result = blockchain.verify_diploma(data['diploma_hash'])
            response = {
                'is_valid': result['isValid'],
                'student_name': result['studentName'],
                'diploma_name': result['diplomaName'],
                'issue_date': result['issueDate'],
                'institution': result['institution']
            }
            logger.debug(f"Réponse formatée: {response}")
            return jsonify(response)
        return render_template('verify.html', blockchain=blockchain)
    except Exception as e:
        logger.error(f"Erreur lors de la vérification: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/network_info')
def network_info():
    """Endpoint pour récupérer les informations du réseau"""
    try:
        check_blockchain()
        info = blockchain.get_network_info()
        return jsonify(info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/accounts')
def get_accounts():
    """Endpoint pour récupérer la liste des comptes"""
    try:
        check_blockchain()
        accounts = blockchain.get_accounts()
        accounts_with_balance = []
        for account in accounts:
            balance = blockchain.get_balance(account)
            accounts_with_balance.append({
                'address': account,
                'balance': balance
            })
        return jsonify(accounts_with_balance)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    