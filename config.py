import logging
import logging.handlers
import multiprocessing

def worker_configure(name = None, queue = None):
    # formatter = logging.Formatter('[%(asctime)s.%(msecs)03d] [%(filename)s:%(lineno)d] %(levelname)s - %(message)s',
    #                               datefmt='%Y-%m-%d %H:%M:%S')
    
    formatter = logging.Formatter('%(message)s')
    
    
    # print(f"worker configure get current logger : {logging.root.manager.loggerDict}")
    
    if name in logging.root.manager.loggerDict:
        logger = logging.getLogger(name)
        print(f"already have {name} logger, use it directly")
    else:
        print(f" {name} logger do not exist, generating ...")
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        handler = logging.handlers.QueueHandler(queue)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger



def listener_process(queue):
    formatter = logging.Formatter('[%(asctime)s.%(msecs)03d] [%(filename)s:%(lineno)d] %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    file_handler = logging.FileHandler("./test.log")
    file_handler.setFormatter(formatter)
    
    listener = logging.handlers.QueueListener(queue, console_handler, file_handler)
    return listener