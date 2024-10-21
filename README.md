# DSA

A collection of essential Data Structures and Algorithms implemented in Python.

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
