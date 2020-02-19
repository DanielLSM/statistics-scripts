import scipy
from scipy import stats
from statistics import NormalDist, mean, stdev


def describe_stats(data):
    m = mean(data)
    std = stdev(data)  #already unbiased for N-1
    var = std**2
    print("mean:{}\nvariance:{}\nstandard deviation {}".format(m, var, std))


#using n-1 for the time being for the standord error of the mean
# def confidence_interval_normal_data(m, stdd, n, confidence=0.95):
#     dist = NormalDist.from_samples(data)
#     z_area = NormalDist().inv_cdf((1 + confidence) / 2.)
#     h = dist.stdev * z / ((n - 1)**.5)
#     return m - h, m + h


def confidence_interval_normal(m, stdd, n, confidence=0.95):
    sem = stdd / ((n)**.5)
    lambda_a = scipy.stats.norm.ppf((1 + confidence) / 2.)
    h = sem * lambda_a
    print("lambda:{}".format(lambda_a))
    print("sem:{}".format(sem))
    return m - h, m + h


def confidence_interval_t(m, stdd, n, confidence=0.95):
    # sem = stdd / ((n - 1)**.5)
    sem = stdd / ((n)**.5)  #this should be n-1, but oh well
    lambda_a = scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    h = sem * lambda_a
    print("lambda:{}".format(lambda_a))
    print("sem:{}".format(sem))
    return m - h, m + h


def confidence_interval(m, stdd, n, confidence=0.95):
    if n <= 30:
        lower_bound, upper_bound = confidence_interval_t(m, stdd, n, confidence)
    else:
        lower_bound, upper_bound = confidence_interval_normal(m, stdd, n, confidence)
    return lower_bound, upper_bound


def confidence_interval_from_data(data, confidence=0.95):
    m = mean(data)
    stdd = stdev(data)
    n = len(data)
    return confidence_interval(m, stdd, n)


def one_sample_prop_proportion(p, n, confidence=0.95):
    sem = ((p * (1 - p)) / n)**.5
    lambda_a = scipy.stats.norm.ppf((1 + confidence) / 2.)
    h = sem * lambda_a
    print("lambda:{}".format(lambda_a))
    print("sem:{}".format(sem))
    return p - h, p + h