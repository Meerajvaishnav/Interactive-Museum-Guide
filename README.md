# Interactive-Museum-Guide

A modular **Python** project that simulates a smart museum guide application using advanced data structures and algorithms for exhibit search, browsing history, and shortest-path navigation inside a virtual museum.

## Features

1. **Trie-based exhibit search**
   - Insert and search exhibits by name, artist, or art style/category.
   - Supports prefix-based search so typing `Van` returns all Van Gogh-related exhibits.

2. **Browsing history with undo/redo**
   - Simplified Red-Black-Tree-inspired structure for storing visits using a binary tree plus stacks.
   - Maintain a visit history, undo the last exhibit visit, and redo previously undone visits.

3. **Shortest-path navigation (Dijkstra + graph)**
   - Undirected, weighted graph model of the museum floor with exhibits as nodes.
   - Dijkstra’s algorithm computes the optimal walking distance between exhibits.

4. **Modular, educational design**
   - Clean separation into `Trie`, `RedBlackTree` (history), and `Graph` (navigation) components.
   - Ideal as a reference or teaching example for advanced data structures in a realistic context.

## Tech Stack

- **Language:** Python 3.x
- **Data Structures & Algorithms:**
  - Trie (prefix-based search)
  - Binary tree + stacks for history (simplified Red-Black Tree model)
  - Graph (adjacency list)
  - Dijkstra’s shortest-path algorithm with a priority queue (`heapq`).

### Core Components

1. **Trie**
   - `insert(keyword, exhibit)` to index exhibits by name/artist/style.
   - `search(prefix)` to return all exhibits starting with the given prefix.

2. **RedBlackTree (simplified)**
   - `insert(exhibit)` to add a visited exhibit to history.
   - `undo()` to revert to the previous exhibit and push the last visit into a redo stack.
   - `redo()` to restore an exhibit visit from the redo stack.

3. **Graph**
   - `add_exhibit(exhibit)` to register an exhibit node.
   - `add_edge(exhibit1, exhibit2, weight)` to connect two exhibits with a walking distance.
   - `dijkstra(start)` to compute shortest distances from a starting exhibit to all others.
## Prerequisites

- Python 3.8+ installed.

## Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/smart-museum-guide.git
cd smart-museum-guide
```

## Running the Demo
```bash
python museum.py
```

The demo currently:
- Inserts sample exhibits into the Trie and performs a prefix search like `"Van"`.
- Simulates exhibit visits and shows undo/redo behavior on the history structure.
- Builds a small graph of exhibits and prints shortest path distances from `"Starry Night"`.
