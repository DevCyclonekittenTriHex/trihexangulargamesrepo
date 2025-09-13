git pull
git lfs track "*.zip"
git lfs push --all origin main
git add .
git commit -m "lfs"
git push -u origin main