# Huffman's coding



import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

class Solution:
    def huffmanCodes(self, chars, freq):
        heap = []

        for i in range(len(chars)):
            node = Node(chars[i], freq[i])
            heapq.heappush(heap, (freq[i], i, node))

        while len(heap) > 1:
            f1, i1, left = heapq.heappop(heap)
            f2, i2, right = heapq.heappop(heap)

            new_node = Node("", f1 + f2)
            new_node.left = left
            new_node.right = right

            heapq.heappush(heap, (new_node.freq, i1, new_node))

        root = heap[0][2]
        result = {}

        def generate(node, code):
            if node.char:
                result[node.char] = code or "0"
                return

            generate(node.left, code + "0")
            generate(node.right, code + "1")

        generate(root, "")
        return result
