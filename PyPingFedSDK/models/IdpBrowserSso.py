class IdpBrowserSso():
    """ The settings used to enable secure browser-based SSO to resources at your site.

    Attributes
    ----------
    adapterMappings : array
        A list of adapters that map to incoming assertions.
    artifact : str
        The settings for an artifact binding.
    assertionsSigned : boolean
        Specify whether the incoming SAML assertions are signed rather than the entire SAML response being signed.
    attributeContract : str
        The list of attributes that the IdP sends in the assertion.
    authenticationPolicyContractMappings : array
        A list of Authentication Policy Contracts that map to incoming assertions.
    authnContextMappings : array
        A list of authentication context mappings between local and remote values. Applicable for SAML 2.0 and OIDC protocol connections.
    decryptionPolicy : str
        The SAML 2.0 decryption policy for browser-based SSO.
    defaultTargetUrl : string
        The default target URL for this connection. If defined, this overrides the default URL.
    enabledProfiles : str
        The profiles that are enabled for browser-based SSO. SAML 2.0 supports all profiles whereas SAML 1.x IdP connections support both IdP and SP (non-standard) initiated SSO. This is required for SAMLx.x Connections.
    idpIdentityMapping : str
        Defines the process in which users authenticated by the IdP are associated with user accounts local to the SP.
    incomingBindings : str
        The SAML bindings that are enabled for browser-based SSO. This is required for SAML 2.0 connections. For SAML 1.x based connections, it is not used for SP Connections and it is optional for IdP Connections.
    messageCustomizations : array
        The message customizations for browser-based SSO. Depending on server settings, connection type, and protocol this may or may not be supported.
    oauthAuthenticationPolicyContractRef : str
        The Authentication policy contract to map into for OAuth. The policy contract can subsequently be mapped into the OAuth persistent grant.
    oidcProviderSettings : str
        The OpenID Provider configuration settings. Required for an OIDC connection.
    protocol : str
        The browser-based SSO protocol to use.
    signAuthnRequests : boolean
        Determines whether SAML authentication requests should be signed.
    sloServiceEndpoints : array
        A list of possible endpoints to send SLO requests and responses.
    ssoOAuthMapping : str
        Direct mapping from the IdP connection to the OAuth persistent grant.
    ssoServiceEndpoints : array
        The IdP SSO endpoints that define where to send your authentication requests. Only required for SP initiated SSO. This is required for SAML x.x and WS-FED Connections.
    urlWhitelistEntries : array
        For WS-Federation connections, a whitelist of additional allowed domains and paths used to validate wreply for SLO, if enabled.

    """

    __slots__ = ["adapterMappings", "artifact", "assertionsSigned", "attributeContract", "authenticationPolicyContractMappings", "authnContextMappings", "decryptionPolicy", "defaultTargetUrl", "enabledProfiles", "idpIdentityMapping", "incomingBindings", "messageCustomizations", "oauthAuthenticationPolicyContractRef", "oidcProviderSettings", "protocol", "signAuthnRequests", "sloServiceEndpoints", "ssoOAuthMapping", "ssoServiceEndpoints", "urlWhitelistEntries"]
    def __init__(self, protocol, idpIdentityMapping, adapterMappings=None, artifact=None, assertionsSigned=None, attributeContract=None, authenticationPolicyContractMappings=None, authnContextMappings=None, decryptionPolicy=None, defaultTargetUrl=None, enabledProfiles=None, incomingBindings=None, messageCustomizations=None, oauthAuthenticationPolicyContractRef=None, oidcProviderSettings=None, signAuthnRequests=None, sloServiceEndpoints=None, ssoOAuthMapping=None, ssoServiceEndpoints=None, urlWhitelistEntries=None):
            self.adapterMappings = adapterMappings
            self.artifact = artifact
            self.assertionsSigned = assertionsSigned
            self.attributeContract = attributeContract
            self.authenticationPolicyContractMappings = authenticationPolicyContractMappings
            self.authnContextMappings = authnContextMappings
            self.decryptionPolicy = decryptionPolicy
            self.defaultTargetUrl = defaultTargetUrl
            self.enabledProfiles = enabledProfiles
            self.idpIdentityMapping = idpIdentityMapping
            self.incomingBindings = incomingBindings
            self.messageCustomizations = messageCustomizations
            self.oauthAuthenticationPolicyContractRef = oauthAuthenticationPolicyContractRef
            self.oidcProviderSettings = oidcProviderSettings
            self.protocol = protocol
            self.signAuthnRequests = signAuthnRequests
            self.sloServiceEndpoints = sloServiceEndpoints
            self.ssoOAuthMapping = ssoOAuthMapping
            self.ssoServiceEndpoints = ssoServiceEndpoints
            self.urlWhitelistEntries = urlWhitelistEntries
    
    def _validate(self):
        return any(x for x in ['protocol', 'idpIdentityMapping'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IdpBrowserSso):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((adapterMappings, artifact, assertionsSigned, attributeContract, authenticationPolicyContractMappings, authnContextMappings, decryptionPolicy, defaultTargetUrl, enabledProfiles, idpIdentityMapping, incomingBindings, messageCustomizations, oauthAuthenticationPolicyContractRef, oidcProviderSettings, protocol, signAuthnRequests, sloServiceEndpoints, ssoOAuthMapping, ssoServiceEndpoints, urlWhitelistEntries))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
