"""
overrides.py: class to handle
"""

import json
import json_delta


class IncorrectVersion(Exception):
    pass


class Override:
    def __init__(self, file_path, current_version):
        # 1. read the json file
        # 2. construct dictionary representing the delta
        # 3. track applicable version
        # 4. track applicable file

        self.current_version = current_version
        self.override_patch = json.loads(open(file_path).read())
        self.file = file_path.split("/")[-1].split(".")[0]
        self.patch_version = ".".join(file_path.split("/")[-1].split(".")[1:-1])

    def apply_patch(self, api_json):
        if self.current_version == "all" or "apiVersion" in api_json and \
           api_json["apiVersion"] == self.current_version:
            return json_delta.patch(api_json, self.override_patch)
        raise IncorrectVersion
