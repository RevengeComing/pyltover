from pydantic import BaseModel


class ErrorStatus(BaseModel):
    message: str
    status_code: int


class RiotAPIError(Exception):
    def __init__(self, error_status):
        self.error_status: ErrorStatus = error_status


def translate_error(json_body):
    return RiotAPIError(
        ErrorStatus(
            message=json_body["status"]["message"],
            status_code=json_body["status"]["status_code"],
        )
    )
