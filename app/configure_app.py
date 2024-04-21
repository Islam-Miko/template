from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from core.cache.connection import close_redis, init_redis
from fastapi import FastAPI



@asynccontextmanager
async def lifespan(app_: FastAPI) -> AsyncGenerator:
    await init_redis()
    yield
    await close_redis()