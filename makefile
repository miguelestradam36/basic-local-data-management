##############################################################################################
# Variables
##############################################################################################

current_dir := $(realpath .)
SETUP_PATH = ${current_dir}/setup_.py
APP_PATH = ${current_dir}/main.py

##############################################################################################
# Automated actions
##############################################################################################

automated-push: ## Automated push
	@echo "Automated push to dev branch to origin"
	@git fetch origin/main
	@git add .
	@git commit -m "AUTOMATED ACTION: Saving changes..."
	@git push -u origin main


##############################################################################################
# Commands
##############################################################################################

.PHONY: create-venv 
create-venv: ## Create pyvenv
	@echo Builiding Python Virtual Environment...
	@python -m venv venv
	@echo.

