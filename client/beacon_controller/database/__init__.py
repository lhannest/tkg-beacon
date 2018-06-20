from . import config
from .model import Node, Edge

from neomodel import db

def query(q, inflator, **kwargs):
    results, meta = db.cypher_query(q, kwargs)
    return [inflator.inflate(row[0]) for row in results]
