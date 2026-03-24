#!/usr/bin/env bash
# Hook script: blocks agent from editing auto-generated migration files.
# Expects JSON on stdin from VS Code PreToolUse hook event.

set -euo pipefail

INPUT=$(cat)

# Extract file path from toolInput (handles both filePath and path keys)
FILE=$(echo "$INPUT" | python3 -c "
import sys, json
d = json.load(sys.stdin)
ti = d.get('toolInput', {})
print(ti.get('filePath', ti.get('path', '')))
" 2>/dev/null || echo "")

# Check if file is an auto-generated migration (numbered migration files)
if echo "$FILE" | grep -qE '/migrations/[0-9]'; then
  cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Migration files are auto-generated. Use the migration-writer agent instead of editing manually."}}
EOF
else
  cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"allow"}}
EOF
fi
