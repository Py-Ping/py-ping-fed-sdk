from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.artifact_resolver_location import ArtifactResolverLocation


class ArtifactSettings(Model):
    """The settings for an Artifact binding.

    Attributes
    ----------
    lifetime: int
        The lifetime of the artifact in seconds.

    resolverLocations: list
        Remote party URLs that you will use to resolve/translate the artifact and get the actual protocol message

    sourceId: str
        Source ID for SAML1.x connections

    """
    def __init__(self, resolverLocations: list, lifetime: int = None, sourceId: str = None) -> None:
        self.lifetime = lifetime
        self.resolverLocations = resolverLocations
        self.sourceId = sourceId

    def _validate(self) -> bool:
        return any(x for x in ["resolverLocations"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ArtifactSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.lifetime, self.resolverLocations, self.sourceId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["lifetime", "resolverLocations", "sourceId"] and v is not None:
                if k == "lifetime":
                    valid_data[k] = int(v)
                if k == "resolverLocations":
                    valid_data[k] = [ArtifactResolverLocation.from_dict(x) for x in v]
                if k == "sourceId":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["lifetime", "resolverLocations", "sourceId"]:
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
