import os, yaml

__sample_name = 'config.sample.yaml'

__config_dict = None

def load_config():
    """
    Walks backwards from __file__ to find config.yaml, loads and returns as a
    dictionary.

    Note: traverses up whole file system if config.yaml is not found, but this
          doesn't appear to be a costly opperation.

    source: https://www.programcreek.com/python/example/3198/yaml.safe_load
    """

    global __config_dict

    if __config_dict is not None:
        return __config_dict

    config = None
    f = __file__
    while config is None:
        d = os.path.dirname(f)
        path = os.path.join(d, 'config.yaml')

        if os.path.isfile(path):
            config = path
            break
        elif f == d:
            break

        f = d

    if not config:
        raise Exception('Could not find config.yaml in any parent directory of {}, try copying and renaming {} in projects root directory'.format(__file__, __sample_name))

    __config_dict = yaml.safe_load(open(config).read())

    return __config_dict
