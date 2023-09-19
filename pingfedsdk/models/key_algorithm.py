from enum import Enum

from pingfedsdk.model import Model


class KeyAlgorithm(Model):
    """Details for a key algorithm.

    Attributes
    ----------
    name: str
        Name of the key algorithm.

    keySizes: list
        Possible key sizes for this algorithm, in bits.

    defaultKeySize: int
        Default key size for this algorithm.

    signatureAlgorithms: list
        Possible signature algorithms for this key algorithm.

    defaultSignatureAlgorithm: str
        Default signature algorithm for this key algorithm.

    """
    def __init__(self, name: str = None, keySizes: list = None, defaultKeySize: int = None, signatureAlgorithms: list = None, defaultSignatureAlgorithm: str = None) -> None:
        self.name = name
        self.keySizes = keySizes
        self.defaultKeySize = defaultKeySize
        self.signatureAlgorithms = signatureAlgorithms
        self.defaultSignatureAlgorithm = defaultSignatureAlgorithm

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, KeyAlgorithm):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.name, self.keySizes, self.defaultKeySize, self.signatureAlgorithms, self.defaultSignatureAlgorithm]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["name", "keySizes", "defaultKeySize", "signatureAlgorithms", "defaultSignatureAlgorithm"] and v is not None:
                if k == "name":
                    valid_data[k] = str(v)
                if k == "keySizes":
                    valid_data[k] = [int(x) for x in v]
                if k == "defaultKeySize":
                    valid_data[k] = int(v)
                if k == "signatureAlgorithms":
                    valid_data[k] = [str(x) for x in v]
                if k == "defaultSignatureAlgorithm":
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
            if k in ["name", "keySizes", "defaultKeySize", "signatureAlgorithms", "defaultSignatureAlgorithm"]:
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
