from src.services.queue.domain.jobs.job import Job, JobStatus, JobDomain
from src.services.queue.domain.jobs.exceptions import InvalidJobState

import uuid


def test_pending_job_can_be_claimed(make_job):
    job = make_job()

    job.claim(uuid.uuid4())

    assert job.status == JobStatus.RUNNING
    assert job.worker_id == "worker-1"


def test_running_job_can_complete(make_job):
    job = make_job()

    job.claim(uuid.uuid4())

    assert job.status == JobStatus.COMPLETED


def test_pending_job_cannot_complete(make_job):
    job = make_job()

    with pytest.raises(InvalidJobState):
        job.complete()


def test_job_cannot_be_claimed_again(make_job):
    job = make_job()

    job.claim(uuid.uuid4())
    job.complete()

    with pytest.raises(InvalidJobState):
        job.claim(uuid.uuid4())
