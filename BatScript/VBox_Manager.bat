@echo off
title VirtualBox VM Manager
color 0A

:menu
cls
echo ===============================
echo   VirtualBox VM Manager
echo ===============================
echo.
echo 1. Start ALL VMs (headless)
echo 2. Stop ALL VMs (safe shutdown)
echo 3. Show running VMs
echo 4. Exit
echo.

set /p choice=Choose an option: 

if "%choice%"=="1" goto start
if "%choice%"=="2" goto stop
if "%choice%"=="3" goto status
if "%choice%"=="4" exit
goto menu

:start
echo.
echo Starting all VMs...
for /f "tokens=1 delims={" %%A in ('VBoxManage list vms') do (
    VBoxManage startvm %%A --type headless
    timeout /t 5 >nul
)
echo.
echo All VMs started
pause
goto menu

:stop
echo.
echo Sending shutdown signal to running VMs...
for /f "tokens=1 delims={" %%A in ('VBoxManage list runningvms') do (
    VBoxManage controlvm %%A acpipowerbutton
)
echo.
echo Shutdown signal sent
pause
goto menu

:status
echo.
echo Running VMs:
VBoxManage list runningvms
pause
goto menu
