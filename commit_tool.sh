#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Check if a commit message was provided as an argument
if [ -z "$1" ]; then
  echo "Error: No commit message provided!"
  echo "Usage: ./commit_tool.sh \"Your commit message\""
  exit 1
fi

# Store the commit message from the user input
COMMIT_MESSAGE="$1"

# Pull the latest changes from the remote repository
echo "Pulling latest changes..."
git pull

# Stage all changes (modified, added, deleted files)
echo "Staging all changes..."
git add -A

# Commit the changes with the user-provided message
echo "Committing changes..."
git commit -m "$COMMIT_MESSAGE"

# Push the committed changes to the remote repository
echo "Pushing changes..."
git push

echo "Operation completed successfully!"
