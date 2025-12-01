class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.exhibits = []  # Store exhibit objects


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, keyword, exhibit):
        node = self.root
        for char in keyword.lower():  # case-insensitive
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
        node.exhibits.append(exhibit)

    def search(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect(node)

    def _collect(self, node):
        results = []
        if node.is_end_of_word:
            results.extend(node.exhibits)
        for child in node.children.values():
            results.extend(self._collect(child))
        return results

class TreeNode:
    def __init__(self, exhibit):
        self.exhibit = exhibit
        self.left = None
        self.right = None


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.history = []   # Stores browsing history (stack)
        self.redo_stack = []  # Optional for redo()

    def insert(self, exhibit):
        new_node = TreeNode(exhibit)
        self.history.append(exhibit)     # Track visited exhibits
        self.redo_stack.clear()          # Reset redo on new insert

        if not self.root:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, root, new_node):
        if new_node.exhibit["name"] < root.exhibit["name"]:
            if root.left:
                self._insert(root.left, new_node)
            else:
                root.left = new_node
        else:
            if root.right:
                self._insert(root.right, new_node)
            else:
                root.right = new_node

    def undo(self):
        if len(self.history) > 1:
            removed = self.history.pop()
            self.redo_stack.append(removed)
            return self.history[-1]  # Return previous exhibit
        return None

    def redo(self):
        if self.redo_stack:
            restored = self.redo_stack.pop()
            self.history.append(restored)
            return restored
        return None

import heapq

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_exhibit(self, exhibit):
        name = exhibit["name"]
        self.nodes[name] = {"data": exhibit, "edges": []}

    def add_edge(self, exhibit1, exhibit2, weight):
        e1 = exhibit1["name"]
        e2 = exhibit2["name"]

        self.nodes[e1]["edges"].append((weight, e2))
        self.nodes[e2]["edges"].append((weight, e1))

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0

        pq = [(0, start)]

        while pq:
            curr_dist, curr_node = heapq.heappop(pq)

            for weight, neighbor in self.nodes[curr_node]["edges"]:
                new_dist = curr_dist + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return distances

# ---- Trie Demo ----
trie = Trie()
trie.insert("Van Gogh", {"name": "Starry Night", "artist": "Van Gogh"})
trie.insert("Renaissance", {"name": "Mona Lisa", "artist": "Leonardo da Vinci"})

print("Search 'Van':", trie.search("Van"))

# ---- RedBlackTree Demo ----
rb = RedBlackTree()
rb.insert({"name": "Starry Night", "artist": "Van Gogh"})
rb.insert({"name": "Mona Lisa", "artist": "Leonardo da Vinci"})

print("Undo:", rb.undo())
print("Redo:", rb.redo())

# ---- Graph Demo ----
graph = Graph()
graph.add_exhibit({"name": "Starry Night"})
graph.add_exhibit({"name": "Mona Lisa"})
graph.add_exhibit({"name": "The Scream"})

graph.add_edge({"name": "Starry Night"}, {"name": "Mona Lisa"}, 5)
graph.add_edge({"name": "Mona Lisa"}, {"name": "The Scream"}, 10)

print("Shortest paths:", graph.dijkstra("Starry Night"))
