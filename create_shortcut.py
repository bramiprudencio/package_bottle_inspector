import os
import sys
import platform

def create_linux_shortcut():
    desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
    project_dir = os.path.abspath(os.path.dirname(__file__))
    
    runner_sh_path = os.path.join(project_dir, 'run_app.sh')
    venv_act = os.path.join(project_dir, 'venv', 'bin', 'activate')
    
    # Create the shell script runner
    runner_content = f"""#!/bin/bash
cd "{project_dir}"
if [ -f "{venv_act}" ]; then
    source "{venv_act}"
fi
python3 main.py
"""
    with open(runner_sh_path, 'w') as f:
        f.write(runner_content)
    os.chmod(runner_sh_path, 0o755)

    # Create the .desktop file
    shortcut_content = f"""[Desktop Entry]
Name=Package Bottle Inspector
Comment=Run Package Bottle Inspector
Exec="{runner_sh_path}"
Icon=utilities-terminal
Terminal=true
Type=Application
Categories=Utility;
"""
    shortcut_path = os.path.join(desktop_dir, 'PackageBottleInspector.desktop')
    with open(shortcut_path, 'w') as f:
        f.write(shortcut_content)
    
    os.chmod(shortcut_path, 0o755)
    print(f"Linux executable created at: {runner_sh_path}")
    print(f"Linux desktop shortcut created at: {shortcut_path}")
    print("Note: On some Linux distributions, you may need to right-click the shortcut and select 'Allow Launching'.")

def create_windows_shortcut():
    try:
        # Try finding the Desktop folder
        desktop_dir = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    except KeyError:
        desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')

    project_dir = os.path.abspath(os.path.dirname(__file__))
    venv_bat = os.path.join(project_dir, 'venv', 'Scripts', 'activate.bat')
    
    # Create the batch script runner
    runner_bat_path = os.path.join(project_dir, 'run_app.bat')
    runner_content = f"""@echo off
cd /d "{project_dir}"
if exist "{venv_bat}" (
    call "{venv_bat}"
)
python main.py
exit
"""
    with open(runner_bat_path, 'w') as f:
        f.write(runner_content)
        
    # Create a temporary VBScript to create the .lnk file
    vbs_script = os.path.join(project_dir, 'create_lnk.vbs')
    lnk_path = os.path.join(desktop_dir, 'Package Bottle Inspector.lnk')
    
    vbs_content = f'''Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "{lnk_path}"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{runner_bat_path}"
oLink.WorkingDirectory = "{project_dir}"
oLink.Description = "Run Package Bottle Inspector"
oLink.Save
'''
    with open(vbs_script, 'w') as f:
        f.write(vbs_content)
    
    # Run the VBScript and then remove it
    os.system(f'cscript //Nologo "{vbs_script}"')
    
    if os.path.exists(vbs_script):
        os.remove(vbs_script)

    print(f"Windows batch runner created at: {runner_bat_path}")
    print(f"Windows shortcut (.lnk) created at: {lnk_path}")

if __name__ == '__main__':
    current_os = platform.system()
    try:
        print(f"Detected OS: {current_os}")
        if current_os == 'Linux':
            create_linux_shortcut()
        elif current_os == 'Windows':
            create_windows_shortcut()
        else:
            print(f"Unsupported OS for automated shortcut creation: {current_os}")
            print("Please create the shortcut manually.")
    except Exception as e:
        print(f"An error occurred while creating the shortcut: {e}")
