import winreg
import ctypes
import sys
import subprocess
import os
from datetime import datetime
import time

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_backup():
    """Create a backup of relevant registry keys"""
    backup_dir = "registry_backup"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"registry_backup_{timestamp}.reg")
    
    try:
        subprocess.run([
            'reg', 'export',
            r'HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers',
            backup_file,
            '/y'
        ], check=True)
        print(f"Registry backup created at: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create backup: {e}")

def fix_registry():
    """Apply registry fixes for right-click menu"""
    try:
        # Fix New Menu Handler
        key_path = r'Directory\Background\shellex\ContextMenuHandlers\New'
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path) as key:
            winreg.SetValueEx(key, '', 0, winreg.REG_SZ, '{D969A300-E7FF-11d0-A93B-00A0C90F2719}')

        # Fix Directory Background
        key_path = r'Directory\Background\shell\New\command'
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path) as key:
            winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'explorer.exe shell:::{20D04FE0-3AEA-1069-A2D8-08002B30309D}')

        print("Registry fixes applied successfully")
        return True
    except Exception as e:
        print(f"Error fixing registry: {e}")
        return False

def clear_icon_cache():
    """Clear Windows icon cache"""
    try:
        # Stop Windows Explorer
        subprocess.run(['taskkill', '/F', '/IM', 'explorer.exe'], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL)
        
        # Clear icon cache
        cache_paths = [
            os.path.expanduser('~\\AppData\\Local\\Microsoft\\Windows\\Explorer\\iconcache*'),
            os.path.expanduser('~\\AppData\\Local\\IconCache.db')
        ]
        
        for path in cache_paths:
            try:
                subprocess.run(f'del /A /F /Q "{path}"', 
                             shell=True, 
                             stdout=subprocess.DEVNULL, 
                             stderr=subprocess.DEVNULL)
            except:
                pass
        
        # Restart Explorer
        subprocess.Popen('explorer.exe')
        print("Icon cache cleared successfully")
        return True
    except Exception as e:
        print(f"Error clearing icon cache: {e}")
        return False

def run_system_file_checker():
    """Run Windows System File Checker"""
    try:
        print("Running System File Checker (this may take several minutes)...")
        subprocess.run(['sfc', '/scannow'], check=True)
        print("System File Checker completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running System File Checker: {e}")
        return False

def main():
    try:
        if not is_admin():
            print("This script requires administrative privileges.")
            print("Please run this script as administrator.")
            print("\nPress Enter to exit...")
            input()
            sys.exit(1)

        print("Starting right-click menu repair process...")
        
        # Create backup
        print("\n1. Creating registry backup...")
        create_backup()
        
        # Apply registry fixes
        print("\n2. Applying registry fixes...")
        fix_registry()
        
        # Clear icon cache
        print("\n3. Clearing icon cache...")
        clear_icon_cache()
        
        # Run System File Checker
        print("\n4. Running System File Checker...")
        run_system_file_checker()
        
        print("\nAll repairs completed. Please restart your computer for changes to take effect.")
        restart = input("Would you like to restart now? (y/n): ").lower()
        if restart == 'y':
            subprocess.run(['shutdown', '/r', '/t', '0'])
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nPress Enter to exit...")
        input()

if __name__ == "__main__":
    main()