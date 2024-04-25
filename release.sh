#!/bin/bash
version_old=$(git describe --tags --abbrev=0)
if [ "$version_old" == "v$1" ]; then
    echo "Error: you did not change the version! Please check the __version__ in your __init__.py"
    exit 1
fi
echo "Creating new release: $version_old -> v$1"
git add .
git commit -m "Bumpversion $version_old -> v$1"
git push
git tag -a "v$1" -m "Release v$1"
git push origin "v$1"