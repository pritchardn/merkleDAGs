# Copyright (c) 2020 N.J. Pritchard
# Released under Apache 2.0 License
# Tested with 64-bit Python 3.8

from Block import Block


class MerkleTree:

    def __init__(self):
        self.left = None
        self.right = None
        self.data = Block()

    def print(self):
        self.data.print()
        if type(self.left) == MerkleTree:
            self.left.print()
        if type(self.right) == MerkleTree:
            self.right.print()

    def _add_data(self, data):
        print(data)
        self.data.add_data(data)
        if len(data) > 1:
            bound = len(data)//2
            if len(data) % 2 != 0:
                bound += 1
            self.left = MerkleTree()
            self.data.add_data(self.left._add_data(data[:bound]), "left")
            self.right = MerkleTree()
            self.data.add_data(self.right._add_data(data[bound:]), "right")
        self.data.generate_hash()
        return self.data.hash

    def add_data(self, data):  # Assumes data is list
        print(data)
        self._add_data(data)
