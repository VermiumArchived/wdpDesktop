from ruamel import yaml

with open("./config.yaml", 'r') as fp:
    data = yaml.safe_load(fp)

general = data['general']
ai = data['ai']
dominant = data['dominant']
palette = data['palette']
