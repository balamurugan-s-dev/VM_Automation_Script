import subprocess
import time

result = subprocess.run(
    ['VBoxManage', 'list', 'vms'],
    capture_output=True,
    text=True,
)

# print(result.stdout)

vms = []
flag = False
vm = ""

for i in result.stdout:
    if(i == '"'):
        if flag:
            vms.append(vm)
            flag = False
            vm = ""
        else:
            flag = True

    else:
        if flag:
            vm += i

# print(vms)
# ['UbuntuLST', 'test1', 'test2', 'test3', 'VPS']

# subprocess.run(["VBoxManage", "startvm", vms[1], "--type", "headless"])
# Waiting for VM "test1" to power on...
# VM "test1" has been successfully started.

# subprocess.run(["VBoxManage", "controlvm", vms[1], "acpipowerbutton"])