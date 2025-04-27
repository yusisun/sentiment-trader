import matplotlib.pyplot as plt

def plot_pnl(trades):
    pnl = [t['pnl'] for t in trades]
    plt.plot(pnl)
    plt.title("PnL Over Time")
    plt.show()
