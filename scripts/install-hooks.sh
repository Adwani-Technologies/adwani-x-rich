#!/bin/bash
# Run once after cloning: bash scripts/install-hooks.sh

HOOK_DIR="$(git rev-parse --git-dir)/hooks"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cp "$SCRIPT_DIR/pre-commit" "$HOOK_DIR/pre-commit"
chmod +x "$HOOK_DIR/pre-commit"

echo "Git hooks installed. You're protected from committing media files."
