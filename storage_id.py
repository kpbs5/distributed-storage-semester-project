from dataclasses import dataclass
import uuid
from functools import total_ordering

@total_ordering
@dataclass
class StorageId:
    """StorageId is a unique identifier for a storage replica."""
    uid: uuid.UUID
    stripe_index: int
    replica_index: int
    delimiter: str = "."

    def __str__(self) -> str:
        return f"{self.uid}{self.delimiter}{self.stripe_index}{self.delimiter}{self.replica_index}"

    def __repr__(self) -> str:
        return f"{str(self.uid)[:8]}{self.delimiter}{self.stripe_index}{self.delimiter}{self.replica_index}"

    @staticmethod
    def from_string(s: str) -> "StorageId":
        uid, stripe_index, replica_index = s.split(StorageId.delimiter)
        return StorageId(uid=uuid.UUID(uid), stripe_index=int(stripe_index), replica_index=(replica_index))

    def __eq__(self, other: "StorageId") -> bool:
        assert isinstance(other, StorageId), f"Cannot compare StorageId with {type(other)}"
        return self.uid == other.uid and self.stripe_index == other.stripe_index and self.replica_index == other.replica_index

    def __lt__(self, other: "StorageId") -> bool:
        assert isinstance(other, StorageId), f"Cannot compare StorageId with {type(other)}"
        assert self.uid == other.uid, f"Cannot compare StorageId with different uid: {self.uid} != {other.uid}"
        return self.stripe_index < other.stripe_index
        