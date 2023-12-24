from dataclasses import dataclass

@dataclass
class User:
    id_: int
    email: str
    isAdmin: bool