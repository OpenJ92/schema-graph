from sqlalchemy import create_engine, inspect

from schema_graph.core import construct_schema_graph

from schema_graph.tree import pprint_tree
from schema_graph.graph import pprint_graph


# Step 2: Build tree and graph
connection_string = "sqlite://example"
tree, graph = construct_schema_graph(connection_string)

pprint_tree(tree)
pprint_graph(graph)
