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
        
t1 = "Anna sends 2 BC to Mike" 
t2 = "Bob sends 4.1 BC to Mike"        
t3 = "Mike sends 3.2 BC to Bob"        
t4 = "Daniel sends 0.3 BC to Anna"        
t5 = "Mike sends 1 BC to Charlie"        
t6 = "Mike sends 5.4 BC to Daniel"      

initial_block = BansongCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = BansongCoinBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = BansongCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)