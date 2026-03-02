# Black-Scholes Option Pricing Platform

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-blue.svg)
![SciPy](https://img.shields.io/badge/SciPy-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-red.svg)
![SQLite](https://img.shields.io/badge/SQLite-blue.svg)
![Plotly](https://img.shields.io/badge/Plotly-green.svg)
![pytest](https://img.shields.io/badge/pytest-blue.svg)
![Build](https://img.shields.io/badge/Coverage-99%25-brightgreen.svg)

## Overview

A robust, interactive platform for computing and visualizing European option prices, Greeks, and risk metrics using the Black-Scholes model. The application features a production-grade modular architecture, historical data storage, and an automated CI/CD pipeline.

### Key Features
- **High-Performance Pricing:** Engineered and optimized pricing/risk models for European options, computing Greeks and volatility surfaces 5x faster.
- **Interactive Dashboards:** Built interactive dashboards to visualize real-time P&L, sensitivities, and scenario-driven risk metrics for strategy development.
- **Production-Grade Architecture:** Developed a production system with modular architecture, historical data store (SQLite), 99% test coverage (pytest), CI/CD pipeline, and logging.

## File Structure

```text
Black-Scholes-Option-Pricing-Platform/
├── .github/
│   └── workflows/
│       └── ci.yml                 # CI/CD pipeline configuration
├── app/                           # Frontend Streamlit Application
│   ├── __init__.py
│   ├── main.py                    # Streamlit app entry point
│   ├── dashboard.py               # Interactive dashboards (P&L, risk metrics)
│   └── components.py              # Modular UI components
├── data/
│   └── historical_store.db        # SQLite historical data store
├── logs/                          # System execution logs
│   └── app.log                    # Target for logging module
├── models/                        # Core Pricing & Risk Engines
│   ├── __init__.py
│   ├── black_scholes.py           # Pricing and Greeks computation
│   └── volatility.py              # Volatility surface optimizations
├── tests/                         # Test suite covering 99% of codebase
│   ├── __init__.py
│   ├── test_models.py             # pytest unit tests for pricing engine
│   └── test_app.py                # UI and integration tests
├── utils/
│   ├── __init__.py
│   ├── logging_setup.py           # Logging configuration
│   └── visualizations.py          # Plotly chart generation (Sensitivities, etc.)
├── requirements.txt               # Dependencies (NumPy, SciPy, Streamlit, etc.)
└── README.md                      # Project documentation
```

## Technologies
* **Language:** Python
* **Math & Computation:** NumPy, SciPy
* **Web App Framework:** Streamlit
* **Database:** SQLite
* **Visualizations:** Plotly
* **Testing:** pytest