import time

from fastapi import FastAPI


# app = FastAPI()
#
# uvicorn / gunicorn / ...


def temp(i: int):
    print(i)
    time.sleep(10000)
