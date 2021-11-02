import math
from sklearn.datasets import make_spd_matrix
import numpy as np
from m6.bruteforce.sceneriogeneration import generate_scenarios, portfolio_log_returns, portfolio_information_ratio



# Crude caching
global sigma_matrix
sigma_matrix = None
global saved_example_scenarios
saved_example_scenarios = None
N_ASSETS = 5
N_DAYS = 21
N_SCENARIOS = 50000
DT = 1/200
SQDT = math.sqrt(DT)
YEARLY = 3.0


def make_example_sigma_matrix_5():
    from datetime import datetime
    day_of_year = datetime.now().timetuple().tm_yday
    return make_spd_matrix(n_dim=N_ASSETS, random_state=day_of_year)


def make_example_sigma_matrix(n_assets):
    from datetime import datetime
    day_of_year = datetime.now().timetuple().tm_yday
    return make_spd_matrix(n_dim=n_assets, random_state=day_of_year)


def example_daily_generator_5(**ignore):
    global sigma_matrix
    if sigma_matrix is None:
        sigma_matrix = make_example_sigma_matrix_5()
    mu = np.array([0 for _ in range(N_ASSETS)])
    log_returns = 0.005*np.random.multivariate_normal(mu, sigma_matrix, 1, check_valid='warn', tol=1e-8)[0]
    return log_returns


def example_daily_generator(n_assets:int):
    sigma_matrix = make_example_sigma_matrix(n_assets)
    mu = np.array([0 for _ in range(n_assets)])
    log_returns = 0.005*np.random.multivariate_normal(mu, sigma_matrix, 1, check_valid='warn', tol=1e-8)[0]
    return log_returns


def example_scenarios():
    global saved_example_scenarios
    if saved_example_scenarios is None:
        scenarios = generate_scenarios(daily_generator=example_daily_generator_5, return_type='log', n_days=N_DAYS, n_scenarios=N_SCENARIOS)
        saved_example_scenarios = example_scenarios
        return scenarios
    else:
        return saved_example_scenarios





if __name__=='__main__':
    print(example_daily_generator_5())
    asset_scenarios = example_scenarios()
    w = [1,0.0,0.0,0.0,0.0]
    port_scenarios = portfolio_log_returns(w=w,scenarios=asset_scenarios)
    print(np.shape(port_scenarios))
    info = portfolio_information_ratio(w=w,scenarios=asset_scenarios)
    print(np.shape(info))
    import matplotlib.pyplot as plt
    plt.hist(info,bins=100)
    plt.show()
