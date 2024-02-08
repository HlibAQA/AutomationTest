from dataclasses import dataclass


@dataclass
class Names:
    fullName: str = None
    firstName: str = None
    lastName: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    currentAddress: str = None
    permanentAddress: str = None
