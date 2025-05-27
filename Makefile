ENV ?= local
-include config/.env.${ENV}
-include config/secrets/.env.*.${ENV}
export

lint:
	@poetry run black src/

run:
	@poetry run streamlit run src/linkedin_easy_apply_bot/frontend/login.py

init:
	@poetry install

%:
	@if [[ -f "scripts/${@}.sh" ]]; then bash scripts/${@}.sh; fi