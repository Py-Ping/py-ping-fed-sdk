"""
Fix Swagger schema of the "SpWsTrustAttribute" model.

The Swagger definition of the "SpWsTrustAttribute" model says that the
"namespace" attribute is mandatory. However the documentation for the
"namespace" attribute says that:

    > This is required when the Default Token Type is SAML2.0 or SAML1.1 or
    > SAML1.1 for Office 365.

Since the Swagger definition of the "SpWsTrustAttribute" model in the
latest PingFederate release as of the date of writing this code (11.3.2.0)
still specifies it as mandatory it is assumed to be present in all v11
versions. If/when it gets fixed in a future 11.x version this patch needs to be
moved to the respective versions. That can be done in multiple ways:

    - Copy this patch file to respective versions.
        - Not recommended - needless duplication of code
    - Move this patch file to the lowest version, then in other versions import
      the relevant functions from the "source" version.
        - Pythonic fix, OS independent
    - Move this patch file to the lowest version, then in symlink this to other
      affected versions.
        - Simplest fix
        - OS/Filesystem dependent

This patch changes the spec for the "SpWsTrustAttribute" model to make
the "namespace" attribute optional.
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
    artifact_settings_model = input_swagger['definitions']['SpWsTrustAttribute']
    model_required_list = artifact_settings_model['required']
    model_required_list.remove("namespace")
