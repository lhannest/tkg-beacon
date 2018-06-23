from swagger_server.models.beacon_concept import BeaconConcept
from swagger_server.models.beacon_concept_with_details import BeaconConceptWithDetails
from swagger_server.models.exact_match_response import ExactMatchResponse

import beacon_controller.database as db
from beacon_controller.database import Node
from beacon_controller.database.model import NodeConceptDetails
from beacon_controller import utils

import yaml
import configparser

def get_concept_details(conceptId):
    q = """
    MATCH (n) WHERE LOWER(n.id)=LOWER({conceptId})
    RETURN
        n.id AS id,
        n.uri AS uri,
        n.iri AS iri,
        n.name AS name,
        n.category AS category,
        n.symbol AS symbol,
        n.description AS description,
        n.synonym AS synonyms,
        n.clique AS clique
    LIMIT 1
    """

    results = db.query(q, conceptId=conceptId)

    for result in results:
        uri = result['uri'] if result['uri'] != None else result['iri']
        synonyms = result['synonyms'] if result['synonyms'] != None else []
        clique = result['clique'] if result['clique'] != None else []
        clique = utils.remove_all(clique, result['id'])

        return BeaconConceptWithDetails(
            id=result['id'],
            uri=uri,
            name=result['name'],
            category=result['category'],
            symbol=result['symbol'],
            description=result['description'],
            synonyms=result['synonyms'],
            exact_matches=clique
        )

def get_concepts(keywords, categories=None, size=None):
    size = size if size is not None and size > 0 else 100
    categories = categories if categories is not None else []

    q = """
    MATCH (n)
    WHERE
        (ANY (keyword IN {keywords} WHERE
            (ANY (name IN n.name WHERE LOWER(name) CONTAINS LOWER(keyword))))) AND
        (SIZE({categories}) = 0 OR
            ANY (category IN {categories} WHERE
            (ANY (name IN n.category WHERE LOWER(name) = LOWER(category)))))
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

    q = """
    MATCH (n) WHERE LOWER(n.id)=LOWER({curie})
    RETURN n
    """

    exact_matches = []
    for curie in c:
        nodes = db.query(q, NodeConceptDetails, curie=curie)
        if (len(nodes)>=1):
            matches = utils.remove_string_from_list(curie, nodes[0].exact_matches)
            exact_match = ExactMatchResponse(id=curie, within_domain=True, has_exact_matches=matches)
        else:
            exact_match = ExactMatchResponse(id=curie, within_domain=False, has_exact_matches=[])
        exact_matches.append(exact_match)

    return exact_matches
