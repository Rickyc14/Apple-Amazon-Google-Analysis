# Apple-Amazon-Google-Analysis

Very few companies can match the influence these three posses. They are the trend-makers always trying to stay 
ahead of the curve. Back in 2005, when a few of PayPal founders started YouTube, and the platform was still finding 
its place on the world wide web, its functionalities weren't yet clear to the public. However, the potential around 
it wasn't ignored, and less than two years later Google acquired it for 1.6 billion. <br>

The archive above contains <em>xlsx</em> files with the data used for this project along with a <em>nasdaq100 list</em>. 
This is common data pattern for each trading computed and stored in the database:
```
- DATE                                - OPEN                                     - HIGH 
- LOW                                 - CLOSE                                    - VOLUME
- ADJUSTED
```
The majority of it is self-explanatory, and when trying to derive meaning from this type of collection, it's a good idea to focus on the closing stock price. Although it is not a good indicator on its own, visualizing it throughout many years can pose as a good representation of a company's position. 
The data was obtained from Yahoo finance using R software. 
