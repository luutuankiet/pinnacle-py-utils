#!/bin/bash

ENV_WORK_DIR=$(pwd)

# Function to initialize .env file
init_env() {
# Add more environment variables here if needed
    cat > ".env" <<EOENV
VIRTUAL_ENV="$ENV_WORK_DIR/.venv"
PYTHONPATH="$ENV_WORK_DIR/src"
EOENV
}

# Function to source .env file
source_env() {
    set -a  # Automatically export all variables
    source .env
    set +a  # Stop automatically exporting variables
}

# Invoke init_env and source_env functions
init_env
source_env

