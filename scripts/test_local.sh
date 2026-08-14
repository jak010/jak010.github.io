#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -e

echo "======================================"
echo "Running local tests before pushing..."
echo "======================================"

echo "[1/3] Checking formatting and CSS linting (npm run lint)..."
npm run lint

echo "[2/3] Running Jekyll build (bundle exec jekyll build)..."
bundle exec jekyll build

echo "[3/3] Running Accessibility tests (bundle exec rspec)..."
bundle exec rspec

echo "======================================"
echo "✅ All tests passed successfully!"
echo "======================================"
