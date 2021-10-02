import hashlib
class NeuralCoinBlock:
    def __init__(self, previos_block_hash, transaction_list):
        self.previous_block_hash = previos_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list)+ "-"+ previos_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Anna sends 2 NC to Mike"
t2 = "Bob sends 4.1 NC to Mike"
t3 = "Mike sends 3.2 NC to Bob"
t4 = "Daniel sends 0.3 NC to Anna"
t5 = "Mike sends 1 NC to Chaile"
t6 = "Mike sends 5.4 NC to Daniel"

intial_block = NeuralCoinBlock("Intial String", [t1, t2])

print(intial_block.block_data)
print(intial_block.block_hash)

second_block = NeuralCoinBlock(intial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)
