"""
Fix Swagger schema of the "SpBrowserSsoAttribute" model.

The Swagger definition of the "SpBrowserSsoAttribute" model (which is used for
definining both "core" as well as "extended" attributes of
"SpBrowserSsoAttributeContract") says that the "nameFormat" attribute is
mandatory. However there are cases where it is not returned by an API call - in
those cases it is always a core attribute in question because the name format
of core attributes are specified by the SAML spec and therefore are not needed.
Besides, no APIs allow modification of the core attributes - only extended
attributes can be modified and for them the "nameFormat" attribute is required.
Unfortunately since the Swagger definition uses the same model for both core
and extended attributes the nameFormat attribute must be made optional to
accomodate for core attributes not returning the "nameFormat" attribute.

Since the Swagger definition of the "SpBrowserSsoAttribute" model in the latest
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

This patch changes the spec for the "SpBrowserSsoAttribute" model to make the
"nameFormat" attribute optional.
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
    artifact_settings_model = input_swagger['definitions']['SpBrowserSsoAttribute']
    model_required_list = artifact_settings_model['required']
    model_required_list.remove("nameFormat")
