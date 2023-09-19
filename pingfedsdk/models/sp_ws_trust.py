from enum import Enum

from pingfedsdk.enums import DefaultTokenType
from pingfedsdk.model import Model
from pingfedsdk.models.idp_token_processor_mapping import IdpTokenProcessorMapping
from pingfedsdk.models.protocol_message_customization import ProtocolMessageCustomization
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.sp_ws_trust_attribute_contract import SpWsTrustAttributeContract


class SpWsTrust(Model):
    """Ws-Trust STS provides security-token validation and creation to extend SSO access to identity-enabled Web Services

    Attributes
    ----------
    partnerServiceIds: list
        The partner service identifiers.

    oAuthAssertionProfiles: bool
        When selected, four additional token-type requests become available.

    defaultTokenType: DefaultTokenType
        The default token type when a web service client (WSC) does not specify in the token request which token type the STS should issue. Defaults to SAML 2.0.

    generateKey: bool
        When selected, the STS generates a symmetric key to be used in conjunction with the "Holder of Key" (HoK) designation for the assertion's Subject Confirmation Method.  This option does not apply to OAuth assertion profiles.

    encryptSaml2Assertion: bool
        When selected, the STS encrypts the SAML 2.0 assertion. Applicable only to SAML 2.0 security token.  This option does not apply to OAuth assertion profiles.

    minutesBefore: int
        The amount of time before the SAML token was issued during which it is to be considered valid. The default value is 5.

    minutesAfter: int
        The amount of time after the SAML token was issued during which it is to be considered valid. The default value is 30.

    attributeContract: SpWsTrustAttributeContract
        A set of user attributes that the IdP sends in the token.

    tokenProcessorMappings: list
        A list of token processors to validate incoming tokens.

    abortIfNotFulfilledFromRequest: bool
        If the attribute contract cannot be fulfilled using data from the Request, abort the transaction.

    requestContractRef: ResourceLink
        Request Contract to be used to map attribute values into the security token.

    messageCustomizations: list
        The message customizations for WS-Trust. Depending on server settings, connection type, and protocol this may or may not be supported.

    """
    def __init__(self, partnerServiceIds: list, attributeContract: SpWsTrustAttributeContract, tokenProcessorMappings: list, oAuthAssertionProfiles: bool = None, defaultTokenType: DefaultTokenType = None, generateKey: bool = None, encryptSaml2Assertion: bool = None, minutesBefore: int = None, minutesAfter: int = None, abortIfNotFulfilledFromRequest: bool = None, requestContractRef: ResourceLink = None, messageCustomizations: list = None) -> None:
        self.partnerServiceIds = partnerServiceIds
        self.oAuthAssertionProfiles = oAuthAssertionProfiles
        self.defaultTokenType = defaultTokenType
        self.generateKey = generateKey
        self.encryptSaml2Assertion = encryptSaml2Assertion
        self.minutesBefore = minutesBefore
        self.minutesAfter = minutesAfter
        self.attributeContract = attributeContract
        self.tokenProcessorMappings = tokenProcessorMappings
        self.abortIfNotFulfilledFromRequest = abortIfNotFulfilledFromRequest
        self.requestContractRef = requestContractRef
        self.messageCustomizations = messageCustomizations

    def _validate(self) -> bool:
        return any(x for x in ["attributeContract", "partnerServiceIds", "tokenProcessorMappings"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpWsTrust):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.partnerServiceIds, self.oAuthAssertionProfiles, self.defaultTokenType, self.generateKey, self.encryptSaml2Assertion, self.minutesBefore, self.minutesAfter, self.attributeContract, self.tokenProcessorMappings, self.abortIfNotFulfilledFromRequest, self.requestContractRef, self.messageCustomizations]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["partnerServiceIds", "oAuthAssertionProfiles", "defaultTokenType", "generateKey", "encryptSaml2Assertion", "minutesBefore", "minutesAfter", "attributeContract", "tokenProcessorMappings", "abortIfNotFulfilledFromRequest", "requestContractRef", "messageCustomizations"] and v is not None:
                if k == "partnerServiceIds":
                    valid_data[k] = [str(x) for x in v]
                if k == "oAuthAssertionProfiles":
                    valid_data[k] = bool(v)
                if k == "defaultTokenType":
                    valid_data[k] = DefaultTokenType[v]
                if k == "generateKey":
                    valid_data[k] = bool(v)
                if k == "encryptSaml2Assertion":
                    valid_data[k] = bool(v)
                if k == "minutesBefore":
                    valid_data[k] = int(v)
                if k == "minutesAfter":
                    valid_data[k] = int(v)
                if k == "attributeContract":
                    valid_data[k] = SpWsTrustAttributeContract.from_dict(v)
                if k == "tokenProcessorMappings":
                    valid_data[k] = [IdpTokenProcessorMapping.from_dict(x) for x in v]
                if k == "abortIfNotFulfilledFromRequest":
                    valid_data[k] = bool(v)
                if k == "requestContractRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "messageCustomizations":
                    valid_data[k] = [ProtocolMessageCustomization.from_dict(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["partnerServiceIds", "oAuthAssertionProfiles", "defaultTokenType", "generateKey", "encryptSaml2Assertion", "minutesBefore", "minutesAfter", "attributeContract", "tokenProcessorMappings", "abortIfNotFulfilledFromRequest", "requestContractRef", "messageCustomizations"]:
                if isinstance(v, Model):
                    body[k] = v.to_dict(remove_nonetypes)
                elif isinstance(v, list):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, dict):
                    vals = {}
                    for x, y in v.items():
                        if isinstance(y, Model):
                            vals[x] = y.to_dict(remove_nonetypes)
                        elif not remove_nonetypes or (remove_nonetypes and y is not None):
                            vals[x] = y
                    body[k] = vals
                elif isinstance(v, set):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, Enum):
                    body[k] = str(v).split('.')[-1]
                elif not remove_nonetypes or (remove_nonetypes and v is not None):
                    body[k] = v
        return body
