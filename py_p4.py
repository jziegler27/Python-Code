import math as m, multiprocessing as mp, time, sys, signal
def checker(lo, hi, que):
    count = 0
    for num in range(lo, hi+1):
        if m.sqrt(m.sqrt(num)) % 1 > .93:
            count += 1
    que.put(count)


def main():
    signal.alarm(120)
    procs = []
    q = mp.Queue(0)
    low = int(sys.argv[1])
    high = int(sys.argv[2])
    n = int(sys.argv[3])
    chunk = int((high-low)/n)
    for i in range(n):
        p = mp.Process(target=checker, args=(i*chunk+low, i*chunk+low+chunk, q))
        procs.append(p)
    starttime = time.time()
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    endtime = time.time()    
    total = 0
    for value in range(n):
        total += q.get()
    print("%0.2f" % (endtime - starttime), total)


if __name__ == "__main__":
    main()





