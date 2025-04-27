import yaml

def load_config():
    with open("shared/config.yaml") as f:
        return yaml.safe_load(f)