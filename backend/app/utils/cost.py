def estimate_cost(duration: int, budget: float | None) -> dict:
    # Extremely simple placeholder logic – swap with BigQuery-powered model later
    daily_accom = 2500
    daily_food = 700
    daily_transport = 400
    flat_fees = 2000  # entrances + misc

    cost = {
        "accommodation": daily_accom * duration,
        "food": daily_food * duration,
        "transport": daily_transport * duration,
        "entrance_fees": flat_fees,
        "misc": 0.05 * (budget or 0)  # 5 % buffer
    }
    cost["total"] = sum(cost.values())
    return cost
