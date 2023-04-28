from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from uuid import UUID, uuid4

class Book(Model):
    __keyspace__ = "linkedin"
    id: UUID = columns.UUID(primary_key=True, default=uuid4())
    author_id: UUID = columns.UUID(index=True)
    name: str = columns.Text()

class Author(Model):
    __keyspace__ = "linkedin"
    id: UUID = columns.UUID(primary_key=True, default=uuid4())
    name: str = columns.Text()
