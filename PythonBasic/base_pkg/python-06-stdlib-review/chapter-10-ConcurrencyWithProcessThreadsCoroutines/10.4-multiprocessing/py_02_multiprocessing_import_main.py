import multiprocessing
from multiprocessing_import_worker import worker

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(
            target=worker,
            args=(i,)
        )
        jobs.append(p)
        p.start()