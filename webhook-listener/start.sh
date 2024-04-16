#!/bin/bash
echo "=====[WEBHOOK LISTENER]====="
echo "Startup checks...."
if [ -z "$SERVER_API_KEY" ]; then
    echo "Error: SERVER_API_KEY environment variable is not set." >&2
    exit 1 # Exit code 1 for unset variable
fi
if [ -z "$SERVER_PORT" ]; then
    echo "Error: SERVER_PORT environment variable is not set." >&2
    exit 1 # Exit code 1 for unset variable
fi
echo " [OK] Config is valid"
echo "==============[CONFIG]==============="
echo " SERVER_PORT        : $SERVER_PORT"
echo "====================================="
echo "Starting webhook listener..."
set -x
gunicorn --bind=0.0.0.0:${SERVER_PORT} --workers=1 app:app
