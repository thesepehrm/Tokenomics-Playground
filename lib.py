from math import log, sqrt, ceil, log2

# Median Blocktime of the network.
MEDIANBLOCKTIME = 5

# Maximum transactions per Block for the network
MAXTXPERBLOCK = 32000


def FORMULA(x):
    """
    Calculate the number of transactions per block
    Edit this formula to change the growth of the transactions per block
    """
    return (log((x+9)/10))


BLOCKS_PER_DAY = (3600 * 24) // MEDIANBLOCKTIME

database = {
    'total_supply': 0
}


def calculate_tokens_per_day(day, reward_per_block):
    """
    Calculate tokens per day
    """
    return day * BLOCKS_PER_DAY * reward_per_block


def calculate_inflation_per_day(day, reward_per_block, fee_per_tx):
    """
    Calculate inflation per day
    """
    tokens = calculate_tokens_per_day(day, reward_per_block)
    tpd = simulate_transactions_per_day(day)
    return tokens - (tpd * fee_per_tx)


def fixed_percentage_inflation_per_day(day, fee_per_tx, percentage, genesis_supply):
    """
        Calculate inflation per day
        This method is used to calculate the inflation per day by a specific percentage
    """
    if day == 1:
        database['total_supply'] = genesis_supply
        return genesis_supply

    # to avoid negative tokens
    if database['total_supply'] < 0:
        return 0

    inflation_per_year = (float(percentage) / 100.0) * database['total_supply']
    tokens = inflation_per_year / 365.0

    tpb = simulate_transactions_per_block(day)

    fee = fee_per_tx - ((fee_per_tx - 1)/MAXTXPERBLOCK) * tpb
    total_fee = (tpb * fee * BLOCKS_PER_DAY)

    database['total_supply'] += tokens - total_fee

    return database['total_supply']


def simulate_transactions_per_block(day):
    txs = FORMULA(day)
    # TODO: Add some noise for decoration :))

    if txs > MAXTXPERBLOCK:
        return MAXTXPERBLOCK
    return txs


def simulate_transactions_per_day(day):
    return BLOCKS_PER_DAY * simulate_transactions_per_block(day)
