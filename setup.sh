#!/bin/bash

# setup.sh

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Please install it first."
    exit 1
fi

# Install dependencies
echo "Installing dependencies using Poetry..."
poetry install

echo "Setup complete. You can now run the unit converter."

