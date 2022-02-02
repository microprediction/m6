# m6

Some resources related to the M6-Forecasting competition. 

### Official rules & contest site

- [Contest site](https://mofc.unic.ac.cy/the-m6-competition/)
- [Rules](https://github.com/microprediction/m6/blob/main/docs/M6-forecasting-competition-Guidelines-20210908.pdf) as of Oct 7, 2021
- [Rule clarifications](https://github.com/microprediction/m6/blob/main/docs/clarifications.md)


### Example entries, and scripts 
See [precise/examples_m6](https://github.com/microprediction/precise/blob/main/examples_m6)

    from precise.skatertools.m6.competition import m6_competition_entry
    df = m6_competition_entry()

This will choose from dozens of different ways of estimating cov, and from a dozen different portfolio construction methods.  

See also [precise/examples_m6/full](https://github.com/microprediction/precise/tree/main/examples_m6/full) for example .csv's to modify as you see fit. 


### Related literatures 
A couple of bibliographies:

 - [precise/LITERATURE.md](https://github.com/microprediction/precise/blob/main/LITERATURE.md) 
 - [precise/Refs](https://github.com/microprediction/precise/blob/main/Refs%20with%20abstracts_Covariances_Correlations_Vols-2022.pdf) 

### My articles on M6 contest 

- [How to train for the M6 Financial Foreasting Competition](https://microprediction.medium.com/six-ways-to-train-for-the-m6-financial-forecasting-competition-cacaf3af58b5)
- [The future of forecasting competitions, according to the experts](https://www.microprediction.com/blog/future)


### Python time-series packages 
Need to forecast something? 

- [Listing](https://www.microprediction.com/blog/popular-timeseries-packages) of popular Python time-series packages, including features, causality and so forth.
- [Elo ratings](https://microprediction.github.io/timeseries-elo-ratings/html_leaderboards/overall.html) of autonomous time-series prediction algorithms judged against live data. 

Note that the Elo ratings contain a "special" category that might be particularly relevant to M6. 

### Live contests to practice on 

Some of the [live streams](https://www.microprediction.org/browse_streams.html) at Microprediction.Org are good fodder for predicting volatilities, covariances, et cetera. See in particular: 

- Crypto streams described [here](https://github.com/microprediction/microprediction/blob/master/stream_examples_crypto/README.md)
- Anything starting with 'fathom' in this list [here](https://www.microprediction.org/browse_streams.html)
- See the [daily $125 contest](https://www.microprediction.com/competitions/daily) for short-term distributional prediction of crypto-currencies and stocks, including variances and co-variances, et cetera. 


### Random data to practice on 

- [Public API](https://www.microprediction.com/public-api) for time-series
- Example [csv](https://csv.microprediction.org/lagged?name=electricity-fueltype-nyiso-hydro.json)
- [Tutorial](https://www.microprediction.com/python-3) on retrieving time-series data using microprediction package. 
- [IEX](https://iexcloud.io/docs/api/) API and [example scripts](https://github.com/numerai/signals-example-scripts/blob/master/iexcloud/dividends.py) from Numerai

### Analytical tools for 5-way rank probabilities ... for the M6 contest that wasn't :)
Ah well, in the first draft of this contest we were to rank 5 stocks 1..5. That's no longer the case. However:

- Paper soon. See [notebook examples](https://github.com/microprediction/m6/tree/main/notebook_examples) 







This site maintained by yours truly, an employee of one of [Intech Investments](https://www.intechinvestments.com/). Code is provided subject to the MIT License (and all disclaimers therein). Nothing here should be construed as investment advice, or even contest entry advice. Always refer to the official rules. 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

