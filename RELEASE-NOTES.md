# Release notes — 64-City Price Bracket

Release date: October 2, 2026

## Summary

This additive release introduces `bracket.html`, a responsive, ESPN-inspired view of the complete 64-city research tournament. The existing schedule, standings, price board, research homepage, and published box scores remain in place.

## What changed

- Added `bracket.html` as a separate page; `schedule.html` was not replaced.
- Displays all 64 cities across East, West, South, and Midwest regional brackets.
- Advances published winners automatically from `schedule-data.json`.
- Shows Boston and Cambridge in East Quarterfinal 1 based on their published next-month forecast prices.
- Displays both forecast prices for completed matchups and labels the higher-price city as the bracket winner.
- Preserves full city names through multiline wrapping at normal browser zoom.
- Uses horizontal regional scrolling on smaller screens instead of truncating city names.
- Includes an embedded fallback dataset so the page remains readable when opened outside a web server.
- Adds Bracket navigation to the research homepage and adds the page to `sitemap.xml`.
- Retains explicit Zillow-source and independent ChrionML-methodology disclosures.

## Research disclosure

Zillow publishes the underlying Zillow Home Value Index histories by geography and housing type. ChrionML selects the relevant condo/co-op series, compiles and quality-checks the monthly datasets, evaluates candidate forecasting models, quantifies uncertainty, and publishes the resulting forecasts and findings. Zillow did not produce, review, or endorse the forecasts.

Forecasts are analytical estimates, not appraisals, investment advice, or guarantees.

## Primary production files

- `bracket.html` — new complete 64-city bracket
- `schedule-data.json` — authoritative matchup status, forecasts, and box-score links
- `index.html` — adds the Bracket navigation link
- `sitemap.xml` — adds the public bracket URL
- `README.md` — documents the bracket convention and public link

## Recommended commit message

`Add 64-city price bracket with automatic winner advancement`
