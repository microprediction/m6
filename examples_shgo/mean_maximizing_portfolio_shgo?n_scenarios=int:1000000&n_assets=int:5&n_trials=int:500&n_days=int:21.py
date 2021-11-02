from runthis import parse_kwargs
from m6.bruteforce.shgoportfolio import info_maximizing_portfolio_shgo
from m6.bruteforce.scenarioexamples import example_daily_generator_5
from pprint import pprint
import json

if __name__=='__main__':
    import os
    this_file = __file__.split(os.path.sep)[-1]
    kwargs = parse_kwargs(this_file)
    pprint(kwargs)
    out_file = this_file.replace('.py','_result.json')
    port, metrics = info_maximizing_portfolio_shgo(daily_generator=example_daily_generator_5, return_type='log', **kwargs)
    with open(out_file,'wt') as fp:
        metrics.update({'portfolio':port})
        json.dumps(fp=fp,obj=metrics)

