from ss.stats_utils import frequency_hypothesis_chisquare
from scipy.stats.distributions import chi2
import itertools

obs_1_cover = [81, 60, 182]
obs_2_cover = [78, 93, 95]
obs_3_cover = [241, 247, 123]
f_expected = [1 / 3, 1 / 3, 1 / 3]

categorical_obs = [obs_1_cover, obs_2_cover, obs_3_cover]

assert round(sum(f_expected), 6) == 1.0

expected_1_cover = [round(sum(obs_1_cover) * i, 2) for i in f_expected]
expected_2_cover = [round(sum(obs_2_cover) * i, 2) for i in f_expected]
expected_3_cover = [round(sum(obs_3_cover) * i, 2) for i in f_expected]

categorical_expected = [expected_1_cover, expected_2_cover, expected_3_cover]

obs = list(itertools.chain(*categorical_obs))
expected = list(itertools.chain(*categorical_expected))

print("obs: {}".format(obs))
print("expected: {}".format(expected))
ddof = (len(categorical_obs) - 1) * (len(categorical_expected) - 1)
statistic = frequency_hypothesis_chisquare(obs, expected, ddof=ddof)
print("statistic is: {}".format(round(statistic[0], 2)))
crit_statistic = chi2.ppf(0.95, df=ddof)
print("degrees of freedom: {}".format(ddof))
print("For area=0.05, X is {}".format(round(crit_statistic, 2)))
if statistic[0] > crit_statistic:
    print("We can reject the hypothesis H0")
else:
    print("Hypothesis H0 can not be rejected")
