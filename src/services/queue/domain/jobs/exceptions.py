from .job import JobStatus


class JobException(Exception):
    """Base exception for all job exceptions"""

    error_code: str = "JOB_FAILED"

    def __init__(
        self,
        message: str,
        error_code: str | None = None,
    ) -> None:
        self.message = message
        self.error_code = error_code or self.error_code
        super().__init__(message)


class InvalidJobState(JobException):
    """Raised when job state in invalid"""

    error_code: str = "INVALID_JOB_STATE"

    def __init__(self, message: str = "Cannont complete job in current state") -> None:
        super().__init__(message)
