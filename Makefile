VENV=.venv/bin
NPM=node_modules/.bin
REQUIREMENTS=$(wildcard requirements.txt)
MARKER=.initialized-with-makefile
VENVDEPS=$(REQUIREMENTS setup.py)
NPMDEPS=$(package-lock.json)

$(VENV):
	python3 -m venv .venv
	$(VENV)/python3 -m pip install --upgrade pip

$(VENV)/$(MARKER): $(VENVDEPS) | $(VENV)
	$(VENV)/pip install $(foreach path,$(REQUIREMENTS),-r $(path))
	touch $(VENV)/$(MARKER)

# $(NPM): $(NPMDEPS)
# 	npm install

# .PHONY: venv npm install clean test-android test-ios

install: $(VENV)/$(MARKER)
# npm: $(NPM)

# install: npm venv

test: 
	npx percy exec -- $(VENV)/python3 tests/test.py

after-test:
	npx percy exec -- $(VENV)/python3 tests/after_test.py