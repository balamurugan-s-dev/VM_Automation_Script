# 🖥️ VirtualBox VM Manager

A lightweight Python automation tool designed to manage multiple Oracle VirtualBox Virtual Machines (VMs) simultaneously. It includes a Windows Batch wrapper for easy one-click execution.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![VirtualBox](https://img.shields.io/badge/VirtualBox-VBoxManage-orange?style=flat&logo=virtualbox)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat&logo=windows)

## 📖 Overview

This tool interacts with the `VBoxManage` command-line interface to auto-detect installed VMs. It provides a simple CLI menu to:

* **Start all VMs** in "Headless" mode (background, no GUI).
* **Stop all VMs** gracefully using ACPI shutdown signals.
* **Check the status** of currently running VMs.

This is particularly useful for users running local home labs or multiple server environments who need to spin up or shut down their entire infrastructure quickly.

---

## ⚙️ Prerequisites

Before running this script, ensure you have the following installed:

1. **Python 3.x**: [Download Python](https://www.python.org/downloads/)
2. **Oracle VirtualBox**: [Download VirtualBox](https://www.virtualbox.org/)
3. **Environment Variables**:
   * Ensure `VBoxManage` is added to your system's `PATH` variable.
   * *Test:* Open a terminal and type `VBoxManage --version`. If it returns a version number, you are good to go.

---

## 📂 File Structure

* `VM_Master.py`: The core logic script that parses VM lists and handles execution.
* `launcher.bat`: A Windows batch file to easily run the Python script without opening a terminal manually.

---

## 🚀 Usage

### Option 1: The Quick Way (Windows)
Double-click the `launcher.bat` file included in the repository. This will automatically locate the Python script and launch the menu.

### Option 2: Command Line
Open your terminal or command prompt in the project directory and run:

```bash
python VM_Master.py
```

---

## 🕹️ Menu Options
When the script runs, you will see the following numeric options:
1. **Start all VMs**
    * *Iterates through your specific VM list.*
    * *Starts them with ```--type headless.```*
    * *Note: Adds a 5-second delay between starts to prevent system resource spikes.*
2. **Stop all VMs**
    * *Sends an ```acpipowerbutton``` signal to all VMs.*
    * *This mimics pressing the physical power button, allowing the OS to shut down safely.*
3. **Status**
    * *Lists the names and UUIDs of currently running VMs.*
4. **Exit**
    * *Closes the script.*

---

## 🛠️ Troubleshooting
Error: ```'VBoxManage' is not recognized...```

* This means VirtualBox is not in your System Path.
* **Fix:** Add ```C:\Program Files\Oracle\VirtualBox``` (or your specific installation path) to your Windows Environment Variables.

Error: ```Python not found```

* **Fix:** Ensure you have checked "Add Python to PATH" during the Python installation process.

---

## 📝 License
This project is open-source and available for personal or educational use.