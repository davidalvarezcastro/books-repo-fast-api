from __future__ import annotations

import os


def _get_value_from_env_key(key: str):
    value = os.getenv(key, None)

    if value is None:
        raise ValueError(f"Enviroment key {key} is not defined!")

    return value
