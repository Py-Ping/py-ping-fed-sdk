

# import json
# import glob
# from collections import defaultdict
# response_codes = defaultdict(lambda: defaultdict(int))
# for file in glob.glob("../pingfedsdk/source/apis/*.json"):
#   #print(file)
#   with open(file) as fh:
#       raw_apis = json.loads(fh.read())
#       for api in raw_apis["apis"]:
#           for operation in api["operations"]:
#               for response_code in operation["responseMessages"]:
#                   response_codes[response_code["code"]][response_code["message"]] += 1
# from pprint import pprint
# pprint(response_codes)


import json
import glob

working = 0
broken = 0
total_modules = 0
total_methods = 0
for file in glob.glob("pingfedsdk/apis/*.py"):
    total_modules += 1
    module_name = file.replace(".py", "").replace("/", ".")
    try:
        abs_module_name = module_name.split(".")[-1]
        module = __import__(module_name, fromlist=[""])
        for x in dir(eval(f"module.{abs_module_name}")):
            if not x.startswith("_"):
                total_methods += 1
        working += 1
    except ModuleNotFoundError as ex:
        broken += 1
        print(ex)

print(f"Found {working}/{total_modules} working, {broken}/{total_modules} broken API modules.")
print(f"Found {total_methods} API methods.")


working = 0
broken = 0
total_modules = 0

for file in glob.glob("pingfedsdk/models/*.py"):
    total_modules += 1
    module_name = file.replace(".py", "").replace("/", ".")
    try:
        abs_module_name = module_name.split(".")[-1]
        module = __import__(module_name, fromlist=[""])
        working += 1
    except ModuleNotFoundError as ex:
        broken += 1
        print(ex)

print(f"Found {working}/{total_modules} working, {broken}/{total_modules} broken model modules.")
