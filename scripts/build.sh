#!/bin/sh
# Builds the manual from the versioned sources and validates it:
#   dist/exelearning-manual-es.elpx  project package (content.xml, content/resources, theme…)
#   dist/site/                       HTML5 website exported with the eXeLearning CLI
# Needs Docker, zip, unzip, perl and python3. Usage: scripts/build.sh
set -eu
cd "$(dirname "$0")/.."

IMAGE="${EXELEARNING_IMAGE:-exelearning/exelearning:v4.0.5}"
NAME=exelearning-manual-es

rm -rf dist
mkdir dist

set -- content.xml
for path in content/resources theme custom screenshot.png; do
    if [ -e "$path" ]; then set -- "$@" "$path"; fi
done
zip -qrX "dist/$NAME.elpx" "$@" -x '*.DS_Store'

# The CLI image runs as a non-root user that must be able to write the export.
chmod 777 dist
docker run --rm -v "$PWD/dist:/data" "$IMAGE" \
    bun cli elp:export "/data/$NAME.elpx" /data/site --format=html5
unzip -q dist/site.zip -d dist/site
rm dist/site.zip

# ponytail: works around three bugs of the eXeLearning 4.0.5 CLI exporter; drop each fix when
# the pinned image no longer needs it (scripts/check.py fails if one comes back):
# 1. names with spaces linked as content/resources/resources/ (fixed upstream in exelearning#2480);
# 2. the 3dmol iDevice linked by its CSS class (idevices/dmole/) instead of its folder (exelearning#2543);
find dist/site -name '*.html' -exec perl -pi -e '
    s#content/resources/resources/#content/resources/#g;
    s#idevices/dmole/dmole\.#idevices/3dmol/3dmol.#g;
    s#idevices/dmole/#idevices/3dmol/#g;
    s#idevice_node dmole"#idevice_node 3dmol"#g;
    s#data-idevice-type="dmole"#data-idevice-type="3dmol"#g;
' {} +
# 3. Mermaid diagrams it cannot pre-render are left for libs/mermaid/, which it never exports (exelearning#2544).
if grep -rlq 'class="mermaid"' dist/site --include='*.html'; then
    mkdir -p dist/site/libs/mermaid
    docker run --rm --entrypoint cat "$IMAGE" /app/public/app/common/mermaid/mermaid.min.js \
        > dist/site/libs/mermaid/mermaid.min.js
fi

python3 scripts/check.py "dist/$NAME.elpx" dist/site
