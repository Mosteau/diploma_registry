from web3 import Web3
from eth_account import Account
import json
import os
from datetime import datetime

class DiplomaBlockchain:
    def __init__(self, ganache_url='http://127.0.0.1:7545'):
        """Initialise la connexion à la blockchain"""
        self.w3 = Web3(Web3.HTTPProvider(ganache_url))
        
        # Vérification de la connexion
        if not self.w3.is_connected():
            raise Exception("Impossible de se connecter à Ganache")
            
        print(f"Connecté à Ganache: {self.w3.is_connected()}")
        
        # Chargement du contrat (à décommenter après avoir déployé le contrat)
        # with open('contracts/DiplomaRegistry.json', 'r') as f:
        #     contract_json = json.load(f)
        # self.contract_address = "ADRESSE_DU_CONTRAT_DEPLOYE"
        # self.contract = self.w3.eth.contract(
        #     address=self.contract_address,
        #     abi=contract_json['abi']
        # )

    def get_accounts(self):
        """Récupère la liste des comptes disponibles"""
        return self.w3.eth.accounts

    def get_balance(self, address):
        """Récupère le solde d'une adresse"""
        balance = self.w3.eth.get_balance(address)
        return self.w3.from_wei(balance, 'ether')

    def issue_diploma(self, student_name, diploma_name, issuer_address):
        """Émet un nouveau diplôme"""
        # Simulation pour le MVP
        diploma_hash = self.w3.keccak(text=f"{student_name}{diploma_name}{datetime.now().isoformat()}")
        return {
            'success': True,
            'diploma_hash': diploma_hash.hex(),
            'student_name': student_name,
            'diploma_name': diploma_name,
            'issuer': issuer_address,
            'timestamp': datetime.now().isoformat()
        }

    def verify_diploma(self, diploma_hash):
        """Vérifie un diplôme"""
        # Simulation pour le MVP
        return {
            'isValid': True,
            'studentName': "Exemple Étudiant",
            'diplomaName': "Master en Informatique",
            'issueDate': datetime.now().isoformat(),
            'institution': "0x123..."
        }

    def get_network_info(self):
        """Récupère les informations du réseau"""
        return {
            'connected': self.w3.is_connected(),
            'network_id': self.w3.net.version,
            'gas_price': self.w3.eth.gas_price,
            'block_number': self.w3.eth.block_number
        }