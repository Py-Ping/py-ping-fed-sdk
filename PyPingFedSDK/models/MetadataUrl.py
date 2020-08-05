class MetadataUrl():
    """Metadata URL and corresponding Signature Verification Certificate.

    Attributes
    ----------
    certView : str
        The Signature Verification Certificate details. This property is read-only and is always ignored on a POST or PUT.    id : string
        The persistent, unique ID for the Metadata Url. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.    name : string
        The name for the Metadata URL.    url : string
        The Metadata URL.    validateSignature : boolean
        Perform Metadata Signature Validation. The default value is TRUE.    x509File : str
        Data of the Signature Verification Certificate for the Metadata URL.
    """

    __slots__ = ["certView", "id", "name", "url", "validateSignature", "x509File"]

    def __init__(self, name, url, certView=None, id=None, validateSignature=None, x509File=None):
        self.certView = certView
        self.id = id
        self.name = name
        self.url = url
        self.validateSignature = validateSignature
        self.x509File = x509File

    def _validate(self):
        return any(x for x in ['name', 'url'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, MetadataUrl):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.certView, self.id, self.name, self.url, self.validateSignature, self.x509File))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["certView", "id", "name", "url", "validateSignature", "x509File"]}

        return cls(**valid_data)
