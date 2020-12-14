import numpy as np
import os
import pandas as pd
from Pyfhel import PyCtxt, PyPtxt, Pyfhel
import sys
import time

THIS_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
DATA_DIR = os.path.join(THIS_DIR,"data")

HE = Pyfhel()
HE.contextGen(p=65537)
HE.keyGen()

def fh_add(s, n):
    r = HE.encryptInt(0)
    for i in range(n):
        m = HE.encryptInt(0)
        for j in s:
            m = m + HE.encryptInt(j)
        r = r + m
    r = HE.decryptInt(r)
    return r

def main():
    n = int(sys.argv[1])
    s = [x for x in range(1, 11)]

    times = []
    for i in range(1, n + 1):
        samples = []
        for j in range(20):
            #s = [x for x in range(1, i + 1)]
            print("Iteration: %d, Sample %d" % (i,j))
            start = time.time()
            fh_add(s, 100)
            end = time.time()
            samples.append(end - start)

        avg = np.average(samples)
        times.append([i, avg])

    data = pd.DataFrame(times, columns=['size', 'time'])
    data.to_csv(os.path.join(DATA_DIR, "fh_add.txt"), index=False)

    return 0


if (__name__ == "__main__"):
    main()