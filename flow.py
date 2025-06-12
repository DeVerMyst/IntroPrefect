import os
from random import random
from prefect import flow, task
from prefect.logging import get_run_logger

#    • PYTHONIOENCODING  : évite les UnicodeDecodeError sous Windows
#    • PREFECT_API_URL   : indique au SDK où se trouve l’API Prefect
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
os.environ.setdefault("PREFECT_API_URL", "http://127.0.0.1:4200/api")

@task(retries=2, retry_delay_seconds=1)
def check_random():
    log = get_run_logger()
    r = random()
    if r < 0.5:
        log.warning(f"{r:.3f} ➜ retrain")
        raise ValueError("retry")
    log.info(f"{r:.3f} ➜ ok")

@flow
def periodic_check():
    log = get_run_logger()
    log.info("🔄 nouveau run")
    check_random()

if __name__ == "__main__":
    periodic_check.serve(
        name="every-10s",
        interval=10          # exécution toutes les 10 s
    )



