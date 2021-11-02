from m6.bruteforce.scenarioexamples import N_ASSETS, example_daily_generator_5
from m6.bruteforce.sceneriogeneration import portfolio_information_ratio, generate_scenarios
import numpy as np
from pprint import pprint
import time

# There are limitations to a brute force approach ;)


def upside_maximizing_portfolio_shgo(threshold_info:float, **kwargs):
    """
         threshold_info:    Minimum desired information ratio
    """

    def threshold_functional(info):
        return 0.95*max(0,info-threshold_info)+0.05*info

    return info_maximizing_portfolio_shgo(info_functional=threshold_functional,**kwargs)


def info_maximizing_portfolio_shgo(daily_generator, return_type:str, n_days, n_assets, n_trials, n_scenarios, info_functional=None)->([float], dict):
    """
    :param generator:       -> [ float ]  function supplying random vector of daily returns
    :param return_type:     'ari','log','mul'
    :param n_trials:         Approximate number of function evaluations to provide the optimizer
    :param n_assets:         Number of assets in the portfolio
    :param info_functional:  float -> float altering the objective
    :return:   portfolio and optimization metrics
    """
    if n_assets>10:
        print('This might kill SHGO ... try a different optimizer?')

    metrics = dict()
    st = time.time()
    asset_scenarios = generate_scenarios(daily_generator=daily_generator, return_type=return_type, n_days=n_days, n_assets=n_assets, n_scenarios=n_scenarios)
    metrics['scenario generation time'] = time.time()-st
    pprint(metrics)

    global best_info
    global objective_time  # Time spent computing objective function
    best_info = -1000000
    optimization_start_time = time.time()
    objective_time = 0

    def objective(w):
        global objective_time
        global best_info
        st = time.time()
        info = portfolio_information_ratio(w=w, scenarios=asset_scenarios)
        objective_time += time.time()-st
        info_ratio = np.mean(info)
        if info_functional is not None:
            info = info_functional(info)
        if info_ratio>best_info:
            optimizer_time = time.time()-optimization_start_time-objective_time
            metrics.update( {'best weights':w,
                             'information ratio':info_ratio,
                             'objective cpu time':objective_time,
                             'optimizer cpu time':optimizer_time})
            best_info = info_ratio
        return -np.mean(info_ratio)

    from scipy.optimize import shgo  # By all means try others (e.g. see humpday package)

    def g(x):
        # Constraint function. By SHGO convention the constraints are g(x)>=0
        # Since we want sum( |x| ) <= 1,   1- sum( |x| ) >= 0
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.shgo.html
        return 1-sum([abs(xi) for xi in x])

    cons = ({'type': 'ineq', 'fun': g})
    bounds = [(-1,1) for _ in range(N_ASSETS)]
    n_trials_reduced = int(n_trials / 2 + 1)
    n_iters = int(1 + n_trials / 80)
    n = int(5 + n_trials / 40)
    minimizer_kwargs = {'method': 'SLSQP',
                         'max_iter': 5}

    res = shgo(func=objective, n=n, iters=n_iters, bounds=bounds, constraints=cons, options={'maxfev': n_trials_reduced,
                                                                                   'minimize_every_iter': False,
                                                                                   'maxfun': n_trials_reduced,
                                                                                   'minimizer_kwargs': minimizer_kwargs})
    metrics.update({'best info':-res.fun, 'best x':res.x })
    return res.x, metrics

if __name__=='__main__':
    port, metrics = info_maximizing_portfolio_shgo(daily_generator=example_daily_generator_5, return_type='log', n_days=21, n_assets=5, n_scenarios=100000)
    pprint(metrics)
    print(port)