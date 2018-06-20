from swagger_server.models.beacon_concept import BeaconConcept
from swagger_server.models.beacon_concept_with_details import BeaconConceptWithDetails
from swagger_server.models.exact_match_response import ExactMatchResponse

import beacon_controller.database as db
from beacon_controller.database import Node
from beacon_controller import utils

import yaml
import configparser

def get_concept_details(conceptId):
    config = utils.load_config()
    return config['client']['database']

def get_concepts(keywords, categories=None, size=None):
    size = size if size is not None and size > 0 else 100
    categories = categoreis if categories is not None else []

    import pudb; pu.db

    q = """
        MATCH (n)
        WHERE
            ANY (keyword IN {keywords} WHERE LOWER(n.name) CONTAINS LOWER(keyword))
        RETURN n
        LIMIT {limit}
    """

    nodes = db.query(q, Node, keywords=keywords, categories=categories, limit=size)

    concepts = []

    for node in nodes:
        concept = BeaconConcept(
            id=node.curie,
            name=node.name,
            category=node.category,
            description=node.description
        )

        concepts.append(concept)

    return concepts

def get_exact_matches_to_concept_list(c):
    return 'do some magic!'
