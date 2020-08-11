class SpBrowserSso():
    """The SAML settings used to enable secure browser-based SSO to resources at your partner's site.

    Attributes
    ----------
    adapterMappings : array
 A list of adapters that map to outgoing assertions.
    artifact : str
 The settings for an artifact binding.
    assertionLifetime : str
 The timeframe of validity before and after the issuance of the assertion.
    attributeContract : str
 A set of user attributes that the IdP sends in the SAML assertion.
    authenticationPolicyContractAssertionMappings : array
 A list of authentication policy contracts that map to outgoing assertions.
    defaultTargetUrl : string
 Default Target URL for SAML1.x connections. For SP connections, this default URL represents the destination on the SP where the user will be directed. For IdP connections, entering a URL in the Default Target URL field overrides the SP Default URL SSO setting.
    enabledProfiles : str
 The profiles that are enabled for browser-based SSO. SAML 2.0 supports all profiles whereas SAML 1.x IdP connections support both IdP and SP (non-standard) initiated SSO. This is required for SAMLx.x Connections.
    encryptionPolicy : str
 The SAML 2.0 encryption policy for browser-based SSO. Required for SAML 2.0 connections.
    incomingBindings : str
 The SAML bindings that are enabled for browser-based SSO. This is required for SAML 2.0 connections. For SAML 1.x based connections, it is not used for SP Connections and it is optional for IdP Connections.
    messageCustomizations : array
 The message customizations for browser-based SSO. Depending on server settings, connection type, and protocol this may or may not be supported.
    protocol : str
 The browser-based SSO protocol to use.
    requireSignedAuthnRequests : boolean
 Require AuthN requests to be signed when received via the POST or Redirect bindings.
    signAssertions : boolean
 Always sign the SAML Assertion.
    signResponseAsRequired : boolean
 Sign SAML Response as required by the associated binding and encryption policy. Applicable to SAML2.0 only and is defaulted to true. It can be set to false only on SAML2.0 connections when signAssertions is set to true.
    sloServiceEndpoints : array
 A list of possible endpoints to send SLO requests and responses.
    spSamlIdentityMapping : str
 Process in which users authenticated by the IdP are associated with user accounts local to the SP.
    spWsFedIdentityMapping : str
 Process in which users authenticated by the IdP are associated with user accounts local to the SP for WS-Federation connection types.
    ssoServiceEndpoints : array
 A list of possible endpoints to send assertions to.
    urlWhitelistEntries : array
 For WS-Federation connections, a whitelist of additional allowed domains and paths used to validate wreply for SLO, if enabled.
    wsFedTokenType : str
 The WS-Federation Token Type to use.
    wsTrustVersion : str
 The WS-Trust version for a WS-Federation connection. The default version is WSTRUST12.

    """

    def __init__(self, protocol, ssoServiceEndpoints:list, encryptionPolicy, attributeContract, adapterMappings:list, assertionLifetime, artifact=None, authenticationPolicyContractAssertionMappings:list=None, defaultTargetUrl:str=None, enabledProfiles=None, incomingBindings=None, messageCustomizations:list=None, requireSignedAuthnRequests:bool=None, signAssertions:bool=None, signResponseAsRequired:bool=None, sloServiceEndpoints:list=None, spSamlIdentityMapping=None, spWsFedIdentityMapping=None, urlWhitelistEntries:list=None, wsFedTokenType=None, wsTrustVersion=None) -> None:
        self.adapterMappings = adapterMappings
        self.artifact = artifact
        self.assertionLifetime = assertionLifetime
        self.attributeContract = attributeContract
        self.authenticationPolicyContractAssertionMappings = authenticationPolicyContractAssertionMappings
        self.defaultTargetUrl = defaultTargetUrl
        self.enabledProfiles = enabledProfiles
        self.encryptionPolicy = encryptionPolicy
        self.incomingBindings = incomingBindings
        self.messageCustomizations = messageCustomizations
        self.protocol = protocol
        self.requireSignedAuthnRequests = requireSignedAuthnRequests
        self.signAssertions = signAssertions
        self.signResponseAsRequired = signResponseAsRequired
        self.sloServiceEndpoints = sloServiceEndpoints
        self.spSamlIdentityMapping = spSamlIdentityMapping
        self.spWsFedIdentityMapping = spWsFedIdentityMapping
        self.ssoServiceEndpoints = ssoServiceEndpoints
        self.urlWhitelistEntries = urlWhitelistEntries
        self.wsFedTokenType = wsFedTokenType
        self.wsTrustVersion = wsTrustVersion

    def _validate(self) -> bool:
        return any(x for x in ["protocol", "ssoServiceEndpoints", "encryptionPolicy", "attributeContract", "adapterMappings", "assertionLifetime"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpBrowserSso):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.adapterMappings, self.artifact, self.assertionLifetime, self.attributeContract, self.authenticationPolicyContractAssertionMappings, self.defaultTargetUrl, self.enabledProfiles, self.encryptionPolicy, self.incomingBindings, self.messageCustomizations, self.protocol, self.requireSignedAuthnRequests, self.signAssertions, self.signResponseAsRequired, self.sloServiceEndpoints, self.spSamlIdentityMapping, self.spWsFedIdentityMapping, self.ssoServiceEndpoints, self.urlWhitelistEntries, self.wsFedTokenType, self.wsTrustVersion))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["adapterMappings", "artifact", "assertionLifetime", "attributeContract", "authenticationPolicyContractAssertionMappings", "defaultTargetUrl", "enabledProfiles", "encryptionPolicy", "incomingBindings", "messageCustomizations", "protocol", "requireSignedAuthnRequests", "signAssertions", "signResponseAsRequired", "sloServiceEndpoints", "spSamlIdentityMapping", "spWsFedIdentityMapping", "ssoServiceEndpoints", "urlWhitelistEntries", "wsFedTokenType", "wsTrustVersion"]}

        return cls(**valid_data)