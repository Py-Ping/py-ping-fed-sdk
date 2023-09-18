"""
Patches to the PingFed-11.3.1 swagger definitions

The PingFed-11.3.1 swagger definition has two invalid model definitions - the
model names have spaces in them:

"A CAPTCHA provider plugin descriptor.": {
    "properties": {
        "attributeContract": {
            "description": "The attribute contract for this plugin.",
            "items": {
                "type": "string"
            },
            "position": 40,
            "type": "array"
        },
        ...
    },
    "type": "object"
},
"A collection of CAPTCHA provider plugin descriptors.": {
    "properties": {
        "items": {
            "description": "The list of CAPTCHA provider plugin descriptors.",
            "items": {
                "$ref": "#/definitions/A CAPTCHA provider plugin descriptor."
            },
            "position": 10,
            "type": "array"
        }
    },
    "type": "object"
}

This patch ensures the models have valid names and APIs that reference these
models use the correct, valid name.
"""
import logging


PATCH_NAME = 'fix_captcha_plugin_descriptor'
DESCRIPTOR_KEY = 'CaptchaProviderPluginDescriptor'
DESCRIPTOR_COLLECTION_KEY = 'CaptchaProviderPluginDescriptorCollection'


def patch_models(input_swagger: dict):
    models = input_swagger['definitions']

    def rename_model(err_key, new_key):
        model_definition = models[err_key]
        models[new_key] = model_definition
        del models[err_key]

    rename_model('A CAPTCHA provider plugin descriptor.', DESCRIPTOR_KEY)
    rename_model('A collection of CAPTCHA provider plugin descriptors.',
                 DESCRIPTOR_COLLECTION_KEY)
    collection_model = models[DESCRIPTOR_COLLECTION_KEY]
    target = collection_model['properties']['items']['items']
    target['$ref'] = f'#/definitions/{DESCRIPTOR_KEY}'


def patch_apis(input_swagger: dict):
    apis = input_swagger['paths']
    target = apis['/captchaProviders/descriptors/{id}']
    target = target['get']['responses']['200']['schema']
    target['$ref'] = f'#/definitions/{DESCRIPTOR_KEY}'

    target = apis['/captchaProviders/descriptors']
    target = target['get']['responses']['200']['schema']
    target['$ref'] = f'#/definitions/{DESCRIPTOR_COLLECTION_KEY}'


def patch(swagger_version: str, input_swagger: dict):
    if swagger_version != '2.0':
        logging.warning('%s patch called for swagger version:%s != 2.0, '
                        'skipping', PATCH_NAME, swagger_version)
        return
    patch_models(input_swagger)
    patch_apis(input_swagger)
