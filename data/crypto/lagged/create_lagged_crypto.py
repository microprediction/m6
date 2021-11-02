# pip install microprediction


if __name__=='__main__':
    import os
    import pandas as pd
    import csv
    from microprediction import MicroReader
    from pprint import pprint

    DELAY = 3555  # Roughly one hour ahead
    mr = MicroReader()
    c5_names = ['c5_bitcoin.json', 'c5_ethereum.json', 'c5_iota.json', 'c5_cardano.json', 'c5_ripple.json']
    import itertools

    c5_triples = list()
    for L in range(0, len(c5_names) + 1):
        for subset in itertools.combinations(c5_names, L):
            if len(subset) == 3:
                z3_name = mr.zcurve_name(names=subset, delay=DELAY)
                c5_triples.append(z3_name)

    all_lagged_values = dict([(name, mr.get_lagged_copulas(name=name)) for name in c5_triples])

    for name,lagged in all_lagged_values.items():
         csv_name = __file__.replace('create_lagged_crypto.py',name.replace('.json','.csv'))
         with open(csv_name, 'w', newline='') as csvfile:
             wrtr = csv.writer(csvfile, delimiter=',',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
             for row in lagged:
                 wrtr.writerow(row)
