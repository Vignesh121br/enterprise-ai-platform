import time

from fastapi import Request


async def request_timer(request: Request, call_next):

    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start

    response.headers["X-Process-Time"] = str(round(process_time, 4))

    return response
