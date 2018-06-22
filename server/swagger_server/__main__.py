#!/usr/bin/env python3

import connexion

from swagger_server import encoder

from beacon_controller import utils

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Translator Knowledge Beacon API'})
    app.run(port=8080)

    utils.initiate_metadata_cache()


if __name__ == '__main__':
    main()
