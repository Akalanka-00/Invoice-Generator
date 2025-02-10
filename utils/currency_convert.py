

def currency_convert(amount):
    exchange_rate = 0.012
    usd_amount = float(amount) * exchange_rate
    return round(usd_amount, 2)  # Round the result to 2 decimal places
