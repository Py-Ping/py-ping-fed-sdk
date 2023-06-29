from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.authn_context_mapping import AuthnContextMapping
from pingfedsdk.models.idp_sso_service_endpoint import IdpSsoServiceEndpoint
from pingfedsdk.models.sso_o_auth_mapping import SsoOAuthMapping
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.idp_browser_sso_attribute_contract import IdpBrowserSsoAttributeContract
from pingfedsdk.models.authentication_policy_contract_mapping import AuthenticationPolicyContractMapping
from pingfedsdk.models.o_i_d_c_provider_settings import OIDCProviderSettings
from pingfedsdk.models.artifact_settings import ArtifactSettings
from pingfedsdk.models.jit_provisioning import JitProvisioning
from pingfedsdk.models.protocol_message_customization import ProtocolMessageCustomization
from pingfedsdk.models.sp_adapter_mapping import SpAdapterMapping
from pingfedsdk.models.slo_service_endpoint import SloServiceEndpoint
from pingfedsdk.models.url_whitelist_entry import UrlWhitelistEntry
from pingfedsdk.models.decryption_policy import DecryptionPolicy
from pingfedsdk.enums import Protocol
from pingfedsdk.enums import IdpIdentityMapping


class IdpBrowserSso(Model):
    """The settings used to enable secure browser-based SSO to resources at your site.

    Attributes
    ----------
    protocol: Protocol
        The browser-based SSO protocol to use.

    oidcProviderSettings: OIDCProviderSettings
        The OpenID Provider configuration settings. Required for an OIDC connection.

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

    alwaysSignArtifactResponse: bool
        Specify to always sign the SAML ArtifactResponse.

    ssoServiceEndpoints: list
        The IdP SSO endpoints that define where to send your authentication requests. Only required for SP initiated SSO. This is required for SAML x.x and WS-FED Connections.

    defaultTargetUrl: str
        The default target URL for this connection. If defined, this overrides the default URL.

    authnContextMappings: list
        A list of authentication context mappings between local and remote values. Applicable for SAML 2.0 and OIDC protocol connections.

    assertionsSigned: bool
        Specify whether the incoming SAML assertions are signed rather than the entire SAML response being signed.

    signAuthnRequests: bool
        Determines whether SAML authentication requests should be signed.

    decryptionPolicy: DecryptionPolicy
        The SAML 2.0 decryption policy for browser-based SSO.

    idpIdentityMapping: IdpIdentityMapping
        Defines the process in which users authenticated by the IdP are associated with user accounts local to the SP.

    attributeContract: IdpBrowserSsoAttributeContract
        The list of attributes that the IdP sends in the assertion.

    adapterMappings: list
        A list of adapters that map to incoming assertions.

    authenticationPolicyContractMappings: list
        A list of Authentication Policy Contracts that map to incoming assertions.

    ssoOAuthMapping: SsoOAuthMapping
        Direct mapping from the IdP connection to the OAuth persistent grant.

    oauthAuthenticationPolicyContractRef: ResourceLink
        The Authentication policy contract to map into for OAuth. The policy contract can subsequently be mapped into the OAuth persistent grant.

    jitProvisioning: JitProvisioning
        JIT Provisioning of user accounts.

    """

    def __init__(self, idpIdentityMapping: IdpIdentityMapping, protocol: Protocol, oidcProviderSettings: OIDCProviderSettings = None, enabledProfiles: list = None, incomingBindings: list = None, messageCustomizations: list = None, urlWhitelistEntries: list = None, artifact: ArtifactSettings = None, sloServiceEndpoints: list = None, alwaysSignArtifactResponse: bool = None, ssoServiceEndpoints: list = None, defaultTargetUrl: str = None, authnContextMappings: list = None, assertionsSigned: bool = None, signAuthnRequests: bool = None, decryptionPolicy: DecryptionPolicy = None, attributeContract: IdpBrowserSsoAttributeContract = None, adapterMappings: list = None, authenticationPolicyContractMappings: list = None, ssoOAuthMapping: SsoOAuthMapping = None, oauthAuthenticationPolicyContractRef: ResourceLink = None, jitProvisioning: JitProvisioning = None) -> None:
        self.protocol = protocol
        self.oidcProviderSettings = oidcProviderSettings
        self.enabledProfiles = enabledProfiles
        self.incomingBindings = incomingBindings
        self.messageCustomizations = messageCustomizations
        self.urlWhitelistEntries = urlWhitelistEntries
        self.artifact = artifact
        self.sloServiceEndpoints = sloServiceEndpoints
        self.alwaysSignArtifactResponse = alwaysSignArtifactResponse
        self.ssoServiceEndpoints = ssoServiceEndpoints
        self.defaultTargetUrl = defaultTargetUrl
        self.authnContextMappings = authnContextMappings
        self.assertionsSigned = assertionsSigned
        self.signAuthnRequests = signAuthnRequests
        self.decryptionPolicy = decryptionPolicy
        self.idpIdentityMapping = idpIdentityMapping
        self.attributeContract = attributeContract
        self.adapterMappings = adapterMappings
        self.authenticationPolicyContractMappings = authenticationPolicyContractMappings
        self.ssoOAuthMapping = ssoOAuthMapping
        self.oauthAuthenticationPolicyContractRef = oauthAuthenticationPolicyContractRef
        self.jitProvisioning = jitProvisioning

    def _validate(self) -> bool:
        return any(x for x in ["idpIdentityMapping", "protocol"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpBrowserSso):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.protocol, self.oidcProviderSettings, self.enabledProfiles, self.incomingBindings, self.messageCustomizations, self.urlWhitelistEntries, self.artifact, self.sloServiceEndpoints, self.alwaysSignArtifactResponse, self.ssoServiceEndpoints, self.defaultTargetUrl, self.authnContextMappings, self.assertionsSigned, self.signAuthnRequests, self.decryptionPolicy, self.idpIdentityMapping, self.attributeContract, self.adapterMappings, self.authenticationPolicyContractMappings, self.ssoOAuthMapping, self.oauthAuthenticationPolicyContractRef, self.jitProvisioning]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["protocol", "oidcProviderSettings", "enabledProfiles", "incomingBindings", "messageCustomizations", "urlWhitelistEntries", "artifact", "sloServiceEndpoints", "alwaysSignArtifactResponse", "ssoServiceEndpoints", "defaultTargetUrl", "authnContextMappings", "assertionsSigned", "signAuthnRequests", "decryptionPolicy", "idpIdentityMapping", "attributeContract", "adapterMappings", "authenticationPolicyContractMappings", "ssoOAuthMapping", "oauthAuthenticationPolicyContractRef", "jitProvisioning"] and v is not None:
                if k == "protocol":
                    valid_data[k] = Protocol[v]
                if k == "oidcProviderSettings":
                    valid_data[k] = OIDCProviderSettings(**v)
                if k == "enabledProfiles":
                    valid_data[k] = [str(x) for x in v]
                if k == "incomingBindings":
                    valid_data[k] = [str(x) for x in v]
                if k == "messageCustomizations":
                    valid_data[k] = [ProtocolMessageCustomization(**x) for x in v]
                if k == "urlWhitelistEntries":
                    valid_data[k] = [UrlWhitelistEntry(**x) for x in v]
                if k == "artifact":
                    valid_data[k] = ArtifactSettings(**v)
                if k == "sloServiceEndpoints":
                    valid_data[k] = [SloServiceEndpoint(**x) for x in v]
                if k == "alwaysSignArtifactResponse":
                    valid_data[k] = bool(v)
                if k == "ssoServiceEndpoints":
                    valid_data[k] = [IdpSsoServiceEndpoint(**x) for x in v]
                if k == "defaultTargetUrl":
                    valid_data[k] = str(v)
                if k == "authnContextMappings":
                    valid_data[k] = [AuthnContextMapping(**x) for x in v]
                if k == "assertionsSigned":
                    valid_data[k] = bool(v)
                if k == "signAuthnRequests":
                    valid_data[k] = bool(v)
                if k == "decryptionPolicy":
                    valid_data[k] = DecryptionPolicy(**v)
                if k == "idpIdentityMapping":
                    valid_data[k] = IdpIdentityMapping[v]
                if k == "attributeContract":
                    valid_data[k] = IdpBrowserSsoAttributeContract(**v)
                if k == "adapterMappings":
                    valid_data[k] = [SpAdapterMapping(**x) for x in v]
                if k == "authenticationPolicyContractMappings":
                    valid_data[k] = [AuthenticationPolicyContractMapping(**x) for x in v]
                if k == "ssoOAuthMapping":
                    valid_data[k] = SsoOAuthMapping(**v)
                if k == "oauthAuthenticationPolicyContractRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "jitProvisioning":
                    valid_data[k] = JitProvisioning(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["protocol", "oidcProviderSettings", "enabledProfiles", "incomingBindings", "messageCustomizations", "urlWhitelistEntries", "artifact", "sloServiceEndpoints", "alwaysSignArtifactResponse", "ssoServiceEndpoints", "defaultTargetUrl", "authnContextMappings", "assertionsSigned", "signAuthnRequests", "decryptionPolicy", "idpIdentityMapping", "attributeContract", "adapterMappings", "authenticationPolicyContractMappings", "ssoOAuthMapping", "oauthAuthenticationPolicyContractRef", "jitProvisioning"]:
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
