import hashlib
import time

# 블록 클래스 정의
class Block:
    def __init__(self, index, previous_hash, transactions, timestamp, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (str(self.index) + str(self.previous_hash) + 
                        str(self.transactions) + str(self.timestamp) + 
                        str(self.nonce)).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        return f"Block #{self.index} [Previous Hash: {self.previous_hash}, Hash: {self.hash}, Transactions: {self.transactions}]"

# 블록체인 클래스 정의
class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions = []
        self.mining_reward = 1

    