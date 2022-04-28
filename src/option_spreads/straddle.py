import seaborn
import numpy
import scipy
import matplotlib.pyplot as plt
plt.style.use("dark_background")

class Straddle:
    """A class to describe the behavior and p/l from Straddle option spreads."""
    def __init__(self, strike, call_price, put_price, long_short):
        self.strike = strike
        self.call_price = call_price
        self.put_price = put_price
        self.long_short = long_short

    def breakeven(self):
        max_loss = self.max_loss()
        be_1 = self.strike + (call_price + put_price)
        be_2 = self.strike - (call_price + put_price)
        return({'breakeven_point_1':be_1, 'breakeven_point_2':be_2})

    def range_underlying_price(self):
        lower_range = self.be_2 - 10
        upper_range = self.be_1 + 10
        underlying_price = list(range(lower_range, upper_range+1))
        return(underlying_price)


    def spread_profit(self):
        underlying_price = self.range_underlying_price()
        profit_call = numpy.array([max(i - self.strike, 0) - self.call_price for i in underlying_price])
        profit_put = numpy.array([max(self.strike - i, 0) - self.put_price for i in underlying_price])
        spread_profit = profit_call + profit_put
        return(spread_profit)


    def plot(self):
        underlying_price = self.range_underlying_price()
        spread_profit = self.spread_profit()
        spread_plot = seaborn.lineplot(x = underlying_price, y = spread_profit)
        fig = spread_plot.get_figure()
        fig.savefig("straddle_profit.png")


    def max_loss(self):
        ## calculate max gain, max loss, and b/e.  Returns dict-------
        max_loss = self.call_price + self.put_price
        return(max_loss)

    def max_gain(self):
        max_gain = "no limit"
        return(max_gain)

### work from here-----------------------------------------
        
    def probability_profit(self, stock_price, vol, rf, days_to_option_exp):
        """Calculate the risk-neutral probability of profiting from the option spread"""
        be_1 = self.breakeven().get('breakeven_point_1')
        be_2 = self.breakeven().get('breakeven_point_2')
        ## expected stock price-----
        expected_stock_price = stock_price * numpy.exp((rf / 252) * days_to_option_exp)
        return_to_be_1 = be_1 / expected_stock_price - 1
        return_to_be_2 = be_2 / expected_stock_price - 1
        ## Normal Dist
        ## wait though--I should turn into a return distribution---returns are normal---
        def norm(x):
            return scipy.stats.norm.pdf(x, rf, vol)
        # integrate between bounds
        integral = scipy.integrate.quad(norm, return_to_be_1, return_to_be_2)
        return(integral[0])

        ### This function will require some thought.  I should create a p/l function of the option
        ### as a function of the stock's return and not price.  PDF is of return.
    # def expected_profit_per_option(self, stock_price, vol, rf, days_to_option_exp):
    #     """Calculate the expected profit given the risk-neutral density."""
    #     underlying_price = self.range_underlying_price()
    #     spread_profit = self.spread_profit()

    #     be_1 = self.breakeven().get('breakeven_point_1')
    #     be_2 = self.breakeven().get('breakeven_point_2')
    #     ## expected stock price-----
    #     expected_stock_price = stock_price * numpy.exp((rf / 252) * days_to_option_exp)
    #     return_to_be_1 = be_1 / expected_stock_price - 1
    #     return_to_be_2 = be_2 / expected_stock_price - 1
    #     ## Normal Dist
    #     ## wait though--I should turn into a return distribution---returns are normal---
    #     def norm(x):
    #         return scipy.stats.norm.pdf(x, rf, vol)
    #     expected_profit = 
        
