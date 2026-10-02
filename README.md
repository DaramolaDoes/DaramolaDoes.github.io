# ChrionML AI Labs — Research & Insights

ChrionML AI Labs publishes evidence-led housing forecasts and applied machine-learning research. Zillow publishes the underlying Zillow Home Value Index (ZHVI) histories by geography and housing type; ChrionML locates the relevant condo/co-op series, compiles and quality-checks the monthly datasets, evaluates forecasting models, quantifies uncertainty, and translates the results into decision-ready findings.

## Completed projects

### 01 — Hyperlocal Housing Forecast Pipeline

A reproducible forecasting workflow that converts Zillow’s published monthly ZHVI histories into structured research datasets, compares time-series models, conducts expanding-window backtests, quantifies uncertainty, and publishes results in a plain-language box score. Source data and ChrionML research outputs are identified separately throughout the site.

Week 1 analyzes 80 monthly observations for each market:

- **Boston, MA 02114:** September 2026 forecast of **$779,306**, representing projected monthly growth of **0.06%**.
- **Providence, RI 02903:** September 2026 forecast of **$438,308**, representing projected monthly growth of **0.44%**.
- **Interpretation:** Boston leads on forecast home value; Providence leads on projected momentum.
- **Selected model:** Drift, chosen independently for both cities using rolling one-month-ahead mean absolute error.

The Week 2 research preview applies the same protocol to two additional markets:

- **Cambridge, MA 02139:** September 2026 forecast of **$888,570**, representing projected monthly growth of **0.19%**.
- **Ithaca, NY 14850:** September 2026 forecast of **$289,770**, representing projected monthly growth of **0.00%**.
- **Long-run trajectory:** Ithaca increased **29.5%** since January 2020 versus **17.8%** for Cambridge.
- **Selected models:** Drift for Cambridge and Last Value for Ithaca, chosen independently across 44 rolling backtests.

### 02 — Scientific Methods, Operationalized

A scientific AI platform proof of concept that transforms experimental methods into governed, reproducible, and observable services. The platform demonstrates versioned API contracts, scientist and autonomous-agent workflows, deployment controls, traceability, and operational monitoring.

## 64-city research program

Boston and Providence are the first completed matchup in a 64-city program. Cambridge and Ithaca comprise the Week 2 research preview. The opening round contains 32 weekly forecast matchups scheduled for Fridays from September 25, 2026 through April 30, 2027.

The program is designed to create a comparable evidence base across markets while maintaining consistent model evaluation, local context, transparent limitations, and reproducible publication standards.

## Research standard

Each published analysis identifies:

- Zillow ZHVI geography, housing type, source link, and sample period
- ChrionML dataset construction and quality checks
- Candidate models and comparison baseline
- Chronological backtesting approach
- Forecast value, projected change, and uncertainty range
- Out-of-sample error
- Limitations and appropriate interpretation

Zillow provides the underlying historical ZHVI data. ChrionML independently produces the datasets used for analysis, model comparisons, forecasts, findings, and visualizations. Zillow did not produce, review, or endorse the forecasts. Forecasts are analytical estimates, not appraisals, investment advice, or guarantees.

## Explore

- [Research & Insights](https://daramoladoes.github.io/)
- [Scientific AI Platform](https://daramoladoes.github.io/platform.html)
- [City Standings](https://daramoladoes.github.io/standings.html)
- [Weekly Schedule](https://daramoladoes.github.io/schedule.html)
- [Boston vs Providence Box Score](https://daramoladoes.github.io/boxscore.html)
- [Cambridge vs Ithaca Box Score](https://daramoladoes.github.io/cambridge-ithaca-boxscore.html)
- [ChrionML AI Labs Videos](https://www.youtube.com/@chrionml/videos)

© 2026 ChrionML AI Labs
