from src.services.queue.domain.jobs.job import JobStatus
from src.services.queue.domain.jobs.exceptions import InvalidJobState

import uuid
import pytest


def test_pending_job_can_be_claimed(create_job):
    job = create_job()

    worker_id = uuid.uuid4()
    job.claim(worker_id)

    assert job.status == JobStatus.RUNNING
    assert job.worker_id == worker_id


def test_running_job_can_complete(create_job):
    job = create_job()

    worker_id = uuid.uuid4()

    assert job.status == JobStatus.PENDING
    job.claim(worker_id)

    assert job.status == JobStatus.RUNNING
    job.complete()

    assert job.status == JobStatus.COMPLETED


def test_pending_job_cannot_complete(create_job):
    job = create_job()

    with pytest.raises(InvalidJobState):
        job.complete()


def test_job_cannot_be_claimed_again(create_job):
    job = create_job()

    worker_id = uuid.uuid4()
    job.claim(worker_id)

    job.complete()

    with pytest.raises(InvalidJobState):
        job.claim(worker_id)
