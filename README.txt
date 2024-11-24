# ContextMenuFixer

**ContextMenuFixer** is a Python tool designed to repair and restore Windows right-click context menus by fixing registry entries, clearing icon caches, and running system file checks. Easily restore your context menus with administrative privileges.

## Why This Script Was Made

Over time, Windows context menus can become cluttered or malfunction due to corrupted registry entries, incomplete installations of software, or system file issues. These problems can hinder productivity and user experience. **ContextMenuFixer** was created to address these issues efficiently.

## Purpose

The purpose of **ContextMenuFixer** is to:

- Backup current registry settings related to context menus.
- Apply necessary registry fixes to restore right-click functionality.
- Clear the Windows icon cache to ensure icons display correctly.
- Run the System File Checker to repair corrupted system files.
- Provide a seamless experience for users to fix context menu issues without manual registry editing.

## How It Was Made

The script utilizes Python's `winreg` module to interact with the Windows Registry, `ctypes` for administrative privilege checks, and `subprocess` to execute system commands. By automating these tasks, **ContextMenuFixer** simplifies the repair process for users experiencing right-click menu issues.

## How to Use It

### **Requirements**

Ensure you have Python installed on your system. If not, download it from [Python.org](https://www.python.org/downloads/).

### **Installation & Setup**

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/ContextMenuFixer.git
    ```
2. **Navigate to the Directory:**
    ```bash
    cd ContextMenuFixer
    ```
3. **(Optional) Create a Virtual Environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

### **Running the Script**

1. **Run the Script with Administrative Privileges:**
    ```bash
    python fix_right_click_menu.py
    ```
2. **Follow the On-Screen Instructions:**
    - The script will create a backup of relevant registry keys.
    - Apply registry fixes.
    - Clear the icon cache.
    - Run the System File Checker.
    - Prompt to restart your computer.

## Customer Usage Example

**Scenario:** A user notices that the "New" option is missing from the right-click context menu on the desktop, disrupting their workflow.

**Solution:**

1. Download **ContextMenuFixer** from the GitHub repository.
2. Run the script with administrative privileges.
3. Follow the prompts to backup registry settings and apply fixes.
4. Restart the computer when prompted.

After these steps, the user observes that the "New" option is restored in the context menu, resolving the issue and restoring normal functionality.

---

**Note:** Always ensure you understand the changes being made to your system. It's recommended to create backups before performing system modifications.