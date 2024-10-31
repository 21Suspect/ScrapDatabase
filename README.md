# Scrap Mechanic Item Database

![Screenshot](https://github.com/21Suspect/ScrapDatabase/raw/main/ScrapDatabase.jpg)

This project is a GUI-based application for managing and searching through item databases in the game Scrap Mechanic. It allows users to load JSON item data, search through various attributes, filter items, and save or manage the data in an intuitive interface.

## Features
- **Load JSON Files**: Load item databases from specified directories (`Creative` and `Survival` paths).
- **Search Functionality**: Search through item attributes including name, UUID, color, physics material, etc., with a dynamic filter that updates in real-time.
- **Sortable Columns**: Columns in the item list can be sorted by clicking on the headers, making it easy to organize and filter data.
- **Column Visibility Management**: Show or hide specific columns to tailor the view to your needs.
- **Copy to Clipboard**: Double-click on an item to copy specific information to the clipboard.
- **Settings Window**: Update the paths for loading item data directly from the settings window.
- **Save to JSON**: Save the current list of items back into a JSON file for future use.
- **Appearance Mode**: Toggle between light, dark, and system appearance modes.

## Requirements
- **Python 3.8+**
- **customtkinter**: This project uses `customtkinter` for an improved UI appearance and additional widgets. Install via:
  ```sh
  pip install customtkinter
  ```

## How to Run
1. **Clone the Repository**
   ```sh
   git clone https://github.com/21Suspect/ScrapDatabase.git
   ```
2. **Install Dependencies**
   ```sh
   pip install customtkinter
   ```
3. **Run the Script**
   ```sh
   python main.py
   ```

## Download ScrapDatabase Executable

You can download the compiled executable version of ScrapDatabase if you prefer not to run the Python script. This version does not require Python to be installed and can be run directly on your Windows system.

- **[Download ScrapDatabase.exe](https://github.com/21Suspect/ScrapDatabase/releases/download/v1.0/ScrapDatabase.exe)**

## Usage
- **Loading Items**: The program will load items from the specified `paths` variable in the script. You can modify these paths manually in the script or through the settings window within the application.
- **Searching**: Enter a search term in the search bar to filter items based on different attributes (e.g., name, UUID, material).
- **Sorting and Filtering**: Click on column headers to sort items. Right-click to manage which columns are visible.
- **Save Functionality**: Click the "Save Items" button to export the current view of the items into a JSON file.
- **Viewing Original Code**: Select an item and click on "Show Original Code" to see the JSON representation of that item.

## Project Structure
- **main.py**: The main script containing all the functionality of the application, including GUI setup, data loading, and event handling.
- **.idea/**: PyCharm configuration files.

## Notes
- **Compatibility**: This program is developed for Windows systems, as it uses specific file paths pointing to the `Scrap Mechanic` directories.
- **JSON Data**: Ensure that the paths provided in `paths` contain valid JSON files that match the expected structure for the program to function correctly.
- **Error Handling**: The program skips over JSON files with incorrect formatting or errors during parsing.

## Uploading ScrapDatabase.exe to GitHub
To upload the `ScrapDatabase.exe` file for others to download, follow these steps:

1. **Create a Release on GitHub**:
   - Go to your repository on GitHub.
   - Click on the **Releases** tab (usually found on the right side of the main page).
   - Click **Draft a new release**.
   - Fill in the **tag version** (e.g., `v1.0`), add a **title** (e.g., `Initial Release`), and provide a brief **description** of the release.
   - Click on **Attach binaries by dropping them here or selecting them** to upload `ScrapDatabase.exe`.
   - Finally, click **Publish release**.

2. **Link the Release**:
   - Once the release is published, you will get a download link for `ScrapDatabase.exe`. You can add this link to your README file for easy access.

## Contribution
Feel free to contribute to this project by forking the repository and submitting pull requests. If you encounter any issues, please open an issue in the GitHub repository.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
Created by **Fabian Vinke**.

