# HH.ru Automated Job Search Script

This Python script automates the process of searching and selecting job candidates on [HH.ru](https://hh.ru/). The script uses `pyautogui` to interact with the web interface and `keyboard` to control the script execution. It searches for job listings based on the specified criteria and interacts with the page to save candidates to favorites.

## Features

- **Automated browser interaction**: Opens Microsoft Edge, navigates to HH.ru, and performs searches.
- **Image recognition**: Locates UI elements on the screen using images stored locally.
- **Automated interaction**: Clicks buttons, scrolls through pages, and saves candidates to favorites.
- **Keyboard control**: Stops the script when the `Esc` key is pressed.

## Requirements

- Python 3.x
- `keyboard`
- `pyautogui`
- `pyscreeze`
- Microsoft Edge

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/hh-ru-automation.git
    cd hh-ru-automation
    ```

2. **Install the required Python packages**:

    ```bash
    pip install keyboard pyautogui pyscreeze
    ```

3. **Prepare your environment**:

    - Ensure Microsoft Edge is installed on your system.
    - Place the required image files (e.g., `log_in.png`, `search.png`, etc.) in a directory named `Letters` within the script's directory.

## Usage

1. **Run the script**:

    ```bash
    python hh_ru_automation.py
    ```

2. **Script Flow**:
    - The script will open Microsoft Edge and navigate to HH.ru.
    - It will perform a search based on a predefined job title (e.g., "programmer").
    - The script interacts with the job listings, adding them to favorites.
    - The script continues to operate until the `Esc` key is pressed or a predefined limit is reached.

3. **Stopping the script**:
    - Press the `Esc` key to stop the script at any time.

## Customization

- **Search Criteria**: You can modify the search keyword directly in the script at the line:

    ```python
    pgui.write('programmer')
    ```

- **Image Files**: Ensure all image files required for locating UI elements (e.g., `log_in.png`, `search.png`) are correctly named and located in the `Letters` folder.

## Error Handling

The script includes basic error handling:
- If the required UI elements are not found, the script will print an error message and attempt to continue.
- If a critical error occurs, the script will terminate and display the error details.

## Notes

- The script uses `pyautogui` for GUI automation, which relies on pixel-based image recognition. Ensure that the images used for matching are clear and accurately represent the UI elements.
- The script assumes that the HH.ru website's layout remains consistent. If the site layout changes, you may need to update the images or adjust the script accordingly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, feel free to open an issue or contact [ghaith.toutanji@yandex.com](mailto:your-email@example.com).

