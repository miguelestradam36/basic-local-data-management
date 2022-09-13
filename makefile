##############################################################################################
# Variables
##############################################################################################

current_dir := $(realpath .)
APP_PATH = ${current_dir}/app/src/main.py

##############################################################################################
# Commands
##############################################################################################

.PHONY: create-venv 
create-venv: ## Create pyvenv
	@echo Builiding Python Virtual Environment...
	@python -m venv app\venv
	@echo.

.PHONY: activate-venv
activate-venv: ## Activate pyvenv
	@echo Activating Python Virtual Environment...
	@app\venv\Scripts\activate.bat
	@echo.

.PHONY: application
application: ## Install requirements.txt into venv
	@echo Installing requirements to Python Virtual Environment...
	@app\venv\Scripts\python ${APP_PATH}
	@echo.

.PHONY: upgrade-venv-pip
upgrade-venv-pip: ## Upgrade or install pip inside venv
	@echo Updating and upgrading pip to Python Virtual Environment...
	@app\venv\Scripts\python -m pip install --upgrade pip
	@echo.

.PHONY: exit-venv
exit-venv: ## Exit the venv
	@echo Leaving Python Virtual Environment...
	@app\venv\Scripts\deactivate.bat
	@echo.

##############################################################################################
# Python Virtual Environment Test
##############################################################################################

.PHONY: test-build-venv
test-build-venv: ## Test the build of your venv
	@echo TESTING: Build of the Python Virtual Environment
	@venv\Scripts\pytest -q ${BUILD_TEST_PATH}
	@echo.

##############################################################################################
# Complex commands
##############################################################################################

.PHONY: build-venv
build-venv: create-venv upgrade-venv-pip activate-venv application test-build-venv exit-venv