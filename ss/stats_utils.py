import scipy
import math
import operator
from scipy import stats
from statistics import NormalDist, mean, stdev


def describe_stats(data):
    m = mean(data)
    std = stdev(data)  #already unbiased for N-1
    var = std**2
    print("mean:{:.2f}\nvariance:{:.2f}\nstandard deviation {:.2f}".format(m, var, std))


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
    print("lambda:{0:.2f}".format(lambda_a))
    print("sem:{0:.2f}".format(sem))
    return m - h, m + h


def confidence_interval_t(m, stdd, n, confidence=0.95):
    # sem = stdd / ((n - 1)**.5)
    sem = stdd / ((n)**.5)  #this should be n-1, but oh well
    lambda_a = scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    h = sem * lambda_a
    print("lambda:{0:.2f}".format(lambda_a))
    print("sem:{0:.2f}".format(sem))
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
    print("lambda:{0:.2f}".format(lambda_a))
    print("sem:{0:.2f}".format(sem))
    return p - h, p + h


def two_sample_proportion(p_1, n_1, p_2, n_2, confidence=0.95):
    diff_p = p_1 - p_2
    sem_weighted = math.sqrt(((p_1 * (1 - p_1)) / n_1 + ((p_2 * (1 - p_2)) / n_2)))
    lambda_a = scipy.stats.norm.ppf((1 + confidence) / 2.)
    h = sem * lambda_a
    print("lambda:{0:.2f}".format(lambda_a))
    print("weighted sem:{0:.2f}".format(sem_weighted))
    return -h, h


def two_sample_population(m_1, stdd_1, n_1, m_2, stdd_2, n_2, confidence=0.95):
    # import ipdb
    # ipdb.set_trace()
    diff_m = m_1 - m_2
    if n_1 <= 30 or n_2 <= 30:
        s_p_squared = ((n_1 - 1) * stdd_1**2 + (n_2 - 1) * stdd_2**2) / (n_1 + n_2 - 2)
        lambda_a = scipy.stats.t.ppf((1 + confidence) / 2., n_1 + n_2 - 1)
        sem_weighted = math.sqrt((s_p_squared / n_1) + (s_p_squared / n_2))
    else:
        lambda_a = scipy.stats.norm.ppf((1 + confidence) / 2.)
        sem_weighted = math.sqrt((stdd_1**2) / n_1 + (stdd_2**2) / n_2)
    h = sem_weighted * lambda_a
    return diff_m - h, diff_m + h


def two_sample_population_from_data(data_1, data_2, confidence=0.95):
    m_1, m_2 = mean(data_1), mean(data_2)
    stdd_1, stdd_2 = stdev(data_1), stdev(data_2)
    n_1, n_2 = len(data_1), len(data_2)
    return two_sample_population(m_1, stdd_1, n_1, m_2, stdd_2, n_2, confidence)


def two_sample_dependant_from_data(data_1, data_2, confidence=0.95):
    diff_list = list(map(operator.sub, data_1, data_2))
    m_diff = mean(diff_list)
    stdd_diff = stdev(diff_list)
    n_diff = len(diff_list)
    return confidence_interval(m_diff, stdd_diff, n_diff, confidence)
