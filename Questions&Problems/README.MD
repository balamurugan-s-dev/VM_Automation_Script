# 🖥️ VirtualBox VM Manager

A lightweight Python automation tool to manage multiple Oracle VirtualBox Virtual Machines (VMs) using `VBoxManage`.  
Designed for **headless environments**, home labs, and server-style VM management.


## 📌 Features

- Auto-detects all registered VirtualBox VMs
- Start VMs in **headless mode**
- Gracefully stop VMs using **ACPI shutdown**
- Designed for automation (CLI / scripts)
- No GUI dependency for normal operation


## ⚙️ Prerequisites

- **Oracle VirtualBox** installed
- `VBoxManage` available in system PATH
- **Python 3.x**
- Host OS: Windows (tested)

Verify:
```bash
VBoxManage --version
python --version
````


## 🧠 How It Works

The script:

- Uses ```VBoxManage list vms``` to fetch all registered VMs
- Parses VM names from the output
- Executes:
    - ```VBoxManage startvm <vm> --type headless```
    - ```VBoxManage controlvm <vm> acpipowerbutton```

**Example VM detection output:**
```bash
    "UbuntuLST" {uuid}
    "test1"     {uuid}
    "test2"     {uuid}
    "test3"     {uuid}
    "VPS"       {uuid}
```

## ▶️ Starting a VM (Headless)

```bash
    subprocess.run([
        "VBoxManage",
        "startvm",
        "test1",
        "--type",
        "headless"
    ])
```

**Result:**
```bash
    Waiting for VM "test1" to power on...
    VM "test1" has been successfully started.
```

## ⏹️ Stopping a VM (Graceful)

```bash
    subprocess.run([
        "VBoxManage",
        "controlvm",
        "test1",
        "acpipowerbutton"
    ])
```
This sends a virtual power button press to the guest OS.


## ⚠️ Important: ACPI Shutdown Issue (GUI VMs)
**❌ Problem**

Some VMs do not shut down when using:
```bash
    VBoxManage controlvm <vm> acpipowerbutton
```

**This happens when:**
- A GUI is installed inside the VM
- VM boots to graphical.target
- VM is started in headless mode
- No user is logged in

**In this state:**
- The display manager owns power handling
- No active user session exists
- ACPI shutdown request is ignored

**You may notice:**
- VM only shuts down after opening GUI
- Or only works after logging in
- GUI shutdown button may appear but does nothing


## ✅ Correct Solution (Recommended)

Configure the VM to boot into CLI first, like a server.

**Inside the guest OS:**
**1️⃣ Switch default target to CLI**
```bash
    sudo systemctl set-default multi-user.target
```

**2️⃣ (Optional but recommended) Disable display manager**
```bash
    sudo systemctl disable gdm
    # or lightdm / sddm depending on distro
```

**3️⃣ Reboot the VM**
```bash
    sudo reboot
```


## 🎯 Result After Fix
- VM starts headless
- No GUI session dependency
- ```acpipowerbutton``` works immediately
- No need to open VirtualBox GUI
- Clean and reliable shutdown

This makes the VM behave like a real headless server.


## ❗ What NOT to Do
Avoid using:
```bash
    VBoxManage controlvm <vm> poweroff
```
This is a hard power cut and can corrupt the VM.


## 🧩 Why Other CLI VMs Worked Fine
CLI-only VMs:
- Boot into multi-user.target
- Use systemd directly for power events
- Do not depend on GUI or user sessions

Hence, ACPI shutdown works instantly.


## 🧪 Tested Scenario

- Host: Windows
- VirtualBox: 7.x
- Guest OS: Linux (CLI & GUI variants)
- Mode: Headless


## 📜 License
This is only for educational purpose. Use, modify, and automate freely.
