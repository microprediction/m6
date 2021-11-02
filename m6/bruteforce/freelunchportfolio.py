from m6.bruteforce.scenarioexamples import N_ASSETS, example_daily_generator
from m6.bruteforce.sceneriogeneration import portfolio_information_ratio, generate_scenarios
import numpy as np
from pprint import pprint
import time
import math


# There are limitations to a brute force approach ;)


FREELUNCH_METHODS = ['DE','SADE','PSO','KrillHerd','SA']

def upside_maximizing_portfolio_freelunch(threshold_info:float, **kwargs):
    """
         threshold_info:    Minimum desired information ratio
    """

    def threshold_functional(info):
        return 0.95*max(0,info-threshold_info)+0.05*info

    return info_maximizing_portfolio_freelunch(info_functional=threshold_functional,**kwargs)


def info_maximizing_portfolio_freelunch(daily_generator, return_type:str, n_days, n_assets, n_trials, n_scenarios, info_functional=None, method='sa', n_pop=21)->([float], dict):
    """
    :param generator:       -> [ float ]  function supplying random vector of daily returns
    :param return_type:     'ari','log','mul'
    :param n_trials:         Approximate number of function evaluations to provide the optimizer
    :param n_assets:         Number of assets in the portfolio
    :param info_functional:  float -> float altering the objective
    :param method            Sub-method in the freelunch library
    :param n_pop             Population size parameter required by freelunch library
    :return:   portfolio and optimization metrics
    """
    try:
        import freelunch
    except ImportError:
        raise ImportError('pip install freelunch')

    metrics = dict()
    st = time.time()
    print('Generating samples')
    asset_scenarios = generate_scenarios(daily_generator=daily_generator, return_type=return_type, n_days=n_days, n_assets=n_assets, n_scenarios=n_scenarios)
    metrics['scenario generation time'] = time.time()-st
    pprint(metrics)

    print('Staring optimization')
    global best_info
    global objective_time  # Time spent computing objective function
    best_info = -1000000
    optimization_start_time = time.time()
    objective_time = 0

    def soft_penalty(w):
        sum_abs = sum([abs(wi) for wi in w])
        penalty = 10000*max(0,sum_abs-1)
        return penalty

    def objective(w):
        global objective_time
        global best_info
        st = time.time()
        info = portfolio_information_ratio(w=w, scenarios=asset_scenarios)
        objective_time += time.time()-st
        if info_functional is not None:
            info = info_functional(info)

        unpenalized_info = np.mean(info)
        mean_info = unpenalized_info - soft_penalty(w)
        if mean_info>best_info:
            optimizer_time = time.time()-optimization_start_time-objective_time
            metrics.update( {'best weights':w,
                             'sum |w|':sum([abs(wi) for wi in w]),
                             'unpenalized info ratio':unpenalized_info,
                             'penalized ratio':mean_info,
                             'objective cpu time':objective_time,
                             'optimizer cpu time':optimizer_time})
            best_info = mean_info
        return -mean_info

    optimizer = getattr(freelunch, method)(obj=objective, bounds=[[-1, 1]] * n_assets)

    if method.lower() in ['de', 'sade', 'pso', 'krillherd']:
        n_gens = int(math.ceil(n_trials / n_pop))
        optimizer.hypers['N'] = n_pop  # population size
        optimizer.hypers['G'] = n_gens  # number of generations
    if method.lower() in 'sa':
        n_gens = int(math.ceil(n_trials / n_pop))
        optimizer.hypers['N'] = n_pop  # population size
        optimizer.hypers['K'] = n_gens  # number of generations

    runs = optimizer(nruns=1, full_output=True)  # instance and run
    best_val = runs['scores'][0]  # all obj scores are sorted low to high
    best_x = runs['solutions'][0]  # corresponding inputs
    feval_count_comparison = runs['nfe']  # function evaluations

    metrics.update({'best info':-best_val, 'best x':best_x })

    # Soft penalty may not be enough
    sum_abs = sum([abs(xi) for xi in best_x])
    if sum_abs>1:
        best_x = [ xi/sum_abs for xi in best_x]

    return best_x, metrics

if __name__=='__main__':
    port, metrics = info_maximizing_portfolio_freelunch(daily_generator=example_daily_generator, return_type='log', n_days=21, n_assets=500,
                                                        n_scenarios=1000000, method='SA', n_pop=21, n_trials=50000)
    pprint(metrics)
