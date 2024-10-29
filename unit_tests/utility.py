CALCULATE_API_URL = 'https://taotlus.bigbank.ee/api/v1/loan/calculate'


def json_request(maturity, amount, interest_rate, monthly_payment_day, administration_fee=3.49, conclusion_fee=600,
                 currency='EUR', product_type='SMALL_LOAN_EE01', ):
    return {
        "maturity": maturity,
        "productType": product_type,
        "amount": amount,
        "interestRate": interest_rate,
        "monthlyPaymentDay": monthly_payment_day,
        "administrationFee": administration_fee,
        "conclusionFee": conclusion_fee,
        "currency": currency
    }
