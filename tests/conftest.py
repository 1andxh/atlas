import pytest
from src.services.queue.domain.jobs.job import Job, JobStatus
import uuid
from datetime import datetime


@pytest.fixture()
def create_job():
    return Job(
        id=uuid.uuid4(),
        type="some_type",
        payload={"create": 1},
        status=JobStatus.PENDING,
        available_at=datetime.now(),
        # worker_id=None,
    )
