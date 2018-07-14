from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    max_profit = 0.0
    for i in range(len(prices)-1):
        max_price_future = max(prices[i+1:])
        profit_poss = max_price_future - prices[i]
        if profit_poss > max_profit:
            max_profit = profit_poss
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
