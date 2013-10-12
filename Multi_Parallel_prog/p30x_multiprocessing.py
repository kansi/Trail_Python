
import multiprocessing

def worker():
    print 'Worker'
    return

jobs = []
for i in range(5):
    p = multiprocessing.Process(name='Worker', target=worker)
    jobs.append(p)
    p.start()
