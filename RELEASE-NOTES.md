# Release notes — ChrionML® Research Archive

## Brand-standardization update — October 4, 2026

- Standardized visible, metadata, Open Graph, structured-data, methodology, disclosure, and footer references to **ChrionML®**.
- Preserved functional lowercase URLs and handles, including `youtube.com/@chrionml`.
- Added a clear proprietary-brand statement to the public project documentation.

Release date: October 4, 2026

## Summary

This release establishes a scalable editorial and data architecture for the ChrionML® 64-City Intelligence program. Four completed city-level ML projects are organized into a searchable research archive, two matchup articles use a consistent scientific-publication structure, and Research Standings update from the shared schedule dataset.

## New pages

- `/research/` — archive for completed city ML projects and matchup publications
- `/research/boston-vs-providence/` — Week 1 research article
- `/research/cambridge-vs-ithaca/` — Week 2 research article
- `/methodology/` — versioned research protocol
- `/about-olu-daramola/` — founder and research-lead profile

## Research article standard

Each matchup article now includes:

- Abstract and publication date
- Research goal
- Principal findings
- Methods summary
- Data availability and provenance
- Limitations and interpretation boundaries
- References and direct Zillow source links
- Clickable in-page article navigation
- Structured article metadata

The author identity is standardized as **Olu (Tim) Daramola**. Principal findings use a light editorial presentation for improved readability.

## Dynamic Research Standings

The ESPN-inspired standings table replaces sports W-L-T fields with:

1. Forecasted Price
2. Historical Average
3. Historical High
4. Historical Low

The page reads finalized matchups from `schedule-data.json`, creates two city rows per matchup, sorts by forecasted price, recalculates rank, updates the published-city count, and supports region filters.

For every future final matchup, add the following fields under `research_findings`:

```json
{
  "forecast_a": 0,
  "forecast_b": 0,
  "historical_avg_a": 0,
  "historical_avg_b": 0,
  "historical_high_a": 0,
  "historical_high_b": 0,
  "historical_low_a": 0,
  "historical_low_b": 0
}
```

Also set `publication_status` to `final` and supply `boxscore_url`.

## Search and brand identity

- Added canonical URLs for all five new pages.
- Added Organization, Person, CollectionPage, and TechArticle structured data.
- Expanded `sitemap.xml`.
- Connected personal LinkedIn, company LinkedIn, YouTube, GitHub, and the U.S. Copyright Office record.
- Standardized the ChrionML® name and 2024–2026 copyright notation.
- Reordered primary navigation to Research, Schedule, Bracket, Standings, Platform, Videos.

## Recommended commit message

`Launch ChrionML® research archive and dynamic city standings`
