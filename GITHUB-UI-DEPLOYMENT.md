# ChrionML® GitHub UI Deployment — Full upload-ready release

## What this ZIP contains
This is a **complete copy of the uploaded production repository**, with 17 HTML pages updated in place, plus `assets/css/forecast-navigation.css` and `assets/js/forecast-navigation.js`. It preserves the existing research, images, datasets, CSS, JS, and documentation. Do not upload this ZIP as a single file to GitHub.

## GitHub browser deployment
1. Extract `chrionml-upload-ready.zip` on your computer.
2. Open your GitHub repository and choose **Add file → Upload files**.
3. Drag the **contents of the extracted `chrionml-upload-ready` folder**, not the outer folder and not the ZIP, into the upload area. GitHub should display `index.html`, `forecast-lab.html`, `assets/css/forecast-navigation.css`, etc., at their correct paths.
4. Select **Create a new branch for this commit and start a pull request**, NOT commit directly to main.
5. Name the branch `feature/forecast-labs-final-ui` and enter commit message `Integrate Forecast Labs across ChrionML website`.
6. Review **Files changed** carefully. The changed HTML pages should preserve their existing research and model JavaScript; the two new assets should be present.
7. Merge only after reviewing the pull request. GitHub Pages may not generate a preview for an unmerged branch; use a separate staging Pages repository for true pre-production browser testing.
8. Wait for GitHub **Actions → pages build and deployment** to finish. Hard refresh the browser.

## Test after merge
- `/index.html`: dark Forecast Lab feature below opening headline, direct launch CTA, three matchup statuses.
- `/forecast-lab.html`: existing model trains, selectors update outputs, chart and MAE/MAPE render.
- `/intelligence-lab.html`: product overview and navigation both work.
- `/schedule.html`, `/standings.html`, `/bracket.html`, `/boxscore.html`, `/cambridge-ithaca-boxscore.html`, `/backbay-hanover-boxscore.html`: existing content remains.
- Every page: `Forecast Labs` menu opens/closes with mouse, keyboard Escape and mobile menu.
- Week 2 and Week 3 remain research-only (not falsely marked live).

## Rollback
Use the GitHub commit history to revert the merge commit. Keep the original repository ZIP you uploaded to ChatGPT as a separate backup.

## Important
The navigation uses root-absolute URLs (`/forecast-lab.html`) appropriate for this user-site domain `daramoladoes.github.io`; it is not intended to be deployed under a GitHub Pages project subpath without URL adjustments. No new live model, API, or validation results are claimed.
