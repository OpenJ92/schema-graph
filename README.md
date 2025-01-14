# Schema-Graph: Database Schema Exploration and Query Construction

## Overview
Schema-Graph is a Python-based project designed to analyze and interact with relational database schemas. By constructing tree and graph representations of the database structure, the project provides an organized way to explore schemas, tables, columns, and relationships. This foundational structure will serve as the backbone for advanced features like query generation and database migration tracking.

---

## Current Features

### 1. **Tree Structure Representation**
- Hierarchical representation of the database structure:
  - **Database**
  - **Schemas**
  - **Tables**
  - **Columns**
- Allows efficient access to schemas, tables, and columns using dictionary-based organization.

### 2. **Graph Structure Representation**
- Graph representation of tables and their relationships:
  - Nodes represent `TableNode` objects.
  - Edges represent foreign key relationships.
- Built dynamically by traversing the tree structure, ensuring object consistency.

### 3. **Pretty-Print Utilities**
- Human-readable output for tree and graph structures for debugging and exploration.

---

## Future Features

### 1. **Graph Traversals for Query Construction**
- Develop advanced graph traversal algorithms for partial query generation.
- Feed traversal results into Jinja2 templates to build modular, reusable SQL queries.

### 2. **Advanced Schema Comparison**
- Extend comparison functionality to:
  - Detect foreign key relationship changes.
  - Highlight column-level modifications (e.g., data type changes, added constraints).

### 3. **Database Migration Tracking**
- Maintain a history of schema-graphs for tracking database evolution.
- Visualize differences between versions for better migration insights.

### 4. **Query Optimization Features**
- Suggest optimized joins and filters based on the graph structure.

### 5. **Visualization**
- Integrate with visualization libraries like `networkx` or `graphviz` to render schema graphs.
- Provide clear insights into table relationships and dependencies.

---

## Usage

### **Constructing the Tree and Graph**
```python
from schema_graph.core import construct_schema_graph
from schema_graph.tree import pprint_tree
from schema_graph.graph import pprint_graph

# Step 2: Build tree and graph
connection_string = "sqlite://example"
tree, graph = construct_schema_graph(connection_string)

pprint_tree(tree)
pprint_graph(graph)
```

---

## Contribution and Future Development

This project is in its early stages, with a strong foundation laid for future enhancements. Contributions are welcome to expand the functionality or optimize the existing features.

### Planned Development
- **Graph Traversals**: Implement advanced algorithms for better query construction.
- **Migration Tracking**: Build tools to visualize and analyze schema evolution.
- **Documentation**: Provide comprehensive examples and API documentation.
- **Testing**: Add robust test cases to ensure reliability.

Let’s build a powerful tool for database schema analysis and query generation together!

