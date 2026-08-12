from enum import StrEnum
from dataclasses import dataclass
from datetime import datetime
import uuid
from typing import Any
from .exceptions import InvalidJobState


class JobStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    DEAD = "dead"


@dataclass
class Job:
    id: uuid.UUID
    type: str
    payload: dict[str, Any]
    status: JobStatus
    available_at: datetime
    worker_id: uuid.UUID

    def __init__(self, status: JobStatus, worker_id: uuid.UUID) -> None:
        self.status = status
        self.worker_id = worker_id

    def claim(self, worker_id: uuid.UUID) -> None:
        if self.status != JobStatus.PENDING:
            raise InvalidJobState()

        self.status = JobStatus.RUNNING
        self.worker_id = worker_id

    def complete(self) -> None:
        if self.status != JobStatus.RUNNING:
            raise InvalidJobState()

        self.status = JobStatus.COMPLETED

    def fail(self) -> None:
        if self.status != JobStatus.RUNNING:  # or JobStatus.COMPLETED ??:
            raise InvalidJobState()

        self.status = JobStatus.FAILED
