# Import and Manage FBX Files in Blender

This script automates the process of importing, managing, and cleaning up `.fbx` files in Blender. It is useful for working with large sets of animations or objects where repetitive tasks need to be streamlined.

## Features

- Recursively searches for `.fbx` files in a specified folder and its subfolders.
- Imports `.fbx` files into Blender while:
  - Renaming animation actions based on the file paths.
  - Merging objects with unique animation actions.
  - Removing unused objects and orphaned data.
  - Cleaning up unwanted objects like those starting with "root." or "SK_Mannequin.".
- Globally removes animation actions containing a specific keyword.
- Binds all animation actions to a root object, if present.

## Prerequisites

- **Blender:** Ensure Blender is installed on your system.

## Usage

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   ```

2. **Open Blender:**
   - Open a new or existing project.

3. **Run the Script:**
   - Open the Blender Text Editor.
   - Load the script file (e.g., `import_manage_fbx.py`).
   - Update the `folder_path` variable to your `.fbx` files' folder path.
   - Press `Run Script` to execute.

4. **Review Outputs:**
   - Check the console for logs about imported objects, actions renamed, and objects removed.

## Script Configuration

- **Folder Path:**
  Update the `folder_path` variable in the script to point to your `.fbx` files directory.

  ```python
  folder_path = r"C:\Users\YourName\Path\To\Your\Folder"
  ```

- **Remove Actions with Keyword:**
  Modify the keyword in `remove_actions_with_keyword` to delete specific actions.

  ```python
  remove_actions_with_keyword("root.")
  ```

- **Binding Actions to Root:**
  Ensure the root object exists in the scene with the name "root" before running `bind_actions_to_root`.

## Notes

- **File Organization:** Ensure `.fbx` files are organized correctly in subfolders if needed.
- **Blender Version:** The script is designed for Blender's latest Python API. Compatibility with older versions may vary.
- **Testing:** Test the script on a small dataset before applying it to a large collection.

## Contribution

Feel free to fork this repository and submit pull requests for improvements or additional features. If you encounter any issues, please open an [issue](https://github.com/<your-username>/<your-repo-name>/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Blender Python API Documentation
- Community forums and tutorials for Blender scripting

---

**Enjoy automating your `.fbx` imports and management in Blender!**

