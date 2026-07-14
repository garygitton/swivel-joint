# Load environment variables
-include .env
-include .env.local

.PHONY: start test install

# Fallback default port if not defined in env files
PORT ?= 3018

start:
	@echo "Starting local server on http://localhost:$(PORT)"
	python3 -m http.server -d src $(PORT)

test:
	@echo "Running Playwright UI tests..."
	python3 tests/test.py

install:
	@echo "Installing test dependencies..."
	pip install playwright
	playwright install chromium
