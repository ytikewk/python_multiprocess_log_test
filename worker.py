import time
import logging
import config
import test_module

log = logging.getLogger("worker")

def worker_process(worker_test):
    while(True):
        log.info(worker_test)
        test_module.test()
        time.sleep(1)