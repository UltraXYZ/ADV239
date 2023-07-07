import hashlib
import json
from time import time

chain = []

def block(proof, previous_hash=None):
	transaction = {
		'sender': "Santoshi",
		'recipient': 'Mike',
		'amount': '5 ETH'
	}

	data = {
		'block_height': 1,
		'timestamp': time(),
		'transactions': transaction,
		'block_reward': 2.046327048499942521,
		'uncle_reward': 0,
		'difficulty': 7293278291370357,
		'total difficulty': 28070572181009216929429,
		'size': 81010,
		'gas_used': 14993305,
		'gas_limit': 14999907

	}

	chain.append(block)
	print("block information:", data)
	string_object = json.dumps(data)
	block_string = string_object.encode()

	raw_hash = hashlib.sha256(block_string)
	hex_hash = raw_hash.hexdigest()
	print("hash code of block is ", hex_hash)

block(previous_hash="No previous hash, because this is the first block.", proof=000)
