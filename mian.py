# this test mainly focus on using logging module in multi process scenario
# the baisc idea is put all the worker log into multiprocess.queue, 
# then set a listener process to output the log


import logging
import config 
import multiprocessing
import time


from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler 
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor



def scheduler_test(info):
    log.info(info)


def start_worker(queue):
    log = config.worker_configure("worker", queue)
    import worker
    log.info("Starting worker")
    worker.worker_process("worker_test")



def main_worker():
    pass
    # while(True):
    #     log.info("")
    
    
if __name__ == "__main__":
    log_queue = multiprocessing.Queue(-1)
    log = config.worker_configure("worker", log_queue)
    
    log_listener = config.listener_process(log_queue)
    log_listener.start()
    # log_listener.join()
    
    log.info("test")
    print(log_queue.qsize())
    # time.sleep(1)
    
    # while (True):
    #     log.info("test")
    #     time.sleep(1)
    # while(log_queue.qsize()>0):
    #     continue
    
    p = multiprocessing.Process(target=start_worker, args=(log_queue,))
    p.start()
    
    scheduler = BlockingScheduler()

    # send test every 5s
    scheduler.add_job(scheduler_test, 'interval', seconds=5, args=("scheduler_test",))
    # start scheduler and block the process
    scheduler.start()