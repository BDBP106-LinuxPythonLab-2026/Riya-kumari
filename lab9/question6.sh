#!/bin/bash
echo "HOME directory is"
echo "$HOME"

echo "Calculation:"
bc << EOF
scale=5
23934/44343
EOF

echo "files in HOME starting with D:"
ls "$HOME" | grep '^D'

echo "Lines containing my username in/etc/passwd:"
grep "$USER" /etc/passwd


