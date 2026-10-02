# GitHub Pages deployment — Condo Price Board

This package is intended for the repository root of `DaramolaDoes/DaramolaDoes.github.io`.

## Deploy with GitHub's web interface

1. Download and extract `ChrionML-Real-Estate-Condo-Price-Board-Production-Upload.zip`.
2. Open the repository on GitHub and select **Add file → Upload files**.
3. Upload the extracted contents—not the enclosing folder—to the repository root.
4. Keep `assets/cml-logo.png` inside the `assets` folder.
5. Allow GitHub to replace matching production files, especially `boxscore.html`, `index.html`, `schedule.html`, `schedule-data.json`, and `README.md`.
6. Do not upload the ZIP file itself into the repository.
7. Use the commit title: `Release condo price board and transparent ZHVI methodology`.
8. Select **Commit changes**, wait for the Pages workflow in **Actions**, and complete the production checks below.

## Deploy with Git

Copy the extracted package contents into an existing local clone, then run:

```bash
git status
git add .
git commit -m "Release condo price board and transparent ZHVI methodology"
git push origin main
```

## Production checks

- `https://daramoladoes.github.io/boxscore.html` shows the stacked condo price board.
- Both **BOX SCORE** controls expand and display complete model statistics.
- `https://daramoladoes.github.io/` shows four published cities and Cambridge vs. Ithaca as the latest matchup.
- `https://daramoladoes.github.io/schedule.html` shows Weeks 1 and 2 as FINAL.
- Trend images and Zillow source links load correctly.
- Navigation works on desktop and mobile.

If an older page remains visible after the Pages build completes, perform a hard refresh (`Ctrl+Shift+R` on Windows or `Cmd+Shift+R` on macOS) or use a private browser window.

For detailed release contents and rollback guidance, read `RELEASE-NOTES.md` and `DEPLOYMENT-PRICE-BOARD.md`.
