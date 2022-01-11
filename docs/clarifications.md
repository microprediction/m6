These are my efforts to clarify the rules. They are not the official rules or official responses. 


## 1. Investment performance

### Question 1(a)

Is the investment portfolio by which intended to be:

 * One large portfolio comprising stocks and ETFS
 * Five portfolios of at most 5 stocks, and another five portfolios of at most 5 ETFs each? 

### Working assumption

It's just one big portfolio with both stocks and ETFs.  

### Resolution:


### Question 1(b)

How are information ratios combined across the overlapping time-periods, and possible portfolios? 

### Working assumption

Denominator and numerator are totalled first, leading to a single information ratio. 

### Question 1(c):

Should the return formula be modified to account for shorts? 

  1 + \sum.   w_i  \left( \frac{S'}{S} - 1 \right) 

We can't collect the -1 unless sum w_i=1 which is not true if there are shorts. 


## 2. Benchark portfolio

### Question:
Why is the benchmark chosen to be the zero portfolio (rather than say, equal positive weights)? The information ratio is undefined at this point. 

### Resolution: 


## 3. Corporate events

## Question(s)

   3a. If a company defaults, will the RET for the day be -1 and 0 thereafter? 

   3b. If a company defaults, will the rank be 1 (or 1.5 if two companies default)? 

   3c. If a company de-lists, will the rank be 1 (or 1.5 if two de-list, etc)? 

   3d. If a company is taken private, will the last recorded stock price persist into the future? 

   3e. If a company is aquired, will the last recorded stock price persist into the future? 

## Working assumption:

As inferred from the questions. 

## 4. Dividends

### Question

Do the prices used include dividends?

### Working assumption

Yes, and pretty clearly indicated by the wording "total return". Same for stock splits. 


## Rounding

At present the rules state that submissions not summing to unity will be disqualified. However this is a set of measure zero. In theory it is still a proper scoring rule without the constraint so one might wonder if it is necessary at all. 

### Question

What is the tolerance for sum of probabilities? 

### Resolution

Five decimal places. 





