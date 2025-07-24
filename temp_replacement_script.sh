#!/bin/bash

# Script to replace uppercase tags with lowercase equivalents

# Define replacement patterns
declare -A replacements=(
    ["[Artificial General Intelligence]"]="[artificial general intelligence]"
    ["[Machine learning]"]="[machine learning]"
    ["[Software development]"]="[software development]"
    ["[Programming]"]="[programming]"
    ["[Wikipedia]"]="[wikipedia]"
    ["[ChatGPT]"]="[chatgpt]"
    ["[Note taking]"]="[note taking]"
    ["[Processes]"]="[processes]"
    ["[General]"]="[general]"
    ["[Teamwork]"]="[teamwork]"
    ["[Time management]"]="[time management]"
    ["[Neurosciences]"]="[neurosciences]"
    ["[Python]"]="[python]"
    ["[Questions]"]="[questions]"
    ["[Investing]"]="[investing]"
    ["[DevOps]"]="[devops]"
    ["[Intelligence Augmentation]"]="[intelligence augmentation]"
)

# Find all markdown files and apply replacements
find /home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content -name "*.md" -type f | while read file; do
    for old_pattern in "${!replacements[@]}"; do
        new_pattern="${replacements[$old_pattern]}"
        if grep -q "tag: $old_pattern" "$file" 2>/dev/null; then
            echo "Updating $file: $old_pattern -> $new_pattern"
            sed -i "s|tag: $old_pattern|tag: $new_pattern|g" "$file"
        fi
    done
done