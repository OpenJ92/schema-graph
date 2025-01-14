class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, from_node, to_node):
        self.add_node(from_node)
        self.add_node(to_node)
        self.adjacency_list[from_node].append(to_node)

    def __repr__(self):
        return "\n".join(
            f"{node.name}: {[n.name for n in connections]}"
            for node, connections in self.adjacency_list.items()
        )

def build_graph(inspector, tree):
    """Construct a graph using the tree structure with dictionaries."""

    graph = Graph()

    for schema_name, schema_node in tree.schemas.items():
        if schema_name in ('public', 'information_schema'):
            continue

        for table_name, table_node in schema_node.tables.items():
            graph.add_node(table_node)

            # Use the inspector to find foreign key relationships
            foreign_keys = inspector.get_foreign_keys(table_name, schema=schema_name)
            for fk in foreign_keys:
                target_table_node = tree.schemas[fk["referred_schema"] or schema_name].tables[fk["referred_table"]]
                graph.add_edge(table_node, target_table_node)

    return graph

def pprint_graph(graph):
    """Pretty-print the graph structure."""
    print("Graph Structure:")
    for node, connections in graph.adjacency_list.items():
        connections_str = ", ".join([f"{conn.name} (Schema: {conn.schema})" for conn in connections])
        print(f"{node.name} (Schema: {node.schema}): {connections_str}")

