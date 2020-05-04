import numpy as np
import pyvttbl as pt
from collections import namedtuple
N = 20
P = [1, 2]
Q = [1, 2, 3]

values = [[998, 511], [1119, 620], [1300, 790]]

sub_id = [i + 1 for i in xrange(N)] * (len(P) * len(Q))
mus = np.concatenate([np.repeat(value, N) for value in values]).tolist()
rt = np.random.normal(mus, scale=112.0, size=N * len(P) * len(Q)).tolist()
iv1 = np.concatenate([np.array([p] * N) for p in P] * len(Q)).tolist()
iv2 = np.concatenate([np.array([q] * (N * len(P))) for q in Q]).tolist()
Sub = namedtuple('Sub', ['Sub_id', 'rt', 'iv1', 'iv2'])
df = pt.DataFrame()

for idx in xrange(len(sub_id)):
    df.insert(Sub(sub_id[idx], rt[idx], iv1[idx], iv2[idx])._asdict())

df.box_plot('rt', factors=['iv1', 'iv2'])