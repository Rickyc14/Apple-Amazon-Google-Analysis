# Apple-Amazon-Google-Analysis

Very few companies can match the influence these three possess. They are the trend-makers always trying to stay ahead of the curve, and despite not being immune to changes in the economic environment, they managed to thrive during all these years.<br>

The archive above contains plot images, <em>xlsx</em> files with the data used in this project, and source code files for both Python and R. The data was obtained from [Yahoo finance](https://finance.yahoo.com/) using the [R software](https://www.r-project.org/).<br><br>
<ul>
<li>  
This is a common data pattern for each trade computed and stored in the database:
 </li>
</ul>

|    DATE [0]    |    OPEN [1]    |    HIGH [2]    |     LOW [3]     |     CLOSE [4]    |     VOLUME [5]    |     ADJUSTED [6]     | 
|:--------------:|:--------------:|:--------------:|:---------------:|:----------------:|:-----------------:|:--------------------:|
|   2018-08-09   |     207.28     |     209.78     |      207.2      |      208.88      |  2 3 4 6 9 2 0 0  |        208.15        |

<br>
When trying to derive meaning from this type of collection, it's a good idea to focus on the <strong>closing stock price</strong>. Although it is not a good indicator on its own, visualizing it throughout many years can pose as a good representation of a company's success.<br><br>

The <strong>adjusted</strong> column represents the closing price when considering everything that happened after the <em>current day closing time</em> and before the <em>next day opening time</em>. Such events can come in the form of additional shares being offered or paying out dividends to shareholders  -- both examples decrease the stock value.

All graphs on the <strong>left</strong> were made employing <strong>only</strong> the CLOSE[4] column from <em>2000</em> to <em>2018</em>. Conversely, all graphs on the <strong>right</strong> are from the last six months and were made using R's `chartSeries` and SMA (<em>simple moving average</em>) functions allowing for a more precise forecast. <br><br>
:arrow_right: Check out my other GitHub respository [Nokia-Analysis](https://github.com/Rickyc14/NOKIA-Analysis.git) to get more info about the mechanics and purpose of the <em>simple moving average</em> used on both project!<br>

---


<p float="left">
  <img src="/data+plot/AAPL.Rplot.jpeg" width="400" />
  <img src="/data+plot/AAPL1.Rplot.jpeg" width="400" /> 
</p>

<br><br>
Apple and Amazon are among the largest companies in the world, not only that but they have the 1st and 2nd [largest market value in 2018](https://www.statista.com/statistics/263264/top-companies-in-the-world-by-market-value/) respectively. Both were founded to supply a few specific solutions to society, and after the initial inertia, they diverged just enough to keep their popularity as problem-solvers and innovators, but still residing in their initial domain.
<br><br>

<p float="left">
  <img src="/data+plot/AMZN.Rplot.jpeg" width="400" />
  <img src="/data+plot/AMZN1.Rplot.jpeg" width="400" /> 
</p>


---

Following the [link above](https://www.statista.com/statistics/263264/top-companies-in-the-world-by-market-value/) then, the 3rd place belongs to Google. Indeed, Alphabet is Google's parent company founded in 2015 by Google's founders as a way of maintain control. After that, all prior Google stocks were converted into Alphabet stocks -- more than half being in possession of a few a people that were closely involved in the company's initial development. Nonetheless, trading is still available for the public under these <strong>tickers</strong>: "GOOG" and "GOOGL". Buying the first will not grant the right to vote on any company decision, and the second will cost a little extra, but it comes with voting rights. All told, both types will follow similar trends. 



<br><br>
  <img src="/data+plot/GOOG.Rplot.jpeg" width="400" />
  <img src="/data+plot/GOOG1.Rplot.jpeg" width="400" /> 
</p>
<br>


> Adjusted closing stock price for all three companies: <em>both Alphabet tickers follow the same changing patterns</em>
> even having different absolute values<br>

|    DATE    |  AAPL    |   AMZN   |   GOOG    |    GOOGL   |    DATE    |  AAPL    |   AMZN   |   GOOG    |    GOOGL   |   
|:----------:|:--------:|:--------:|:---------:|:----------:|:----------:|:--------:|:--------:|:---------:|:----------:|   
| 2015-01-02 |  103.86  |  308.52  |   524.81  |   529.55   | 2015-01-06 |  100.94  |  295.29  |   501.96  |   506.64   | 
| 2015-01-05 |  100.93  |  302.19  |   513.87  |   519.46   | 2015-01-07 |  102.36  |  298.42  |   501.10  |   505.15   |



---
---




When dealing with stocks though, it's better to look at <strong>changes</strong> rather than absolute values. The plot on the <strong>right shows absolute</strong> stock prices, and the one on the <strong> left tell us about the earnings</strong> of investors over that particular period of time. This is done with a simple, but efficient approach: dividing the stock's current value by its original value, and then subtracting one from it -- since the initial capital can't be seen as earnings.<br>

<br>
<p float="left">
<img src="/data+plot/Jupyter_docs/relative_value_stock.png " />
<img src="/data+plot/Jupyter_docs/absolute_value_stock.png " />
 </p>

The method used to plot the <strong>left graph</strong> is very useful, but it's possible to go a bit further. Instead of dividing present/past values and subtracting one, recursively implementing this method after each day is a much more accurate way to evaluate returns. It's worth noting that this process is mostly used like this: `log(v[t+1]) - log(v[t])`; v[t] being the stock's value at any given time <em>[ t ]</em>. This eliminates a lot possible data conflicts, which is predictable considering logarithmic properties are close related to changes from percentage values. <br>

<br>
<p float="left">
<img src="/data+plot/Jupyter_docs/returns2.png " width="400" />
<img src="/data+plot/returns_Rplot.jpeg " width="400"/>
 </p>
<br>

<h4>Both charts above represent the same concept: return on investment. </h4><br> 
<strong>Left</strong> - it was used a couple of very useful <strong>Python</strong> modules:<br>
<ul>
<li>
 
  [matplotlib](https://matplotlib.org/): plotting
 </li>
 <li>
 
  [pandas](https://pandas.pydata.org/): setting data frame
 </li>
 <li>
 
  [numpy](http://www.numpy.org/): setting log function into the program
 </li>
 <li>
 
  [quandl](https://www.quandl.com/): requesting data
 </li>
</ul>


<strong>Right</strong> - R code: 
```r
# R code for implementing the recursively log process mentioned above:

ap = AAPL[,6] %>% log %>% diff
am = AMZN[,6] %>% log %>% diff
go = GOOG[,6] %>% log %>% diff
```
