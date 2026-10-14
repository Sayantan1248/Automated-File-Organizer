# File System Organizer

A lightweight Python automation tool that automatically scans, sorts, and declutters directories by organizing files into categorized subfolders based on their extensions.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

##  Key Features

- **Automated Routing:** Classifies files into structured categories (`Images`, `Documents`, `Archives`, `Media`, `Code`, `Others`).
- **Safety Checks:** Verifies directory existence and ignores subdirectories to avoid recursive moving errors.
- **Dynamic Folder Creation:** Automatically creates target subdirectories only when matching files are detected.
- **Cross-Platform:** Built using standard Python library modules, fully compatible with Windows, macOS, and Linux.

---

## 🛠️ Built With

* **[Python](https://www.python.org/)** — Core programming language.
* **`pathlib`** — Modern, object-oriented file system path management.
* **`shutil`** — High-level file operations and directory handling.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher installed on your system. No third-party packages are required (`pathlib` and `shutil` are included in the Python Standard Library).

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/file-organizer-python.git](https://github.com/your-username/file-organizer-python.git)
   cd file-organizer-python
