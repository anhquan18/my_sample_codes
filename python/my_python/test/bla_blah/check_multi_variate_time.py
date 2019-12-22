from scipy.stats import multivariate_normal
import numpy as np

#likelihood = multivariate_normal(cov=np.diag([1.0, 2.0]))
for i in range(100):
    #print(likelihood.pdf((i, 0.0)))
    print(multivariate_normal(cov=np.diag([1.0, 2.0])).pdf((i,0.0)))
