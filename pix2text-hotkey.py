'''
@Author: Raffaele Ruggeri
@Date: 02 October 2024


Simple script to recognize formula, page and text from clipboard image.copy to clipboard
- The Formula will be copied in latex format
- The Page will be copied in markdown format
- The Text will be copied in plain text format
Shortcuts:
    ctrl + alt + m: recognize formula
    ctrl + alt + n: recognize page
    ctrl + alt + k: recognize text
'''

from pix2text import Pix2Text
from PIL import ImageGrab
import keyboard
import pyperclip

def copy_recognize_formula():
    image = ImageGrab.grabclipboard()
    if not image:
        print('No image found in clipboard')
        return None
    result = p2t.recognize_formula(image)
    pyperclip.copy(f'$$\n{result}\n$$')
    print(f'Success Recognition: {result}')

def copy_recognize():
    image = ImageGrab.grabclipboard()
    if not image:
        print('No image found in clipboard')
        return None
    result = p2t.recognize(image, resized_shape=608, return_text=True)
    pyperclip.copy(f'{result}')
    print(f'Success Recognition: {result}')

def copy_recognize_text():
    image = ImageGrab.grabclipboard()
    if not image:
        print('No image found in clipboard')
        return None
    result = p2t.recognize_text(image)
    pyperclip.copy(f'{result}')
    print(f'Success Recognition: {result}')

if __name__ == "__main__":
    p2t = Pix2Text.from_config()
    keyboard.add_hotkey('ctrl + alt + m', copy_recognize_formula)
    keyboard.add_hotkey('ctrl + alt + n', copy_recognize)
    keyboard.add_hotkey('ctrl + alt + k', copy_recognize_text)
    keyboard.wait()
    