class ContactInfo():
    """Contact information.

    Attributes
    ----------
    company : string
 Company name.
    email : string
 Contact email address.
    firstName : string
 Contact first name.
    lastName : string
 Contact last name.
    phone : string
 Contact phone number.

    """

<<<<<<< HEAD
    def __init__(self, company=None, email=None, firstName=None, lastName=None, phone=None) -> None:
        self.company = company
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
=======
    def __init__(self, company=None, email=None, firstName=None, lastName=None, phone=None):
        self.company: str = company
        self.email: str = email
        self.firstName: str = firstName
        self.lastName: str = lastName
        self.phone: str = phone
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ContactInfo):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.company, self.email, self.firstName, self.lastName, self.phone))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["company", "email", "firstName", "lastName", "phone"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
