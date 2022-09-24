#!/bin/bash

# Fail on errors.
set -e

# Go to the root.
cd "${0%/*}"

# Check if new translations were generated and exit on first difference.
ls "locale/" | while read lang; do
    python manage.py makemessages --no-obsolete --no-location --no-wrap -l "$lang"
    fname="locale/$lang/LC_MESSAGES/django.po"
    sed -i.bak '/"POT-Creation-Date:/d' "$fname"
    rm "${fname}.bak"
    unset GIT_DIR
    git diff --exit-code "$fname"
    # There should be exactly one match,
    matches=$(grep -c 'msgstr ""' "$fname")
    if [ "$matches" -ne 1 ]; then
        echo "Some of the messages are not translated:"
        grep -B 3 'msgstr ""' "$fname"
        exit 1
    fi
done
