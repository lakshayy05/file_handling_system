# File Handling System 📂

A lightweight, command-line interface (CLI) tool built with Python to perform efficient file management operations. This project demonstrates core **CRUD (Create, Read, Update, Delete)** functionalities using Python's `pathlib` and `os` modules.

## 🚀 Features

* **File Creation:** Create new text files and write initial content immediately.
* **Read Functionality:** View the contents of existing files directly in the terminal.
* **Smart Updates:**
    * **Rename:** Change filenames easily.
    * **Overwrite:** Completely replace file content.
    * **Append:** Add new data to the end of a file without losing existing content.
* **Deletion:** Safely remove files from the directory.
* **Directory Listing:** Automatically lists all files in the current directory and subdirectories to help users select the correct file.

## 🛠️ Technologies Used

* **Language:** Python 
* **Modules:**
    * `pathlib` (For object-oriented filesystem paths)
    * `os` (For interacting with the operating system)

## 💻 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/LakshayGarg/File-Handling-System.git](https://github.com/LakshayGarg/File-Handling-System.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd File-Handling-System
    ```
3.  **Run the script:**
    ```bash
    python main.py
    ```

## 📖 Usage

Upon running the script, you will be presented with a menu:

1.  **Press 1** to Create a new file.
2.  **Press 2** to Read an existing file.
3.  **Press 3** to Update a file (Rename, Overwrite, or Append).
4.  **Press 4** to Delete a file.

Follow the on-screen prompts to enter file names and content. The system will automatically display the list of available files before every operation for convenience.

## 🔮 Future Improvements

* Implement exception handling for specific error types (e.g., `FileNotFoundError`).
* Add a Graphical User Interface (GUI) using Tkinter.
* Organize code into a class-based structure for better modularity.

## 👤 Author

**Lakshay Garg**
* [GitHub Profile](https://github.com/lakshayy05)

---
*This project is part of my journey in mastering Python and Software Development.*
