# pix2text-hotkey
A simple script to recognize formulas, pages, and text from clipboard images. <\br>
The recognized content is automatically copied to the clipboard in the appropriate format.

## Features

- **Formula**: Recognizes formulas from images and copies them to the clipboard in LaTeX format.
- **Page**: Recognizes full pages and copies them to the clipboard in Markdown format.
- **Text**: Recognizes plain text from images and copies it to the clipboard as plain text.

## Shortcuts

- `Ctrl + Alt + M`: Recognize and copy the formula in LaTeX format.
- `Ctrl + Alt + N`: Recognize and copy the page in Markdown format.
- `Ctrl + Alt + K`: Recognize and copy the text in plain text format.

## Installation

1. **Clone the repository** or download the Python script:
    ```
    git clone https://github.com/Raffo24/pix2text-hotkey.git
    cd pix2text-hotkey
    ```

2. **Install required dependencies**:
    The script requires several Python libraries. You can install them using the following command:
    ```
    pip install -r requirements.txt
    ```

3. **Run the script**:
    Execute the script using Python:
    ```
    python pix2text-hotkey.py
    ```

## Usage

1. Capture an image to your clipboard.
2. Use the appropriate shortcut to recognize and copy the content in the desired format.
3. Paste the content where needed.

## Dependencies

This script relies on the following Python libraries:
- `pix2text` (for OCR/HCR functionality)
- `Pillow` (for handling image data)
- `keyboard` (for hotkey support)
- `pyperclip` (for clipboard operations)

You can install them with:
```
pip install pix2text Pillow keyboard pyperclip
