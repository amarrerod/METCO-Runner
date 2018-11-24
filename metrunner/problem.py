from dataclasses import dataclass, field


@dataclass(frozen=True)
class Problem:
    name: str
    args: list = field(default_factory=list)
