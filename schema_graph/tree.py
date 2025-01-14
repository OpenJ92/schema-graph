class DatabaseNode:
    def __init__(self, name):
        self.name = name
        self.schemas = {}  # Dictionary of schema_name -> SchemaNode

    def __repr__(self):
        return f"Database: {self.name}"


class SchemaNode:
    def __init__(self, name):
        self.name = name
        self.tables = {}  # Dictionary of table_name -> TableNode

    def __repr__(self):
        return f"Schema: {self.name}"


class TableNode:
    def __init__(self, name, schema):
        self.name = name
        self.schema = schema
        self.columns = {}  # Dictionary of column_name -> ColumnNode
        self.foreign_keys = []  # List of foreign key relationships

    def __repr__(self):
        return f"Table: {self.name}"


class ColumnNode:
    def __init__(self, name, data_type, is_primary_key):
        self.name = name
        self.data_type = data_type
        self.is_primary_key = is_primary_key

    def __repr__(self):
        return f"Column: {self.name} (Type: {self.data_type}, PK: {self.is_primary_key})"

def build_tree(inspector, database):
    """Build a tree structure using dictionaries for schemas, tables, and columns."""
    db_node = DatabaseNode(name=database)

    for schema_name in inspector.get_schema_names():
        if schema_name in ('public', 'information_schema'):
            continue

        schema_node = SchemaNode(name=schema_name)
        db_node.schemas[schema_name] = schema_node

        for table_name in inspector.get_table_names(schema=schema_name):
            table_node = TableNode(name=table_name, schema=schema_name)
            schema_node.tables[table_name] = table_node

            for column in inspector.get_columns(table_name, schema=schema_name):
                col_node = ColumnNode(
                    name=column["name"],
                    data_type=column["type"],
                    is_primary_key=column.get("primary_key", False)
                )
                table_node.columns[column["name"]] = col_node

            for fk in inspector.get_foreign_keys(table_name, schema=schema_name):
                table_node.foreign_keys.append({
                    "source_column": fk["constrained_columns"][0],
                    "target_schema": fk["referred_schema"] or schema_name,
                    "target_table": fk["referred_table"],
                    "target_column": fk["referred_columns"][0],
                })

    return db_node

def pprint_tree(node, indent=0):
    """Pretty-print the tree structure."""
    if isinstance(node, DatabaseNode):
        print(f"{' ' * indent}Database: {node.name}")
        for schema_name, schema in node.schemas.items():
            pprint_tree(schema, indent + 2)
    elif isinstance(node, SchemaNode):
        print(f"{' ' * indent}Schema: {node.name}")
        for table_name, table in node.tables.items():
            pprint_tree(table, indent + 2)
    elif isinstance(node, TableNode):
        print(f"{' ' * indent}Table: {node.name} (Schema: {node.schema})")
        for column_name, column in node.columns.items():
            pprint_tree(column, indent + 2)
    elif isinstance(node, ColumnNode):
        print(f"{' ' * indent}Column: {node.name} (Type: {node.data_type}, PK: {node.is_primary_key})")

