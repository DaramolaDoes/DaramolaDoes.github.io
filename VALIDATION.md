# Week 4 revised release validation

Date: October 14, 2026. Result: the confirmed release defects have been corrected. The revised static site passes the automated local Chromium checks below and is ready for a controlled production deployment, followed by live smoke checks.

## Browser validation

Chromium 153.0.8010.0, driven by Playwright, served the extracted candidate over local HTTP. All 20 full HTML pages were checked at 1440×900 and 390×900: 40 final page/viewport observations. HOMEPAGE-INSERT.html is a fragment and was checked statically rather than as a full page.

- All page responses were HTTP 200.
- No uncaught page JavaScript errors, failed requests, HTTP errors on loaded resources, broken images, missing same-page anchors, or document-level horizontal overflow were detected.
- Eight interaction scenarios passed: shared menu/Week 4/Escape; standings counts and regions; bracket counts and advancement; forecast city/horizon execution; Week 4 canonical and negative chart annotation; schedule search and region filtering; price-board expansions; mobile navigation and Week 4 access.
- The schedule's mobile grid and secondary navigation overflow found during testing were fixed and retested at both widths.
- Selected homepage, study, standings and box-score renders were inspected during QA. Screenshots are not included in this package.

Machine-readable final results are in reproducibility/browser-validation.json. These checks are targeted smoke tests, not exhaustive interaction, accessibility, or cross-browser certification. Production was not modified or tested as part of this revision.

## Model reproduction

| Market | Selected model | October forecast | MAE | Relative MAE proxy | Projected monthly change |
|---|---|---:|---:|---:|---:|
| Brooklyn 11201 | Holt damped trend | $1,308,132 | $3,718 | 0.285% | +0.16% |
| Philadelphia 19107 | Holt damped trend | $257,048 | $439 | 0.170% | −0.29% |

The supplied CSVs each contain 81 unique, consecutive monthly dates from January 2020 through September 2026, with finite positive prices. Both selected models and every rounded leaderboard MAE/RMSE, point forecast and empirical residual range reproduce the original published Week 4 values. Five candidates were evaluated from 37 initial training months across 44 expanding-window one-step validation forecasts. See reproducibility/verify_week4.py, requirements.txt and week4-model-results.json. Use a virtual environment and run `python -m pip install -r reproducibility/requirements.txt`, then `python reproducibility/verify_week4.py` from the package root.

Model selection and error reporting use the same validation windows. There is no independent post-selection test. Relative MAE is MAE divided by September's observed value, not MAPE. Empirical residual ranges are not calibrated confidence intervals. Earlier published studies and their model results are preserved; they were not independently rerun in this revision. This verification uses the supplied CSVs, not a fresh independent transcription of Zillow's condo view.

## Static and outbound-link checks

All declared local href/src targets and fragment destinations resolve. JSON and JavaScript/JSON-LD syntax checks pass. The eight-city schedule, standings and bracket share the finalized matchup data; Weeks 1–3 target September and Week 4 targets October.

The retired YouTube URL was replaced with the responding ChrionML channel. Of 18 distinct external href/src URLs, 16 returned HTTP 200; two LinkedIn profile URLs returned HTTP 999 and remain inconclusive. One responding GitHub issue URL redirects to login. HTTP 200 is a transport check, not proof of video playability, profile identity, or the selected Zillow housing-type view. Per-URL results are in reproducibility/external-url-validation.json.

## Deployment scope

This package replaces the complete static site, including index.html. Use DEPLOYMENT.md, preserve all folders, and verify the published pages after GitHub Pages finishes. Hosting-specific behavior is not established by local tests.

## Homepage copy revision

The revised homepage paragraph was rechecked in Chromium at 1440×900 and 390×900, with additional desktop/mobile preview captures. Exact replacement wording was verified, the old photography claim was absent, and no runtime errors, broken assets, missing anchors, or horizontal overflow were detected. The earlier full-site results apply to the unchanged pages. Evidence: reproducibility/homepage-copy-validation.json.
