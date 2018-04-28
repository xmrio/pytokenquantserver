# encoding=utf8
from django.core.management.base import BaseCommand
from ethereum.models import EthereumBlockModel, EthereumTransactionModel, EthereumTransactionReceiptModel
from web3 import Web3, HTTPProvider
from logging import info as loginfo
import ipdb

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--ip', dest='ip', required=True, help='ip address')
        parser.add_argument('--port', dest='port', required=True, help='RPC port')

    def handle(self, *args, **options):
        ip = options['ip']
        port = options['port']
        w3 = Web3(HTTPProvider(ip+':'+port))
        # ethereumblockmodel = EthereumBlockModel.objects.all().order_by('-number')[0]
        # startblockheight = ethereumblockmodel.height
        blocknumber = w3.eth.blockNumber
        for height in range(1, blocknumber+1):
            block = w3.eth.getBlock(height, True)
            # block data
            loginfo(block['timestamp'])
            EthereumBlockModel.objects.get_or_create(
                number=block['number'],
                defaults={
                    'hash': block['hash'].hex(),
                    'parent_hash': block['parentHash'].hex(),
                    'nonce': block['nonce'].hex(),
                    'transactions_root': block['transactionsRoot'].hex(),
                    'state_root': block['stateRoot'].hex(),
                    'receipts_root': block['receiptsRoot'].hex(),
                    'miner': str(block['miner']),
                    'difficulty': block['difficulty'],
                    'total_difficulty': block['totalDifficulty'],
                    'extra_data': block['extraData'].hex(),
                    'size': block['size'],
                    'gas_limit': str(block['gasLimit']),
                    'gas_used': str(block['gasUsed']),
                    'timestamp': int(block['timestamp']),
                }

            )
            print("nummber:", block['number'], "block hash:", block['hash'].hex())
            # transactions
            transactions = block['transactions']
            for transaction in transactions:
                print("transaction hash:", transaction['hash'].hex())
                self.store_transaction(transaction)
                self.store_transaction_receipt(w3, transaction['hash'])

    # transaction
    def store_transaction_receipt(self, web3, txhash):
        receipt = web3.eth.getTransactionReceipt(txhash.hex())
        status = 0
        try:
            status = int(receipt['status'], 16)
        except KeyError as e:
            status = 9
        print("transaction receipt status:", status)
        EthereumTransactionReceiptModel.objects.get_or_create(
            txhash=receipt['transactionHash'].hex(),
            defaults={
                'txhash': receipt['transactionHash'].hex(),
                'txindex': receipt['transactionIndex'],
                'block_hash': receipt['blockHash'].hex(),
                'block_number': receipt['blockNumber'],
                'total_gas': receipt['cumulativeGasUsed'],
                'gas_used': str(receipt['gasUsed']),
                'contract_address': str(receipt['contractAddress']),
                'root': receipt['root'],
                'status': status,
            }
        )

    def store_transaction(self, transaction):
        EthereumTransactionModel.objects.get_or_create(
            txhash=transaction['hash'].hex(),
            defaults={
                'nonce': transaction['nonce'],
                'block_hash': transaction['blockHash'].hex(),
                'block_number': transaction['blockNumber'],
                'txindex': transaction['transactionIndex'],
                'from_address': str(transaction['from']),
                'to_address': str(transaction['to']),
                'value': str(transaction['value']),
                'gas_price': transaction['gasPrice'],
                'gas': str(transaction['gas']),
                'input_data': transaction['input'],

            }
        )
        print("Transaction Hash:", transaction['hash'].hex())