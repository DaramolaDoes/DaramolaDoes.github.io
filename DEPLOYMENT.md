# ChrionML® Interactive Lab — Safe Production Deployment

## Deployment philosophy
This is an **additive release**. Do not upload this ZIP as a replacement for your whole repository. The existing `index.html`, `schedule.html`, `standings.html`, `bracket.html`, `boxscore.html`, `research/`, `methodology/`, and `platform.html` remain untouched until you deliberately insert the CTA.

## 1. Back up production
Open https://github.com/DaramolaDoes/DaramolaDoes.github.io and choose **Code → Download ZIP**. Keep the backup.

## 2. Upload new files
On the repository's `main` branch choose **Add file → Upload files**. Upload these files preserving their paths:
- `forecast-lab.html`
- `intelligence-lab.html`
- `assets/data/boston-condo-2020-2026.csv`
- `assets/data/providence-condo-2020-2026.csv`

For nested CSV paths, the easiest method is Git locally, or create the directories via GitHub's file editor before upload. Do **not** upload `HOMEPAGE-INSERT.html` or `DEPLOYMENT.md` to the site unless you want them publicly accessible; they are deployment aids.

## 3. Verify new pages before editing homepage
Visit:
- https://daramoladoes.github.io/intelligence-lab.html
- https://daramoladoes.github.io/forecast-lab.html
Check dropdowns, plots, MAE/MAPE, table, both markets, and responsive layout. Confirm browser console has no errors.

## 4. Add CTA to existing homepage
Edit the **existing** root `index.html` on GitHub. Find the closing `</section>` for your current hero, and paste the contents of `HOMEPAGE-INSERT.html` immediately after it, within `<main>`. Commit as `feat: launch interactive Boston Providence forecast lab`. **Do not replace your homepage** with `intelligence-lab.html`; it is a separate product landing page.

## 5. Production smoke tests
- Existing homepage, research archive, bracket, schedule, standings, all three box scores and platform page still load.
- Homepage CTA launches forecast lab; secondary CTA launches product landing page.
- Forecast lab loads both city datasets and displays Boston $778,846 and Providence $436,391 as August 2026 observations.
- Change each dropdown; forecast and chart update.
- Holdout and baseline metrics show finite values; no claimed 97% accuracy.
- Test at mobile widths and keyboard navigation.
- Check the model disclaimer and Zillow provenance text.

## 6. Rollback
Remove the inserted CTA from `index.html` using GitHub commit history. Optionally delete the four new files. Existing site pages should be unaffected.

## Limitations
The forecast runs in browser using a ridge-regularized autoregression of monthly percentage changes, three lags and annual cyclic terms. A 12-month fixed-origin recursive holdout is compared with a constant-last-value baseline. This differs from the original published 44 expanding-window one-step tests. No backend, email capture, live data feed, model registry, or validated predictive intervals are included. Do not imply that those features are live.
