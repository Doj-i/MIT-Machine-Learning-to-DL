import scipy.special

x = scipy.special.comb(31000, 63)
y = 0.00203**63
z = (1-0.00203)**(31000-63)
print(x*y*z)
print(scipy.stats.binom.ppf(0.05, 31000, 0.00203))

