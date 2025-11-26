#!/bin/bash

# This script sets up the MkDocs site with the material theme,
# and renames the chapter files to have leading zeros for correct ordering.

# Exit on any error
set -e

# 1. Create a dummy source_chapters directory for demonstration
# echo "Creating dummy source_chapters directory..."
# mkdir -p source_chapters
# for i in {1..30}; do
#     echo "# Chapter $i" > "source_chapters/chapter_$i.md"
# done
# echo "Dummy source_chapters directory created."

# 2. Install dependencies
echo "Installing MkDocs and MkDocs-Material theme..."
pip install mkdocs mkdocs-material

# 3. Create the directory structure
echo "Creating docs/test directory..."
mkdir -p docs/test

# 4. Copy and rename chapter files
# echo "Copying and renaming chapter files..."
# for i in {1..30}; do
#     # Zero-pad the chapter number
#     printf -v padded_i "%02d" "$i"
    
#     # Source and destination file paths
#     src_file="source_chapters/chapter_$i.md"
#     dest_file="docs/AIIMS-PSW/chapter_$padded_i.md"
    
#     if [ -f "$src_file" ]; then
#         echo "Copying $src_file to $dest_file"
#         cp "$src_file" "$dest_file"
#     else
#         echo "Warning: $src_file not found."
#     fi
# done

# 5. Create mkdocs.yml
echo "Creating mkdocs.yml..."
cat <<EOL > mkdocs.yml
site_name: My Docs
theme:
  name: material
  custom_dir: overrides
  palette:
    # Palette toggle for light mode
    - scheme: default
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode

    # Palette toggle for dark mode
    - scheme: slate
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.footer
    - navigation.tabs
    - navigation.top
EOL

# 6. Create docs/index.md
echo "Creating docs/index.md..."
cat <<EOL > docs/index.md
# Welcome to My Docs

This is the homepage for your MkDocs site.
EOL

# 7. Create custom footer
echo "Creating custom footer..."
mkdir -p overrides/partials
cat <<EOL > overrides/partials/copyright.html
<div class="md-copyright">
  <div class="md-copyright__highlight">
    Your custom text here
  </div>
</div>
EOL

echo "Setup complete. You can now run 'mkdocs serve' to see your site."
