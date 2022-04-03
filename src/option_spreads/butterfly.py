import seaborn
import numpy
import matplotlib.pyplot as plt
plt.style.use("dark_background")

class Butterfly:
    def __init__(self, strike_1, strike_2, strike_3, price_1, price_2, price_3):
        self.strike_1 = strike_1
        self.strike_2 = strike_2
        self.strike_3 = strike_3
        self.price_1 = price_1
        self.price_2 = price_2
        self.price_3 = price_3

    def plot(self):
       lower_range = self.strike_1 - 10
       upper_range = self.strike_3 + 10
       underlying_price = list(range(lower_range, upper_range+1))
       profit_strike_1 = numpy.array([max(i - self.strike_1, 0) - self.price_1 for i in underlying_price])
       profit_strike_2 = -2 * numpy.array([max(i - self.strike_2, 0) - self.price_2 for i in underlying_price])
       profit_strike_3 = numpy.array([max(i - self.strike_3, 0) - self.price_3 for i in underlying_price])
       spread_profit = profit_strike_1 + profit_strike_2 + profit_strike_3
       spread_plot = seaborn.lineplot(x = underlying_price, y = spread_profit)
       fig = spread_plot.get_figure()
       fig.savefig("butterfly_profit.png")
       ## spread_plot
       ## plt.show()

    def max_min(self):
        ## calculate max gain, max loss, and b/e.  Returns dict-------
        max_loss = -1 * (- self.price_1 + 2 * self.price_2 - self.price_3)
        max_gain = (self.strike_2 - self.strike_1) - max_loss
        be_1 = self.strike_1 + max_loss
        be_2 = self.strike_3 - max_loss
        return({'Max_Loss':round(max_loss,2), 'Max_Gain':round(max_gain,2), 'Breakeven_1':round(be_1,2), 'Breakeven_2':round(be_2,2)})
        
