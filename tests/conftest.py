import pytest
from src.services.queue.domain.jobs.job import Job, JobStatus
import uuid
from datetime import datetime


@pytest.fixture()
def make_job():
    id = uuid.uuid4()
    type = "some_type"
    payload = {"create": 1}
    status = JobStatus.PENDING
    available_at = datetime.now()
    worker_id = uuid.uuid4()

    job = Job(
        id=id,
        type=type,
        payload=payload,
        status=status,
        available_at=available_at,
        worker_id=worker_id,
    )
