from sqlalchemy import create_engine, inspect

from schema_graph.tree import build_tree, pprint_tree
from schema_graph.graph import build_graph, pprint_graph

def construct_schema_graph(connection_string):
    """Constructs both the tree and graph from the given metadata."""
    # Step 1: Build the tree
    engine = create_engine(connection_string)

    database, inspector = engine.url.database, inspect(engine)
    database_tree = build_tree(inspector, database)
    database_graph = build_graph(inspector, database_tree)
    return database_tree, database_graph
