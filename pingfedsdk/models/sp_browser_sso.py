from enum import Enum

from pingfedsdk.enums import Protocol
from pingfedsdk.enums import SpSamlIdentityMapping
from pingfedsdk.enums import SpWsFedIdentityMapping
from pingfedsdk.enums import WsFedTokenType
from pingfedsdk.enums import WsTrustVersion
from pingfedsdk.model import Model
from pingfedsdk.models.artifact_settings import ArtifactSettings
from pingfedsdk.models.assertion_lifetime import AssertionLifetime
from pingfedsdk.models.authentication_policy_contract_assertion_mapping import AuthenticationPolicyContractAssertionMapping
from pingfedsdk.models.encryption_policy import EncryptionPolicy
from pingfedsdk.models.idp_adapter_assertion_mapping import IdpAdapterAssertionMapping
from pingfedsdk.models.protocol_message_customization import ProtocolMessageCustomization
from pingfedsdk.models.slo_service_endpoint import SloServiceEndpoint
from pingfedsdk.models.sp_browser_sso_attribute_contract import SpBrowserSsoAttributeContract
from pingfedsdk.models.sp_sso_service_endpoint import SpSsoServiceEndpoint
from pingfedsdk.models.url_whitelist_entry import UrlWhitelistEntry


class SpBrowserSso(Model):
    """The SAML settings used to enable secure browser-based SSO to resources at your partner's site.

    Attributes
    ----------
    protocol: Protocol
        The browser-based SSO protocol to use.

    wsFedTokenType: WsFedTokenType
        The WS-Federation Token Type to use.

    wsTrustVersion: WsTrustVersion
        The WS-Trust version for a WS-Federation connection. The default version is WSTRUST12.

    enabledProfiles: list
        The profiles that are enabled for browser-based SSO. SAML 2.0 supports all profiles whereas SAML 1.x IdP connections support both IdP and SP (non-standard) initiated SSO. This is required for SAMLx.x Connections.

    incomingBindings: list
        The SAML bindings that are enabled for browser-based SSO. This is required for SAML 2.0 connections when the enabled profiles contain the SP-initiated SSO profile or either SLO profile. For SAML 1.x based connections, it is not used for SP Connections and it is optional for IdP Connections.

    messageCustomizations: list
        The message customizations for browser-based SSO. Depending on server settings, connection type, and protocol this may or may not be supported.

    urlWhitelistEntries: list
        For WS-Federation connections, a whitelist of additional allowed domains and paths used to validate wreply for SLO, if enabled.

    artifact: ArtifactSettings
        The settings for an artifact binding.

    sloServiceEndpoints: list
        A list of possible endpoints to send SLO requests and responses.

    defaultTargetUrl: str
        Default Target URL for SAML1.x connections. For SP connections, this default URL represents the destination on the SP where the user will be directed. For IdP connections, entering a URL in the Default Target URL field overrides the SP Default URL SSO setting.

    alwaysSignArtifactResponse: bool
        Specify to always sign the SAML ArtifactResponse.

    ssoServiceEndpoints: list
        A list of possible endpoints to send assertions to.

    spSamlIdentityMapping: SpSamlIdentityMapping
        Process in which users authenticated by the IdP are associated with user accounts local to the SP.

    spWsFedIdentityMapping: SpWsFedIdentityMapping
        Process in which users authenticated by the IdP are associated with user accounts local to the SP for WS-Federation connection types.

    signResponseAsRequired: bool
        Sign SAML Response as required by the associated binding and encryption policy. Applicable to SAML2.0 only and is defaulted to true. It can be set to false only on SAML2.0 connections when signAssertions is set to true.

    signAssertions: bool
        Always sign the SAML Assertion.

    requireSignedAuthnRequests: bool
        Require AuthN requests to be signed when received via the POST or Redirect bindings.

    encryptionPolicy: EncryptionPolicy
        The SAML 2.0 encryption policy for browser-based SSO. Required for SAML 2.0 connections.

    attributeContract: SpBrowserSsoAttributeContract
        A set of user attributes that the IdP sends in the SAML assertion.

    adapterMappings: list
        A list of adapters that map to outgoing assertions.

    authenticationPolicyContractAssertionMappings: list
        A list of authentication policy contracts that map to outgoing assertions.

    assertionLifetime: AssertionLifetime
        The timeframe of validity before and after the issuance of the assertion.

    """
    def __init__(self, protocol: Protocol, ssoServiceEndpoints: list, encryptionPolicy: EncryptionPolicy, attributeContract: SpBrowserSsoAttributeContract, adapterMappings: list, assertionLifetime: AssertionLifetime, wsFedTokenType: WsFedTokenType = None, wsTrustVersion: WsTrustVersion = None, enabledProfiles: list = None, incomingBindings: list = None, messageCustomizations: list = None, urlWhitelistEntries: list = None, artifact: ArtifactSettings = None, sloServiceEndpoints: list = None, defaultTargetUrl: str = None, alwaysSignArtifactResponse: bool = None, spSamlIdentityMapping: SpSamlIdentityMapping = None, spWsFedIdentityMapping: SpWsFedIdentityMapping = None, signResponseAsRequired: bool = None, signAssertions: bool = None, requireSignedAuthnRequests: bool = None, authenticationPolicyContractAssertionMappings: list = None) -> None:
        self.protocol = protocol
        self.wsFedTokenType = wsFedTokenType
        self.wsTrustVersion = wsTrustVersion
        self.enabledProfiles = enabledProfiles
        self.incomingBindings = incomingBindings
        self.messageCustomizations = messageCustomizations
        self.urlWhitelistEntries = urlWhitelistEntries
        self.artifact = artifact
        self.sloServiceEndpoints = sloServiceEndpoints
        self.defaultTargetUrl = defaultTargetUrl
        self.alwaysSignArtifactResponse = alwaysSignArtifactResponse
        self.ssoServiceEndpoints = ssoServiceEndpoints
        self.spSamlIdentityMapping = spSamlIdentityMapping
        self.spWsFedIdentityMapping = spWsFedIdentityMapping
        self.signResponseAsRequired = signResponseAsRequired
        self.signAssertions = signAssertions
        self.requireSignedAuthnRequests = requireSignedAuthnRequests
        self.encryptionPolicy = encryptionPolicy
        self.attributeContract = attributeContract
        self.adapterMappings = adapterMappings
        self.authenticationPolicyContractAssertionMappings = authenticationPolicyContractAssertionMappings
        self.assertionLifetime = assertionLifetime

    def _validate(self) -> bool:
        return any(x for x in ["adapterMappings", "assertionLifetime", "attributeContract", "encryptionPolicy", "protocol", "ssoServiceEndpoints"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpBrowserSso):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.protocol, self.wsFedTokenType, self.wsTrustVersion, self.enabledProfiles, self.incomingBindings, self.messageCustomizations, self.urlWhitelistEntries, self.artifact, self.sloServiceEndpoints, self.defaultTargetUrl, self.alwaysSignArtifactResponse, self.ssoServiceEndpoints, self.spSamlIdentityMapping, self.spWsFedIdentityMapping, self.signResponseAsRequired, self.signAssertions, self.requireSignedAuthnRequests, self.encryptionPolicy, self.attributeContract, self.adapterMappings, self.authenticationPolicyContractAssertionMappings, self.assertionLifetime]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["protocol", "wsFedTokenType", "wsTrustVersion", "enabledProfiles", "incomingBindings", "messageCustomizations", "urlWhitelistEntries", "artifact", "sloServiceEndpoints", "defaultTargetUrl", "alwaysSignArtifactResponse", "ssoServiceEndpoints", "spSamlIdentityMapping", "spWsFedIdentityMapping", "signResponseAsRequired", "signAssertions", "requireSignedAuthnRequests", "encryptionPolicy", "attributeContract", "adapterMappings", "authenticationPolicyContractAssertionMappings", "assertionLifetime"] and v is not None:
                if k == "protocol":
                    valid_data[k] = Protocol[v]
                if k == "wsFedTokenType":
                    valid_data[k] = WsFedTokenType[v]
                if k == "wsTrustVersion":
                    valid_data[k] = WsTrustVersion[v]
                if k == "enabledProfiles":
                    valid_data[k] = [str(x) for x in v]
                if k == "incomingBindings":
                    valid_data[k] = [str(x) for x in v]
                if k == "messageCustomizations":
                    valid_data[k] = [ProtocolMessageCustomization.from_dict(x) for x in v]
                if k == "urlWhitelistEntries":
                    valid_data[k] = [UrlWhitelistEntry.from_dict(x) for x in v]
                if k == "artifact":
                    valid_data[k] = ArtifactSettings.from_dict(v)
                if k == "sloServiceEndpoints":
                    valid_data[k] = [SloServiceEndpoint.from_dict(x) for x in v]
                if k == "defaultTargetUrl":
                    valid_data[k] = str(v)
                if k == "alwaysSignArtifactResponse":
                    valid_data[k] = bool(v)
                if k == "ssoServiceEndpoints":
                    valid_data[k] = [SpSsoServiceEndpoint.from_dict(x) for x in v]
                if k == "spSamlIdentityMapping":
                    valid_data[k] = SpSamlIdentityMapping[v]
                if k == "spWsFedIdentityMapping":
                    valid_data[k] = SpWsFedIdentityMapping[v]
                if k == "signResponseAsRequired":
                    valid_data[k] = bool(v)
                if k == "signAssertions":
                    valid_data[k] = bool(v)
                if k == "requireSignedAuthnRequests":
                    valid_data[k] = bool(v)
                if k == "encryptionPolicy":
                    valid_data[k] = EncryptionPolicy.from_dict(v)
                if k == "attributeContract":
                    valid_data[k] = SpBrowserSsoAttributeContract.from_dict(v)
                if k == "adapterMappings":
                    valid_data[k] = [IdpAdapterAssertionMapping.from_dict(x) for x in v]
                if k == "authenticationPolicyContractAssertionMappings":
                    valid_data[k] = [AuthenticationPolicyContractAssertionMapping.from_dict(x) for x in v]
                if k == "assertionLifetime":
                    valid_data[k] = AssertionLifetime.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["protocol", "wsFedTokenType", "wsTrustVersion", "enabledProfiles", "incomingBindings", "messageCustomizations", "urlWhitelistEntries", "artifact", "sloServiceEndpoints", "defaultTargetUrl", "alwaysSignArtifactResponse", "ssoServiceEndpoints", "spSamlIdentityMapping", "spWsFedIdentityMapping", "signResponseAsRequired", "signAssertions", "requireSignedAuthnRequests", "encryptionPolicy", "attributeContract", "adapterMappings", "authenticationPolicyContractAssertionMappings", "assertionLifetime"]:
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
