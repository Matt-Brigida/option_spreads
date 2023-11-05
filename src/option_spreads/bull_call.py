import seaborn
import numpy
import scipy
import matplotlib.pyplot as plt
plt.style.use("dark_background")

class bull_call:
    """A class to describe the behavior and p/l from bull call option spreads."""
    def __init__(self, strike_1, strike_2, price_1, price_2):
        self.strike_1 = strike_1
        self.strike_2 = strike_2
        self.price_1 = price_1
        self.price_2 = price_2

    def range_underlying_price(self):
        lower_range = self.strike_1 - 10
        upper_range = self.strike_2 + 10
        underlying_price = list(range(lower_range, upper_range+1))
        return(underlying_price)

    def spread_profit(self):
        underlying_price = self.range_underlying_price()
        profit_strike_1 = numpy.array([max(i - self.strike_1, 0) - self.price_1 for i in underlying_price])
        profit_strike_2 = -(numpy.array([max(i - self.strike_2, 0) - self.price_2 for i in underlying_price]))
        spread_profit = profit_strike_1 + profit_strike_2 
        return(spread_profit)

    def plot(self):
        underlying_price = self.range_underlying_price()
        spread_profit = self.spread_profit()
        spread_plot = seaborn.lineplot(x = underlying_price, y = spread_profit)
        fig = spread_plot.get_figure()
        fig.savefig("bull_call_profit.png")
        ## spread_plot
        ## plt.show()

    def max_loss(self):
        ## calculate max gain, max loss, and b/e.  Returns dict-------
        return(max_loss)

    def max_gain(self):
        return(max_gain)

    def breakeven(self):
        return({'breakeven_point_1':be_1, 'breakeven_point_2':be_2})
        
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
        
