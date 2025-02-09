from web3 import Web3
from eth_account import Account
import json
import os
from datetime import datetime

class DiplomaBlockchain:
    def __init__(self, ganache_url='http://127.0.0.1:7545'):
        self.w3 = Web3(Web3.HTTPProvider(ganache_url))
        
        with open('contracts/DiplomaRegistry.json', 'r') as f:
            contract_json = json.load(f)
        
        # Adresse du contrat déployé
        self.contract_address = "YOUR_CONTRACT_ADDRESS"
        self.contract = self.w3.eth.contract(
            address=self.contract_address,
            abi=contract_json['abi']
        )

    def issue_diploma(self, student_name: str, diploma_name: str, institution_address: str):
        """Émettre un nouveau diplôme"""
        nonce = self.w3.eth.get_transaction_count(institution_address)
        
        # Construire la transaction
        transaction = self.contract.functions.issueDiploma(
            student_name,
            diploma_name,
            f"metadata_{datetime.now().timestamp()}"  
        ).build_transaction({
            'gas': 2000000,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': nonce,
        })
        
        return transaction
    
    def verify_diploma(self, diploma_hash: str):
        """Vérifier un diplôme"""
        result = self.contract.functions.verifyDiploma(diploma_hash).call()
        
        return {
            "isValid": result[0],
            "studentName": result[1],
            "diplomaName": result[2],
            "issueDate": datetime.fromtimestamp(result[3]).isoformat(),
            "issuingInstitution": result[4]
        }

# Code pour Flask
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
blockchain = DiplomaBlockchain()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/issue_diploma', methods=['POST'])
def issue_diploma():
    data = request.json
    try:
        tx = blockchain.issue_diploma(
            data['student_name'],
            data['diploma_name'],
            data['institution_address']
        )
        return jsonify({"success": True, "transaction": tx})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/verify_diploma', methods=['POST'])
def verify_diploma():
    data = request.json
    try:
        result = blockchain.verify_diploma(data['diploma_hash'])
        return jsonify({"success": True, "result": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)