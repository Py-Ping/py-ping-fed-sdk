"""
Fix Swagger definition of the "AccessTokenMappingContext schema.

The Swagger definition of the "AccessTokenMappingContext" object says that it
has three attributes - "description", "type" and "contextRef" of which "type"
and "contextRef" are mandatory.

However, in some cases the API does not return the "contextRef" attribute which
can cause problems when the generated SDK tries to create
AccessTokenMappingContext objects from results of an API call.

This behaviour has been observed in 11.1.7 and 11.3.1 and therefore we assume
is in all v11 versions. If/when it gets fixed in a future 11.x version this
patch needs to be moved to the respective versions. That can be done in
multiple ways:

    - Copy this patch file to respective versions.
        - Not recommended - needless duplication of code
    - Move this patch file to the lowest version, then in other versions import
      the relevant functions from the "source" version.
        - Pythonic fix, OS independent
    - Move this patch file to the lowest version, then in symlink this to other
      affected versions.
        - Simplest fix
        - OS/Filesystem dependent
"""
import logging
from pathlib import Path


PATCH_NAME = Path(__file__).stem


def patch(swagger_version: str, input_swagger: dict):
    if swagger_version != '2.0':
        logging.warning('%s patch called for swagger version:%s != 2.0, '
                        'skipping', PATCH_NAME, swagger_version)
        return
    models = input_swagger['definitions']
    target_model = models['AccessTokenMappingContext']
    required_properties = target_model['required']
    required_properties.remove('contextRef')
