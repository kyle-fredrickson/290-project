#!/usr/bin/python3

import numpy as np
import os
import pandas as pd
import sys
import time

THIS_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
DATA_DIR = os.path.join(THIS_DIR,"data")

def many_insecure_mul(s, n):
    r = 1
    for i in range(n):
        m = 1
        for j in s:
            m *= j
        r *= m
    return r

def main():
    n = int(sys.argv[1])
    s = [x for x in range(1, 11)]

    times = []
    for i in range(1, n + 1):
        samples = []
        for j in range(20):
            print("Iteration: %d, Sample %d" % (i,j))
            start = time.time()
            many_insecure_mul(s, 1000)
            end = time.time()
            samples.append(end - start)

        avg = np.average(samples)
        times.append([i, avg])

    data = pd.DataFrame(times, columns=['size', 'time'])
    data.to_csv(os.path.join(DATA_DIR, "insecure_mul.txt"), index=False)

    return 0

if (__name__ == "__main__"):
    main()