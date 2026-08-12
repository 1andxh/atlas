from .job import JobStatus


class JobException(Exception):
    """Base exception for all job exceptions"""

    error_code: str = "JOB_FAILED"

    def __init__(self, message: str, error_code: str | None, status: JobStatus) -> None:
        self.message = message
        self.error_code = error_code or self.error_code
        self.status = status
        super().__init__(message)


class InvalidJobState(JobException):
    """Raised when job state in invalid"""

    error_code = "INVALID_JOB_STATE"

    def __init__(
        self, status: JobStatus, message: str = "Cannont complete job in"
    ) -> None:
        super().__init__(message)
