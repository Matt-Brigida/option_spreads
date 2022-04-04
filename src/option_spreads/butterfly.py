import seaborn
import numpy
import scipy
import matplotlib.pyplot as plt
plt.style.use("dark_background")

class Butterfly:
    """A class to describe the behavior and p/l from Butterfly option spreads."""
    def __init__(self, strike_1, strike_2, strike_3, price_1, price_2, price_3):
        self.strike_1 = strike_1
        self.strike_2 = strike_2
        self.strike_3 = strike_3
        self.price_1 = price_1
        self.price_2 = price_2
        self.price_3 = price_3

    def range_underlying_price(self):
        lower_range = self.strike_1 - 10
        upper_range = self.strike_3 + 10
        underlying_price = list(range(lower_range, upper_range+1))
        return(underlying_price)

    def spread_profit(self):
        underlying_price = self.range_underlying_price()
        profit_strike_1 = numpy.array([max(i - self.strike_1, 0) - self.price_1 for i in underlying_price])
        profit_strike_2 = -2 * numpy.array([max(i - self.strike_2, 0) - self.price_2 for i in underlying_price])
        profit_strike_3 = numpy.array([max(i - self.strike_3, 0) - self.price_3 for i in underlying_price])
        spread_profit = profit_strike_1 + profit_strike_2 + profit_strike_3
        return(spread_profit)

    def plot(self):
        underlying_price = self.range_underlying_price()
        spread_profit = self.spread_profit()
        spread_plot = seaborn.lineplot(x = underlying_price, y = spread_profit)
        fig = spread_plot.get_figure()
        fig.savefig("butterfly_profit.png")
        ## spread_plot
        ## plt.show()

    def max_loss(self):
        ## calculate max gain, max loss, and b/e.  Returns dict-------
        max_loss = -1 * (- self.price_1 + 2 * self.price_2 - self.price_3)
        return(max_loss)

    def max_gain(self):
        max_gain = (self.strike_2 - self.strike_1) - max_loss
        return(max_gain)

    def breakeven(self):
        max_loss = self.max_loss()
        be_1 = self.strike_1 + max_loss
        be_2 = self.strike_3 - max_loss
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
        
