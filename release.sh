#!/bin/bash
version_old=$(git describe --tags --abbrev=0)
if [ "$version_old" == "$1" ]; then
    echo "Error: you did not change the version! Please check the __version__ in your __init__.py"
    exit 1
fi
echo "Creating new release: $version_old -> $1"
git add .
git commit -m "Bumpversion $version_old -> $1"
git push
git tag -a "$1" -m "Release $1"
git push origin "$1"