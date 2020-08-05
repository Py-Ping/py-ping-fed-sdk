class RedirectValidationSettingsWhitelistEntry():
    """Whitelist entry for valid target resource.

    Attributes
    ----------
    allowQueryAndFragment : boolean
        Allow any query parameters and fragment in the resource.    idpDiscovery : boolean
        Enable this target resource for IdP discovery validation.    inErrorResource : boolean
        Enable this target resource for in error resource validation.    requireHttps : boolean
        Require HTTPS for accessing this resource.    targetResourceSLO : boolean
        Enable this target resource for SLO redirect validation.    targetResourceSSO : boolean
        Enable this target resource for SSO redirect validation.    validDomain : string
        Domain of a valid resource.    validPath : string
        Path of a valid resource.
    """

    __slots__ = ["allowQueryAndFragment", "idpDiscovery", "inErrorResource", "requireHttps", "targetResourceSLO", "targetResourceSSO", "validDomain", "validPath"]

    def __init__(self, validDomain, allowQueryAndFragment=None, idpDiscovery=None, inErrorResource=None, requireHttps=None, targetResourceSLO=None, targetResourceSSO=None, validPath=None):
        self.allowQueryAndFragment = allowQueryAndFragment
        self.idpDiscovery = idpDiscovery
        self.inErrorResource = inErrorResource
        self.requireHttps = requireHttps
        self.targetResourceSLO = targetResourceSLO
        self.targetResourceSSO = targetResourceSSO
        self.validDomain = validDomain
        self.validPath = validPath

    def _validate(self):
        return any(x for x in ['validDomain'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, RedirectValidationSettingsWhitelistEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.allowQueryAndFragment, self.idpDiscovery, self.inErrorResource, self.requireHttps, self.targetResourceSLO, self.targetResourceSSO, self.validDomain, self.validPath))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["allowQueryAndFragment", "idpDiscovery", "inErrorResource", "requireHttps", "targetResourceSLO", "targetResourceSSO", "validDomain", "validPath"]}

        return cls(**valid_data)
