# Release notes — Real Estate Condo Price Board

Release date: October 2, 2026

## Summary

This release replaces the former single-matchup `boxscore.html` experience with a responsive, ESPN-inspired Real Estate Condo Price Board. Completed weekly matchups now appear in a continuous stacked view, while detailed model and research statistics remain available through expandable box scores.

## What changed

- Added a stacked weekly price board for completed matchups.
- Added Cambridge vs. Ithaca as the featured Week 2 matchup.
- Retained Boston vs. Providence as the Week 1 final.
- Displayed each city's latest Zillow ZHVI value, next-month forecast, and projected change.
- Added expandable research statistics, prediction ranges, trend charts, and five-model MAE comparisons.
- Added responsive desktop and mobile layouts.
- Added canonical URL, search description, and Open Graph metadata for `boxscore.html`.
- Corrected portfolio methodology language to distinguish Zillow's published ZHVI histories from ChrionML's independent dataset construction, quality assurance, modeling, backtesting, interpretation, and visualization.
- Added direct Zillow source links for each completed city.
- Preserved schedule-driven homepage counts and the latest completed matchup logic.

## Research disclosure

Zillow publishes the underlying Zillow Home Value Index histories by geography and housing type. ChrionML selects the relevant condo/co-op series, compiles and quality-checks the monthly datasets, evaluates candidate forecasting models, quantifies uncertainty, and publishes the resulting forecasts and findings. Zillow did not produce, review, or endorse the forecasts.

Forecasts are analytical estimates, not appraisals, investment advice, or guarantees.

## Primary production files

- `boxscore.html` — new Real Estate Condo Price Board
- `cambridge-ithaca-boxscore.html` — Week 2 full matchup research
- `index.html` — research homepage with current program totals
- `schedule.html` and `schedule-data.json` — completed-matchup status and links
- `README.md` — updated portfolio methodology

## Recommended commit message

`Release condo price board and transparent ZHVI methodology`
