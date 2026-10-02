# GitHub Pages deployment — Condo Price Board

Target repository: `https://github.com/DaramolaDoes/DaramolaDoes.github.io`

Production URL: `https://daramoladoes.github.io/boxscore.html`

## Option A — GitHub website upload

1. Download and extract `ChrionML-Real-Estate-Condo-Price-Board-Production-Upload.zip`.
2. Open the target GitHub repository and select **Add file → Upload files**.
3. Open the extracted folder and upload its contents—not the enclosing folder—to the repository root.
4. Allow GitHub to replace files with matching names, including `boxscore.html`, `index.html`, `schedule.html`, `schedule-data.json`, and `README.md`.
5. Do not upload the production ZIP itself into the repository.
6. Use the commit title: `Release condo price board and transparent ZHVI methodology`.
7. Optional extended description: `Adds the stacked weekly condo price board, expandable model statistics, Week 2 research, and corrected Zillow/ChrionML data provenance language.`
8. Commit directly to `main`, or create a branch and pull request if you want a review checkpoint.

## Option B — Git command line

From a local clone of the repository, copy the extracted production files into the repository root, then run:

```bash
git status
git add .
git commit -m "Release condo price board and transparent ZHVI methodology"
git push origin main
```

## Production verification

After GitHub Pages finishes publishing, verify:

1. `https://daramoladoes.github.io/boxscore.html` displays the Real Estate Condo Price Board.
2. Cambridge vs. Ithaca and Boston vs. Providence appear as stacked matchup cards.
3. Each **BOX SCORE** control expands and collapses.
4. Model MAE tables and trend charts display correctly.
5. Zillow source links open the corresponding ZIP-code market pages.
6. The navigation links return to Research, Standings, and Schedule.
7. `https://daramoladoes.github.io/` displays four published cities, two applied ML projects, and Cambridge vs. Ithaca as the latest completed matchup.
8. `https://daramoladoes.github.io/schedule.html` shows both completed matchups as FINAL.

GitHub Pages commonly updates within a few minutes. If an older version remains visible, use a private browser window or perform a hard refresh with `Ctrl+Shift+R`.

## Rollback

If a production issue appears, open the repository's commit history, select the deployment commit, and use **Revert**. With Git locally, revert the release commit and push the new revert commit instead of rewriting repository history.
