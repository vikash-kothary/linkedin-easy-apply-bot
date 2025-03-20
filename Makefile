ENV ?= local
-include config/.env.${ENV}
-include config/secrets/.env.*.${ENV}
export

lint:
	@.venv/bin/black src/

run:
	@.venv/bin/python3 src/easyapplybot.py

init:
	@python3 -m venv .venv
	@.venv/bin/pip3 install black pandas
	@.venv/bin/pip3 install -r src/requirements.txt
	@.venv/bin/pip3 install ./webdriver_manager
