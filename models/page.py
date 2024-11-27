from dataclasses import dataclass
import time

@dataclass
class Page:
    page_number: int
    reference_count: int = 0
    last_accessed_time: float = field(default_factory=time.time)
