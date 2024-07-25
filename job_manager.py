from datetime import datetime
from dataclasses import dataclass
from typing import List, Dict
from threading import Lock


@dataclass
class Event:
    timestamp: datetime
    message: str


@dataclass
class Job:
    status: str
    events: List[Event]
    results: str


jobs_lock = Lock()
jobs: Dict[str, Job] = {}


def append_event(job_id: str, event_data: str):
    with jobs_lock:
        if job_id not in jobs:
            print(f"Starting Job: {job_id}")
            jobs[job_id] = Job(
                status="STARTED",
                events=[],
                results="",
            )

        else:
            print(f"Appending event to Job: {job_id}")
            jobs[job_id].events.append(
                Event(
                    timestamp=datetime.now(),
                    message=event_data,
                )
            )
