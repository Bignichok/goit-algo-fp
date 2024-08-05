import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key, color="skyblue"):
        self.heap.append(Node(key, color))
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index].val < self.heap[parent_index].val:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _build_edges(self, graph, pos, index=0, x=0, y=0, layer=1):
        if index < len(self.heap):
            node = self.heap[index]
            graph.add_node(node.id, color=node.color, label=node.val)
            pos[node.id] = (x, y)

            left_index = 2 * index + 1
            right_index = 2 * index + 2

            if left_index < len(self.heap):
                left_child = self.heap[left_index]
                graph.add_edge(node.id, left_child.id)
                l = x - 1 / 2 ** layer
                pos[left_child.id] = (l, y - 1)
                self._build_edges(graph, pos, left_index, l, y - 1, layer + 1)

            if right_index < len(self.heap):
                right_child = self.heap[right_index]
                graph.add_edge(node.id, right_child.id)
                r = x + 1 / 2 ** layer
                pos[right_child.id] = (r, y - 1)
                self._build_edges(graph, pos, right_index, r, y - 1, layer + 1)

    def draw_heap(self):
        heap_tree = nx.DiGraph()
        pos = {}
        self._build_edges(heap_tree, pos)

        colors = [node[1]['color'] for node in heap_tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in heap_tree.nodes(data=True)}

        plt.figure(figsize=(10, 6))
        nx.draw(heap_tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.show()


heap = BinaryHeap()
heap.insert(10)
heap.insert(4)
heap.insert(5)
heap.insert(30)
heap.insert(3)
heap.insert(1)
heap.insert(6)

heap.draw_heap()
