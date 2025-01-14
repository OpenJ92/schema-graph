class DatabaseNode:
    def __init__(self, name):
        self.name = name
        self.schemas = []

    def __repr__(self):
        return f"Database: {self.name}"


class SchemaNode:
    def __init__(self, name):
        self.name = name
        self.tables = []

    def __repr__(self):
        return f"Schema: {self.name}"


class TableNode:
    def __init__(self, name, schema=None):
        self.name = name
        self.schema = schema
        self.columns = []  # List of ColumnNode objects
        self.foreign_keys = []  # List of ForeignKey objects

    def add_foreign_key(self, foreign_key):
        self.foreign_keys.append(foreign_key)

    def __repr__(self):
        return f"Table: {self.name}"


class ColumnNode:
    def __init__(self, name, data_type=None, is_primary_key=False):
        self.name = name
        self.data_type = data_type
        self.is_primary_key = is_primary_key

    def __repr__(self):
        return f"Column: {self.name} ({'PK' if self.is_primary_key else 'column'})"


class ForeignKey:
    def __init__(self, source_table, source_column, target_table, target_column, constraint_name=None):
        self.source_table = source_table  # TableNode
        self.source_column = source_column  # str
        self.target_table = target_table  # TableNode
        self.target_column = target_column  # str
        self.constraint_name = constraint_name  # Optional, str

    def __repr__(self):
        return f"{self.source_table.name}.{self.source_column} -> {self.target_table.name}.{self.target_column}"

