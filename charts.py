from lib import *
from ipywidgets.widgets import interaction
from ipywidgets import interact, interact_manual

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [10, 10]


def build_chart(title, y_label, x_label, domain):
    """
    Builds a chart with the given title, y-axis label, x-axis label, and domain.
    """
    fig = plt.figure()
    ax = plt.gca()

    ax.tick_params(axis='x', rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    fig.tight_layout()

    return ax


def tx_volume_chart(period=(360, 1800, 90)):
    ax = build_chart('Transaction Volume', 'Transactions', 'Day (t)', period)
    t = np.arange(0, period, 1)
    y = [simulate_transactions_per_day(x) for x in t]
    ax.plot(t, y, label='Transactions')

    plt.show()


def token_supply_chart(reward_per_block=(0, 10000, 1), fee_per_tx=(0, 10, 0.01), period=(360, 1800, 90)):
    ax = build_chart('Total Supply', 'Coins', 'Day (t)', period)

    t = np.arange(1, period+1, 1)
    y = [calculate_tokens_per_day(x, reward_per_block) for x in t]
    y2 = [calculate_inflation_per_day(
        x, reward_per_block, fee_per_tx) for x in t]
    ax.plot(t, y, label='Tokens Produced')
    ax.plot(t, y2, label='Total Supply Estimation')
    ax.legend(labels=['Tokens Produced', 'Total Supply Estimation'])

    plt.show()


def percentage_inflation_chart(fee_per_tx=(0, 10, 0.01), period=(365, 3650, 90), percentage=(1, 10, 0.1), genesis_supply=(0, 1000000000, 1000)):
    ax = build_chart('Total Supply', 'Coins', 'Day (t)', period)

    t = np.arange(1, period+1, 1)
    y = [fixed_percentage_inflation_per_day(
        x, fee_per_tx, percentage, genesis_supply) for x in t]
    ax.plot(t, y, label='Total Supply')

    plt.show()
