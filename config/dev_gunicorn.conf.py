# bind = "0.0.0.0:7000"
bind = "127.0.0.1:7000"
# bind = 'unix:///tmp/nginx.socket'
workers = 1
# worker_class = "uvicorn.workers.UvicornWorker"
preload_app = True


def when_ready(server):
    print('---------- READY -----------------')
    # open('/tmp/app-initialized', 'w').close()


def post_fork(server, worker):
    print('---------- POST FORK -----------------')


def post_worker_init(worker):
    print('---------- POST WORKER INIT -----------------')