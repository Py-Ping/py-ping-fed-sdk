import glob
import json
from pprint import pprint
from collections import defaultdict
from helpers import json_type_convert 

depends_on = {}
base_of = {}
has_type = 0
has_type_list = []
no_type = 0
no_type_list = []
redefinitions = defaultdict(set)

method_types = {}
models = {}

for file in glob.glob("pingfedsdk/source/apis/*.json"):
    with open(file, "+r") as file_handle:
        model_dict = json.loads(file_handle.read())
        for api_data in model_dict["apis"]:
            for operation_data in api_data["operations"]:
                method_types[operation_data["nickname"]] = operation_data["type"]

        for model_name, model_data in model_dict["models"].items():
            models.update(model_dict["models"])
            if file not in redefinitions[model_name]:
                redefinitions[model_name].add(file)
            if 'extends' in model_data:
                depends_on[model_name] = model_data['extends']
                if 'type' in model_data['properties']:
                    has_type += 1
                    has_type_list.append((model_name, model_data['extends']))
                else:
                    no_type += 1
                    no_type_list.append((model_name, model_data['extends']))
            if 'subTypes' in model_data:
                base_of[model_name] = model_data['subTypes']

print(f'There are {len(depends_on)} dependent model classes.')
pprint(depends_on)
print(f'There are {len(base_of)} base model classes.')
pprint(base_of)
