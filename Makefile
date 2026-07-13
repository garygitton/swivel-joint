.PHONY: start test install

# Port for the local server
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
