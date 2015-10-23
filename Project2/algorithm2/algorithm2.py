def changegreedy(coins, total):
    
    num_coins = 0
    num_of_each = []

    for coin in coins:
        num_of_each.append(0)

    i = len(coins)

    while total > 0:
        if total - coins[i - 1] >= 0:
            num_of_each[i - 1] += 1
            num_coins += 1
            total -= coins[i - 1]
        else:
            i -= 1

    return num_of_each, num_coins