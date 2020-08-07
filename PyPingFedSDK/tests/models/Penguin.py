class Penguin():
    """The details of a penguin.

    Attributes
    ----------
    firstName : string
 The penguins first name.
    lastName : string
 The penguins last name.
    height : string
 Height of the penguin.
    soundMade : string
 List of sounds made.

    """

    def __init__(self, firstName=None, lastName=None, height=None, soundMade=None) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.height = height
        self.soundMade = soundMade

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Penguin):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.firstName, self.lastName, self.height, self.soundMade))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["firstName", "lastName", "height", "soundMade"]}

        return cls(**valid_data)