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

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        block = Block(len(self.chain), self.get_latest_block().hash, self.pending_transactions, time.time())
        block = self.proof_of_work(block)
        self.chain.append(block)

        # 마이너에게 보상을 주기 위한 거래 추가
        self.pending_transactions = [
            {"from": None, "to": miner_address, "amount": self.mining_reward}
        ]

    def proof_of_work(self, block):
        while not block.hash.startswith('0' * self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def __str__(self):
        chain_data = ""
        for block in self.chain:
            chain_data += str(block) + "\n"
        return chain_data

# 블록체인 초기화 및 거래 생성
bansongcoin = Blockchain()

# 새로운 거래 생성
bansongcoin.create_transaction({"from": "Alice", "to": "Bob", "amount": 50})
bansongcoin.create_transaction({"from": "Bob", "to": "Charlie", "amount": 25})

# 채굴 (블록 생성)
bansongcoin.mine_pending_transactions(miner_address="Miner1")

print("Blockchain after mining a block:")
print(bansongcoin)

