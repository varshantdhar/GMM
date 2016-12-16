from scipy.special import psi, gammaln
import numpy as np

import autograd.numpy as agnp
import autograd.scipy.special as agscipy 

def dirichlet_expectation(alpha):
    if len(alpha.shape) == 1:
        return psi(alpha + np.finfo(np.float32).eps) - psi(np.sum(alpha))
    return psi(alpha) - psi(np.sum(alpha, 1))[:, np.newaxis]

def exp_normalize(aux):
    return (np.exp(aux-np.max(aux))+ np.finfo(np.float32).eps)/(np.sum(np.exp(aux-np.max(aux))+np.finfo(np.float32).eps))

def log_beta_function(x):
    return np.sum(gammaln(x + np.finfo(np.float32).eps))-gammaln(np.sum(x + np.finfo(np.float32).eps))


def ag_dirichlet_expectation(alpha):
    if len(alpha.shape) == 1:
        return agscipy.psi(alpha + agnp.finfo(np.float32).eps) - agscipy.psi(agnp.sum(alpha))
    return agscipy.psi(alpha) - agscipy.psi(agnp.sum(alpha, 1))[:, agnp.newaxis]

def ag_log_beta_function(x):
    return agnp.sum(agscipy.gammaln(x + agnp.finfo(np.float32).eps))-agscipy.gammaln(agnp.sum(x + agnp.finfo(np.float32).eps))
