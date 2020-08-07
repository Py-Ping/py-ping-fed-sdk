class ArtifactSettings():
    """The settings for an Artifact binding.

    Attributes
    ----------
    lifetime : integer
 The lifetime of the artifact in seconds.
    resolverLocations : array
 Remote party URLs that you will use to resolve/translate the artifact and get the actual protocol message
    sourceId : string
 Source ID for SAML1.x connections

    """

    def __init__(self, lifetime, resolverLocations, sourceId=None) -> None:
        self.lifetime = lifetime
        self.resolverLocations = resolverLocations
        self.sourceId = sourceId

    def _validate(self) -> bool:
        return any(x for x in ["lifetime", "resolverLocations"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ArtifactSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.lifetime, self.resolverLocations, self.sourceId))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["lifetime", "resolverLocations", "sourceId"]}

        return cls(**valid_data)