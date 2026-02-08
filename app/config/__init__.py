from functools import lru_cache
from .base import Settings
from pathlib import Path
import os


@lru_cache(maxsize=1)
def get_settings():
    env = os.getenv("ENV", False)
    print(env)
    current = Path(__file__).parent
    root_dir = current.parent.parent
    if env:
        env_file = root_dir / f".env.{env}"
    else:
        env_file = root_dir / ".env"
    return Settings(_env_file=env_file, _env_file_encoding='utf-8')


settings = get_settings()
print(settings.model_dump())
