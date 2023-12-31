# PixelArt
Simple Python script for pixelating and upscaling an input image.

![IMAGE](https://i.imgur.com/rw9xooS.jpeg)

## Requirements:
- [Python3](https://www.python.org/downloads/)

## How To Use:
1) Rename the image you wish to pixelate "input.png", then copy it to the folder. If you want to use the default SFM logo you can skip this step.
2) Install requirements through the `pip install -r requirements.txt` command.
3) Run the script using the `python make.py` command. 
- Select the name of the pixelated output file. This will be **output** by default.
- Select the size of your pixelated image. This will be **32** by default. The number represents the amount of pixels in width and height, meaning '32' will output a 32x32 pixel image.
- The pixelated image will be saved to the same folder the input.png file resides in.

## Upscaling (Optional):
4) If you wish to upscale the pixelated image, you can run the `python upscale.py` command.
- Select the name of the pixelated image you wish to upscale. This will be **output** by default.
- Select the name of the upscaled image. This will be **upscaled_output** by default.
- Select the new image size. This will be **1080** by default.
