"""
Fix Swagger schema of the "SpSsoServiceEndpoint" model.

The Swagger definition of the "SpSsoServiceEndpoint" model says that the
"binding" and "index" attributes are mandatory. However the description for the
"binding" attribute says that it is usually only required for SAML 2.0
endpoints.

There are cases where the APIs don't return "binding" attribute for an
SpSsoServiceEndpoint object causing a problem when the generated code tries to
convert the response to an SpSsoServiceEndpoint object. Additionally, due to
the nature of the "index' attribute, it is not required for an endpoint for
which "isDefault" is true.

See: https://docs.pingidentity.com/r/en-us/pingfederate-102/idp_endpoints

Since the Swagger definition of the "SpSsoServiceEndpoint" model in the latest
PingFederate release as of the date of writing this code (11.3.2.0) still
specifies it as mandatory it is assumed to be present in all v11 versions.
If/when it gets fixed in a future 11.x version this patch needs to be moved to
the respective versions. That can be done in multiple ways:

    - Copy this patch file to respective versions.
        - Not recommended - needless duplication of code
    - Move this patch file to the lowest version, then in other versions import
      the relevant functions from the "source" version.
        - Pythonic fix, OS independent
    - Move this patch file to the lowest version, then in symlink this to other
      affected versions.
        - Simplest fix
        - OS/Filesystem dependent

This patch changes the spec for the "SpSsoServiceEndpoint" model to make the
"binding" and "index" attributes optional.
"""
import logging
from pathlib import Path


PATCH_NAME = Path(__file__).stem


def patch(swagger_version: str, input_swagger: dict):
    if swagger_version != '2.0':
        logging.warning(
            '%s patch called for swagger version:%s != 2.0, skipping',
            PATCH_NAME, swagger_version
        )
        return
    artifact_settings_model = input_swagger['definitions']['SpSsoServiceEndpoint']
    model_required_list = artifact_settings_model['required']
    model_required_list.remove("binding")
    model_required_list.remove("index")
