from datetime import datetime
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Event:
    timestamp: datetime
    message: str


@dataclass
class Job:
    status: str
    events: List[Event]
    results: str
