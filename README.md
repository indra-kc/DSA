# DSA

A collection of essential Data Structures and Algorithms implemented in Python.


# Contributing Guide

Thank you for considering contributing! Here’s a quick guide to get you started:

## Steps to Contribute

1. **Fork the Repository**  
   Click the "Fork" button on the repository page to create a copy in your GitHub account.

2. **Clone the Repository**  
   ```bash
   git clone https://github.com/indra-kc/DSA.git

   ## Create a branch

Change to the repository directory on your computer (if you are not already there):

```bash
cd DSA
```

Now create a branch using the `git switch` command:

```bash
git switch -c your-new-branch-name
```

For example:

```bash
git switch -c add-graph-xy
```

## Make necessary changes and commit those changes

Now commit those changes using the `git commit` command:

```bash
git commit -m "your-changes-here."
```



## Push changes to GitHub

Push your changes using the command `git push`:

```bash
git push -u origin your-branch-name
```



# Installing Python on Ubuntu

Follow these steps to install Python on Ubuntu.

## Steps to Install Python

Open a terminal and run the following commands:

```sh
# 1. Update Package List
sudo apt update

# 2. Install Python
sudo apt install python3

# 3. Verify the Installation
python3 --version

# 4. Install pip (Python Package Installer)
sudo apt install python3-pip

# 5. Verify pip Installation
pip3 --version
```

# for running

```sh
python3 index.py
```

# Installing Python on Windows

Follow these steps to install Python on Windows.

## Steps to Install Python

1. **Download Python Installer**:
   - Go to the official Python website: [python.org/downloads](https://www.python.org/downloads/).
   - Download the latest version of Python for Windows.

2. **Run the Installer**:
   - Open the downloaded installer.
   - **Important**: Check the box **"Add Python to PATH"** before clicking "Install Now."

3. **Verify Python Installation**:
   - Open **Command Prompt** (Windows + R, type `cmd`).
   - Run the following command to verify the installation:
     ```sh
     python --version
     ```

4. **Install pip (Python Package Installer)**:
   - Pip is typically installed by default with Python. Verify it using:
     ```sh
     pip --version
     ```

   - If pip is not installed, you can manually install it by running:
     ```sh
     python -m ensurepip --upgrade
     ```

## Running Python Scripts

To run your Python script, use the command in **Command Prompt**:

```sh
python index.py
