# Team T081's Text-Based Photo Editing Program
Version 1.0 April 14th, 2021

Description
--------------------
The project contains three files that will allow the user to apply various filters to images. Multiple filters may be applied on top of each other. The manipulated image can then be saved.

The project is made up of three files:
- [T081_image.filters.py](https://github.com/emilyxtang/text-based-photo-editing/blob/main/T081_image_filters.py) is a Python file containing all of the image filters
- [T081_interactive_ui.py](https://github.com/emilyxtang/text-based-photo-editing/blob/main/T081_interactive_ui.py) is an interactive user interface
- [T081_batch_ui.py](https://github.com/emilyxtang/text-based-photo-editing/blob/main/T081_interactive_ui.py) is a batch user interface

Installation
--------------------
Python 3.9.2 or later must be installed. It can be downloaded at https://www.python.org/downloads/. Pillow 8.1.2 or later must be installed. It can be downloaded in Command Prompt on Windows 10, or Terminal on MacOS. The Cimpl version 1.04 library and point_manipulation.py are required.

Usage
--------------------
```js
> python T081_interactive_ui.py
```
When prompted, enter a command to execute, then press the 'Enter' key. Both
lowercase and uppercase letters for these commands will be accepted. First, an
image must be loaded in to start applying filters. The user will be able to
apply as many filters as they see fit. After each filter is applied to the image,
the manipulated image will be shown. The manipulated image can then be saved
before quitting the program.

```js
> python T081_batch_ui.py
```
When prompted, the user will enter the name of the batch file. The program will read the batch file, and for each job it will read the image file, apply all the filters, and save the manipulated image to the designated file.

Credits
--------------------
- Written by Emily Tang: combine, _determine_color, _adjust_component, posterize, _interpolation, _exhaustive_search, _image_border_finding, draw_curve, check_valid_command, show_and_save_image
- Written by Alexander Bundgaard: blue_channel, sepia, detect_edges
- Written by Taytum George: green_channel, three_tone, flip_vertical
- Written by Matthew Gray: red_channel, extreme_contrast, flip_horizontal

--------------------

Copyright 2021 T081 Corporation. All rights reserved.

T081 Text-Based Photo Editing Program and its use are subject to a license
agreement and are also subject to copyright, trademark, patent and/or other
laws.