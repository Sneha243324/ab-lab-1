def score_deal(amount: float, risk: int, customer_type: str) -> float:
    base = amount / 1000.0

    multipliers = {
    "enterprise": 1.25,
    "smb": 1.0,
    "consumer": 0.9,
    }
    multiplier = multipliers.get(customer_type, 0.9)


    penalty = risk / 50.0
    return (base * multiplier) - penalty




def decision(score: float) -> str:
    if score >= 8:
        return "APPROVE"
    if score >= 4:
        return "REVIEW"
    return "REJECT"


def main() -> None:
    amount = 10000.0
    risk = 35
    customer_type = "smb"

    s = score_deal(amount, risk, customer_type)
    print(f"score={s:.2f} decision={decision(s)}")


if __name__ == "__main__":
    main()