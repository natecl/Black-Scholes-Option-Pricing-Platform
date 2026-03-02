Black-Scholes Option Pricing Platform

A modular, production-style quantitative finance platform for pricing European options, computing Greeks, generating implied volatility surfaces, and analyzing portfolio risk in real time.

Built with Python, NumPy, SciPy, Streamlit, SQLite, Plotly, and pytest.

Overview

This project implements a fully vectorized Black-Scholes pricing engine with:

Closed-form option pricing (European calls & puts)

Full analytic Greeks (Delta, Gamma, Vega, Theta, Rho)

Implied volatility solver

Volatility smile & surface visualization

Portfolio risk aggregation

Scenario-based P&L analysis

SQLite-backed historical data storage

CI-tested modular architecture

The system is designed to resemble a lightweight production quant platform rather than a notebook prototype.

Features
1. Black-Scholes Pricing Engine

Vectorized NumPy implementation

Closed-form pricing

Efficient reuse of intermediate calculations (d1, d2, etc.)

Supports batch pricing across full option chains

2. Greeks Engine

Analytical computation of:

Delta

Gamma

Vega

Theta

Rho

Includes numerical finite-difference tests to validate analytic formulas.

3. Implied Volatility Solver

Uses SciPy root-finding methods

Handles edge cases (no-solution bounds)

Supports scalar and vectorized chain-level IV calculation

4. Volatility Smile & Surface

Compute IV across strikes and expiries

2D volatility smile visualization

3D volatility surface via Plotly

Optional interpolation for missing grid points

5. Portfolio & Risk Dashboard

Aggregates portfolio-level Greeks

Scenario-based stress testing:

Spot shocks

Volatility shifts

Rate shifts

Time decay

P&L explain decomposition (Delta/Gamma/Vega approximation)

6. Data Layer (SQLite)

Stores:

Underlying prices

Interest rates

Option chain quotes

Portfolio positions

Scenario definitions

Designed for reproducibility and historical backtesting.

Tech Stack

Core Computation:

Python

NumPy

SciPy

Visualization:

Streamlit

Plotly

Data:

SQLite

Testing & Dev:

pytest

GitHub Actions CI

Architecture
src/
  bs/
    pricing.py        # Black-Scholes pricing + Greeks
    implied_vol.py    # IV solver
    surface.py        # Volatility surface builder
    risk.py           # Portfolio & scenario engine
    models.py         # Data classes

  data/
    db.py             # SQLite interface
    market_data.py    # Chain ingestion

  app/
    streamlit_app.py  # UI
    components.py     # Plot components

tests/
.github/workflows/

Design principles:

Pure functions for pricing logic

Vectorized computation (no Python loops for chains)

Separation of pricing, data, and UI layers

Testable core logic independent of frontend

Installation

Clone the repository:

git clone https://github.com/yourusername/black-scholes-platform.git
cd black-scholes-platform

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run src/app/streamlit_app.py
Example Usage
Price a European Call
from bs.pricing import bs_price

price = bs_price(
    S=100,
    K=105,
    T=0.5,
    r=0.02,
    sigma=0.25,
    option_type="call"
)
Compute Implied Volatility
from bs.implied_vol import implied_vol

iv = implied_vol(
    market_price=3.50,
    S=100,
    K=105,
    T=0.5,
    r=0.02,
    option_type="call"
)
Testing

Run unit tests:

pytest

Coverage includes:

Put-call parity validation

Boundary behavior (T → 0)

Monotonicity checks

Finite-difference validation of Greeks

CI enforces test coverage and prevents regression.

Performance Notes

Fully vectorized chain pricing using NumPy

Shared intermediate term reuse

Designed to scale across thousands of strikes and expiries

Suitable for real-time dashboard refresh

Future Extensions

Dividend yield support

American option approximation

Local volatility calibration

Heston model extension

Live market data API integration

Risk-neutral density extraction

Why This Project?

This platform demonstrates:

Quantitative modeling (derivatives theory)

Numerical methods (root-finding, interpolation)

Software architecture design

Production-style engineering practices

Data persistence & reproducibility

Interactive financial visualization

It bridges quantitative finance and full-stack engineering in a clean, extensible system.