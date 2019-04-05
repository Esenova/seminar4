from mytree import MyTree


heap = []
tree = MyTree()
tree.push_heap(heap, 1)
tree.push_heap(heap, 3)
tree.push_heap(heap, 33)
tree.push_heap(heap, 5)
tree.push_heap(heap, 7)
tree.push_heap(heap, 3)
print(heap)
tree.get_len(heap)

with open("words_19.txt", 'r') as f:
    lines = f.readlines()
    tree.heap_sort(lines)
