#!/usr/bin/python3

from mpyc.runtime import mpc
import numpy as np
import os
import pandas as pd
import sys
import time

THIS_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
DATA_DIR = os.path.join(THIS_DIR,"data")
DATA_PATH = os.path.join(DATA_DIR, "secure_mul.txt")

secint = mpc.SecInt(64)

@mpc.coroutine
async def many_secure_mul(s, n):
    await mpc.returnType(secint)
    r = secint(1)
    for i in range(n):
        m = secint(1)
        for j in s:
            m *= j
        r *= m
    return r


def main():
    data = pd.read_csv(DATA_PATH)

    mpc.run(mpc.start())

    n = len(mpc.parties)
    s = [secint(x) for x in range(1, 11)]

    samples = []
    for j in range(20):
        #s = [secint(x) for x in range(1, n + 1)]
        print("Iteration: %d, Sample %d" % (n,j))
        start = time.time()
        mpc.run(mpc.output(many_secure_mul(s, 100)))
        end = time.time()
        samples.append(end - start)

    mpc.run(mpc.shutdown())

    avg = np.average(samples)
    data.loc[data.shape[0]] = [n, avg]
    data.to_csv(DATA_PATH, index=False)

    return 0

if (__name__ == "__main__"):
    main()