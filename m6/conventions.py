import math
import numpy as np
from numpy import where

# Non-annualized quantities


def arithmetic_to_multiple(arithmetic_return):
    return arithmetic_return+1


def multiple_to_arithmetic_return(multiple):
    return multiple-1


def multiple_to_log_return(multiple):
    return where(multiple!=0,np.log(multiple),-np.inf)


def arithmetic_to_log_return(arithmetic_return):
    return multiple_to_log_return(arithmetic_to_multiple(arithmetic_return))


def log_return_to_multiple(continous_return):
    return where(continous_return>-np.inf,np.exp(continous_return),0)


def to_multiple(r, return_type:str):
    rt = return_type.lower().split('_')[0][:3]
    if rt =='ari':
        return multiple_to_arithmetic_return(r)
    elif return_type=='log':
        return log_return_to_multiple(r)
    elif return_type=='mul':
        return r







if __name__=='__main__':
    arithmetic_return = 0.05
    print(arithmetic_to_log_return(arithmetic_return))
    arithmetic_return = np.array([0.05, 0.02])
    print(arithmetic_to_log_return(arithmetic_return))
    print(multiple_to_log_return(0))


