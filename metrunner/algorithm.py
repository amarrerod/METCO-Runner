from dataclasses import dataclass, field


@dataclass(frozen=True)
class Algorithm:
    name: str
    params: list = field(default_factory=list)
