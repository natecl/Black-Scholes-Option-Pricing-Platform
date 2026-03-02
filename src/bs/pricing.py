"""
Black_Scholes pricing + Greeks (vectorized / broadcast-friendly).

Design goals:
- Accept scalars or NumPy arrays for S, K, T, r, sigma (any broadcastable shapes)
- No Python loops
- Reuse shared terms for speed
"""

import numpy as np
from scipy import norm

def bs_price(S, K, T, r, sigma, option_type: str):
    """
S: Spot price
K: Strike price
T: Time to maturity
r: risk free interest rate
sigma: volatility
Option type: call or put
    """
    d1 = (np.log(S / K) + ((r + ((sigma**2)/2)) * T)) / (sigma(np.sqrt(T)))
    d2 =d1 - sigma(np.sqrt(T))

    if option_type == 'call':
        return S*norm.cdf(d1) - (K * np.e ** (-r*T) * norm.cdf(d2))
    elif option_type == 'put' :
        return K * (np.e ** (-r*T)) * norm.cdf(d2) - (S * norm.cdf(d1))
    

    