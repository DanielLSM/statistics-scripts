from scipy import stats
from statistics import NormalDist


def confidence_interval_normal(data, confidence=0.95):
    a = 1.0 * data
    n = len(a)
    dist = NormalDist.from_samples(data)
    z = NormalDist().inv_cdf((1 + confidence) / 2.)
    h = dist.stdev * z / ((n - 1)**.5)
    return dist.mean - h, dist.mean + h


def confidence_interval_t(data, confidence=0.95):
    a = 1.0 * data
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    return dist.mean - h, dist.mean + h


def confidence_interval(data, confidence_interval=0.95):
    if len(data) <= 30:
        lower_bound, upper_bound = confidence_interval_t(data, confidence_interval)
    else:
        lower_bound, upper_bound = confidence_interval_normal(data, confidence_interval)
