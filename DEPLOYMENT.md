# Deploy ChrionML® Research Archive to GitHub Pages

Production repository: `https://github.com/DaramolaDoes/DaramolaDoes.github.io`

Release date: October 4, 2026

## Recommended deployment: Git

This method reliably preserves the nested research-page folders.

1. Download and extract `ChrionML-Research-Archive-Production-2026-10-04-Brand-Update.zip`.
2. Clone the production repository:

   ```bash
   git clone https://github.com/DaramolaDoes/DaramolaDoes.github.io.git
   cd DaramolaDoes.github.io
   ```

3. Copy **the extracted contents** into the cloned repository root. Do not copy the enclosing ZIP folder and do not delete unrelated repository files.
4. Confirm these paths exist before committing:

   ```text
   index.html
   standings.html
   schedule-data.json
   assets/archive.css
   research/index.html
   research/boston-vs-providence/index.html
   research/cambridge-vs-ithaca/index.html
   methodology/index.html
   about-olu-daramola/index.html
   ```

5. Review and commit:

   ```bash
   git status
   git add .
   git commit -m "Standardize ChrionML® brand across production site"
   git push origin main
   ```

6. Open the repository's **Actions** tab and wait for the GitHub Pages workflow to finish successfully.

## Browser-only GitHub deployment

1. Extract the ZIP on your computer. Do **not** upload the ZIP itself.
2. Open the repository and select **Add file → Upload files**.
3. Drag the extracted files and folders into the upload area. Confirm GitHub displays the nested `research`, `methodology`, `about-olu-daramola`, and `assets` paths.
4. Commit directly to `main` with:

   `Standardize ChrionML® brand across production site`

5. Wait for the Pages workflow under **Actions**.

If the browser does not preserve folders, use the Git method above.

## GitHub Pages settings

In **Settings → Pages**, confirm:

- Source: **Deploy from a branch**
- Branch: **main**
- Folder: **/(root)**

The package includes `.nojekyll`, which should remain in the repository root.

## Production verification

After deployment, verify:

- `https://daramoladoes.github.io/`
- `https://daramoladoes.github.io/research/`
- `https://daramoladoes.github.io/research/boston-vs-providence/`
- `https://daramoladoes.github.io/research/cambridge-vs-ithaca/`
- `https://daramoladoes.github.io/methodology/`
- `https://daramoladoes.github.io/about-olu-daramola/`
- `https://daramoladoes.github.io/standings.html`

Confirm that:

- Article section links scroll to Abstract, Research Goal, Results, Methods, Data Availability, Limitations, and References.
- Principal-finding panels use the light editorial treatment with readable dark text.
- The author appears as **Olu (Tim) Daramola**.
- Each abstract ends with its publication date.
- Standings display four city studies and the four research variables.
- The All Regions and East filters show four rows; unpublished regions show the empty state.
- Box Score buttons open the correct matchup.

If older content remains after the workflow succeeds, hard-refresh with `Ctrl+Shift+R` on Windows or `Cmd+Shift+R` on macOS.

## Rollback

Open the repository commit history, select the previous production commit, and use GitHub's **Revert** action if available. With Git locally, revert the new release commit and push the generated revert commit; do not force-push production history.
