from dataclasses import dataclass


@dataclass(frozen=True)
class Escort:
    userId: int


@dataclass(frozen=True)
class Status:
    status: str
    escort: Escort


class ServiceRequest:
    def __init__(self):
        self.status = "Pending"

    def getService(self) -> "ServiceRequest":
        return self

    def acceptService(self, escort: Escort) -> Status:
        self.status = "Accepted"
        return Status(self.status, escort)

    def denyService(self, escort: Escort) -> None:
        self.status = "Declined"
