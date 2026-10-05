# ChrionML® AI Labs — Research & Insights

ChrionML® AI Labs publishes independent applied machine-learning research with transparent source qualification, dataset construction, quality assurance, model evaluation, interpretation, and limitations.

## 64-City Intelligence program

The program currently includes four completed ZIP-level condo/co-op forecasting projects:

- Boston, MA 02114
- Providence, RI 02903
- Cambridge, MA 02139
- Ithaca, NY 14850

The studies are organized into two finalized matchups:

- Week 1: Boston vs. Providence
- Week 2: Cambridge vs. Ithaca

Each city uses 80 monthly observations and five candidate forecasting approaches evaluated through 44 expanding-window, one-month-ahead backtests.

## Data provenance

Zillow publishes the underlying Zillow Home Value Index histories by geography and housing type. ChrionML® identifies the relevant condo/co-op series, compiles and quality-checks the research datasets, evaluates the forecasting models, quantifies uncertainty, and publishes the resulting analysis. Zillow did not produce, review, or endorse the forecasts.

Forecasts are analytical estimates—not appraisals, investment advice, or guarantees.

## Research architecture

- `research/` — completed-project archive
- `research/boston-vs-providence/` — Week 1 publication
- `research/cambridge-vs-ithaca/` — Week 2 publication
- `methodology/` — research protocol
- `about-olu-daramola/` — Olu (Tim) Daramola, founder and research lead
- `standings.html` — schedule-driven Research Standings
- `schedule-data.json` — shared weekly publication data

## Weekly standings update

When a matchup is complete:

1. Add the two city forecasts and historical average, high, and low values to `research_findings` in `schedule-data.json`.
2. Set `publication_status` to `final`.
3. Add the matchup `boxscore_url` and `published_at` date.

The homepage and standings then update their city counts, latest matchup, table rows, and rankings automatically.

## Links

- [Production research site](https://daramoladoes.github.io/)
- [Research archive](https://daramoladoes.github.io/research/)
- [Research methodology](https://daramoladoes.github.io/methodology/)
- [Olu (Tim) Daramola](https://daramoladoes.github.io/about-olu-daramola/)
- [YouTube](https://www.youtube.com/@chrionml/videos)
- [LinkedIn](https://www.linkedin.com/in/oludaramola-ai/)

© 2024–2026 ChrionML® AI Labs

ChrionML® is the proprietary research brand of Olu (Tim) Daramola. Original brand assets and published works are supported by the referenced U.S. Copyright Office registration.
