import time


def current_ms_time() -> int:
    return round(time.time() * 1000)
