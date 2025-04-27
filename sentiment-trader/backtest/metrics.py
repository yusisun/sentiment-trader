def compute_metrics(trades):
    total_return = sum([trade['pnl'] for trade in trades])
    sharpe_ratio = total_return / (sum([trade['risk'] for trade in trades]) + 1e-9)
    return total_return, sharpe_ratio
