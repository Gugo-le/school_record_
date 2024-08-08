'''
Bansong Coin (BC)

t1: Anna sends Bob 2BC
t2: Bob sends Daniel 4.3 BC
t3: Mark sends Charlie 3.2 BC

SHA256
B1("AAA", t1, t2, t3) -> 76fd89, B2("76fd89", t4, t5, t6) -> 8923ff, B3(8923ff, t7)

BansongHash()
'''

import hashlib

class BansongCoinBlock:
    def __init__(self, previous_block_hash, tranction_list):
        self.previous_block_hash = previous_block_hash
        self.tranction_list = tranction_list
        
        self.block_data = "-".join(tranction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
      