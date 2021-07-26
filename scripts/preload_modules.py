"""

"""

import glob


def to_camel_case(snake_str):
    snake_str_list = snake_str.split('_')
    camel_case_list = [
        x.title() for x in snake_str_list
    ]
    return "".join(camel_case_list)


working = 0
broken = 0
total_modules = 0
total_methods = 0
for file in glob.glob("pingfedsdk/apis/*.py"):
    total_modules += 1
    module_name = file.replace(".py", "").replace("/", ".")
    try:
        abs_module_name = to_camel_case(module_name.split(".")[-1])
        module = __import__(module_name, fromlist=[""])
        for x in dir(eval(f"module.{abs_module_name}")):
            if not x.startswith("_"):
                total_methods += 1
        working += 1
    except ModuleNotFoundError as ex:
        broken += 1
        print(ex)

print(
    f"Found {working}/{total_modules} working, "
    f"{broken}/{total_modules} broken API modules."
)
print(f"Found {total_methods} API methods.")


working = 0
broken = 0
total_modules = 0

for file in glob.glob("pingfedsdk/models/*.py"):
    total_modules += 1
    module_name = file.replace(".py", "").replace("/", ".")
    try:
        abs_module_name = to_camel_case(module_name.split(".")[-1])
        module = __import__(module_name, fromlist=[""])
        working += 1
    except ModuleNotFoundError as ex:
        broken += 1
        print(ex)

print(
    f"Found {working}/{total_modules} working, "
    f"{broken}/{total_modules} broken model modules."
)
