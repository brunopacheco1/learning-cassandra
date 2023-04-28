from datetime import datetime
from app.dtos import ExceptionResponse
from fastapi import status
from fastapi.responses import JSONResponse
import dataclasses

def default_exception_handler(status_code: int, exception: Exception):
    return JSONResponse(
        status_code=status_code,
        content=dataclasses.asdict(
            ExceptionResponse(
                message=str(exception), 
                className=exception.__class__.__name__,
                capturedAt=datetime.now().isoformat(),
            )
        )
    )

async def bad_request_exception_handler(request, exception: Exception):
    return default_exception_handler(
        status_code=status.HTTP_400_BAD_REQUEST,
        exception=exception,
    )

async def not_found_exception_handler(request, exception: Exception):
    return default_exception_handler(
        status_code=status.HTTP_404_NOT_FOUND,
        exception=exception,
    )

async def generic_exception_handler(request, exception: Exception):
    return default_exception_handler(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        exception=exception,
    )
