# MAKE GNU :penguin:

## Install `make` into your computer

### Only for Windows visitors

For more information about how to install Makefile into your computer, direct to:

- For a more detailed description: [Chocolatey Overview Repo](https://github.com/miguelestradam36/chocolatey-for-windows)
- For a quick set-up: [Other project that uses Chocolatey and Make GNU](https://github.com/miguelestradam36/python-skillset-01)

### For Linux and MacOS visitors

For the **MacOS** option, you will have to download a package manager as with Windows.

#### For Linux users

```bash
#Update the package installer
sudo apt-get update
#Make sure you have the build-essentials package to make use of tools like:
#GCC for example.
sudo apt-get install build-essential

#At last, let's be 100% sure.
sudo apt-get -y install make
```

#### For MacOS users

```bash
#Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
#Run this command
brew install make
```