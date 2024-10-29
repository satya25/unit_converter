#!/bin/bash

# project_clean_up.sh

# Remove Python cache directories
echo "Cleaning up Python cache files..."
find . -type d -name '__pycache__' -exec rm -rf {} +

# Remove compiled Python files
echo "Removing compiled Python files..."
find . -type f -name '*.pyc' -exec rm -f {} +

# Remove virtual environment if it exists
if [ -d "venv" ]; then
    echo "Removing virtual environment..."
    rm -rf venv
fi

# Optionally, remove other temporary files or directories
# Uncomment and modify the following lines as needed
# echo "Removing temporary files..."
# rm -rf temp/

echo "Cleanup complete."