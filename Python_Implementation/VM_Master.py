import subprocess
import time

result = subprocess.run(
    ['VBoxManage', 'list', 'vms'],
    capture_output=True,
    text=True,
)

VMS = []
vm = ""
flag = False
for i in result.stdout:
    
    if(i == '"'):
        if flag:
            VMS.append(vm)
            flag = False
            vm = ""
        else:
            flag = True

    else:
        if flag:
            vm += i

print("Available vm are: ", VMS)

def start_all():
    for vm in VMS:
        subprocess.run(["VBoxManage", "startvm", vm, "--type", "headless"])
        time.sleep(5)

def stop_all():
    for vm in VMS:
        subprocess.run(["VBoxManage", "controlvm", vm, "acpipowerbutton"])

def status():
    subprocess.run(["VBoxManage", "list", "runningvms"])

while True:
    print("1. Start all VMs")
    print("2. Stop all VMs")
    print("3. Status")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        start_all()
    elif choice == "2":
        stop_all()
    elif choice == "3":
        status()
    else:
        break