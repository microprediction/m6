from m6.conventions import to_multiple, multiple_to_log_return
import numpy as np


# Generate rank probabilities by brute force from daily generator

def generate_scenarios(daily_generator, n_scenarios, n_assets, n_days=21, return_type='multiple'):
    """
    :param daily_generator:    -> [ float ]      should return vector of returns, or multiples, one for each asset
    :param return_type:str     'arithmetic', 'log', 'multiple', 'ari' ,'arithmetic_return' etc
    :param n_scenarios:
    :param n_days:
    :param n_assets
    :return:
    """
    scenarios = np.ndarray(shape=(n_scenarios,n_days,n_assets))
    for scenario_ndx in range(n_scenarios):
        for day_ndx in range(n_days):
            ret = np.array( daily_generator(n_assets=n_assets) )
            scenarios[scenario_ndx,day_ndx,:] = to_multiple(ret,return_type=return_type)
    return scenarios


def portfolio_log_returns(w, scenarios):
    """
    :param w:
    :param scenarios:   n_days x n_assets x n_scenarios
    :return:
    """
    n_assets = len(w)
    assert n_assets == np.shape(scenarios)[2], 'mismatch in n_assets'
    portfolio_multiples = np.dot(scenarios,w)
    lg_returns = multiple_to_log_return(portfolio_multiples)
    return lg_returns


def portfolio_information_ratio(w,scenarios):
    lg_returns = portfolio_log_returns(w=w,scenarios=scenarios)
    cumulative_lg_returns = np.sum(lg_returns,axis=1)
    lg_return_std = np.std(lg_returns,axis=1)
    return cumulative_lg_returns/(1e-8 + lg_return_std)



if __name__=='__main__':
    try:
        from sklearn.datasets import make_spd_matrix
    except ImportError:
        raise Exception('pip install scikit-learn')
