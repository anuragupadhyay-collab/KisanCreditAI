import pandas as pd

exchange_df = pd.read_csv("data/exchange_rate.csv")

exchange_dict = dict(zip(exchange_df["Year"], exchange_df["USD_INR"]))


def usd_to_inr(price_usd, year):
    year = int(year)

    # Agar year available hai
    if year in exchange_dict:
        rate = exchange_dict[year]

    # Agar future year hai
    elif year > max(exchange_dict.keys()):
        rate = exchange_dict[max(exchange_dict.keys())]

    # Agar past year hai
    else:
        rate = exchange_dict[min(exchange_dict.keys())]

    return round(price_usd * rate, 2)