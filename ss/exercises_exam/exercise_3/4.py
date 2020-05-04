from ss.stats_utils import frequency_hypothesis_chisquare
from scipy.stats.distributions import chi2
import itertools

obs_yes = [43, 81]
obs_no = [157, 119]
f_expected = [1 / 2, 1 / 2]

categorical_obs = [obs_yes, obs_no]

assert round(sum(f_expected), 1) == 1.0

expected_yes = [round(sum(obs_yes) * i, 2) for i in f_expected]
expected_no = [round(sum(obs_no) * i, 2) for i in f_expected]

categorical_expected = [expected_yes, expected_no]

obs = list(itertools.chain(*categorical_obs))
expected = list(itertools.chain(*categorical_expected))

print("obs: {}".format(obs))
print("expected: {}".format(expected))
ddof = (len(categorical_obs) - 1) * (len(categorical_expected) - 1)
statistic = frequency_hypothesis_chisquare(obs, expected, ddof=ddof)
print("statistic is: {}".format(round(statistic[0], 2)))
crit_statistic = chi2.ppf(0.99, df=ddof)
print("degrees of freedom: {}".format(ddof))
print("For area=0.05, X is {}".format(round(crit_statistic, 2)))
if statistic[0] > crit_statistic:
    print("We can reject the hypothesis H0")
else:
    print("Hypothesis H0 can not be rejected")
