import yaml
import os

# Repeated values
filepath = "..\\config\\defaults.yaml"
fullpath = os.path.join(os.path.dirname(__file__), filepath)

with open(fullpath, 'r') as file:
    global yaml_config
    yaml_config = yaml.safe_load(file)

def test_dependencies(virtualenv):
    
    must_installs = [
        'PyYAML'
    ]
    
    installed_packages = virtualenv.installed_packages()
    
    for module in yaml_config["python"]["global"]["modules"]["standard"]:
        assert module['install'] or module['import'] in installed_packages

    for module in yaml_config["python"]["services"]["modules"]:
        assert module['install'] or module['import'] in installed_packages

    for module in yaml_config["python"]["global"]["modules"]["test"]:
        assert module['install'] or module['import'] in installed_packages

    for module in must_installs:
        assert module in installed_packages