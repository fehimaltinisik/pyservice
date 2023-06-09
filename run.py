import os
import uvicorn


APP_HOST = os.environ.get("APP_HOST") or "0.0.0.0"
APP_LOG_LEVEL = os.environ.get("APP_LOG_LEVEL", "debug") or "debug"
APP_RELOAD = bool(int(os.environ.get("APP_RELOAD", "0"))) or False


if __name__ == '__main__':
    uvicorn.run(app="src.main:app", host=APP_HOST, port=8000, log_level=APP_LOG_LEVEL, reload=APP_RELOAD)
