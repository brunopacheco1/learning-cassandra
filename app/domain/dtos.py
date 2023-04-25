from dataclasses import dataclass

@dataclass(frozen=True)
class ExceptionResponse:
    message: str
    className: str
    capturedAt: str
