
# coding: utf-8

# In[30]:


import pandas as pd
import quandl
import datetime
 
start = datetime.datetime(2015,1,1) 
end = datetime.date.today()


apple, amazon, google, alphabet = (quandl.get("WIKI/" + s, start_date=start, end_date=end) for s in ["AAPL", "AMZN","GOOG", "GOOGL"])
 
stocks = pd.DataFrame({"AAPL": apple["Adj. Close"],
                      "AMZN": amazon["Adj. Close"],
                      "GOOG": google["Adj. Close"],
                      "GOOGL": alphabet["Adj. Close"]}) #Alphabet Inc.
 
stocks.head()


# In[31]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')

stocks.plot(grid = True)


# In[32]:


stock_return = stocks.apply(lambda x: x / x[0])
stock_return.head() - 1

stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)

