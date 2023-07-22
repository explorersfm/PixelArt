# PixelArt
Simple Python script for pixelating and upscaling an input image.

![IMAGE](https://imgur.com/rw9xooS)

## Requirements:
- [Python 3.X.X](https://www.python.org/downloads/)

## How To Use:
1) Rename the image you wish to pixelate "input.png", then copy it to the folder. If you want to use the default SFM logo you can skip this step.
2) Install requirements using: `pip install -r requirements.txt`
3) Run the script using `python make.py`  
- Select the name of the pixelated output file. This will be 'output' by default.
- Select the size of your pixelated image. This will be '32' by default. The number represents the amount of pixels in with and height, meaning '32' will output a 32x32 px image.
- The pixelated image will be saved to the same folder the script resides in.

## Upscaling (Optional):
4) If you wish to upscale the pixelated image, you can run `python upscale.py`
- Select the name of the pixelated image you wish to upscale. This will be 'output' by default.
- Select the name of the upscaled image. This will be 'upscaled_output' by default.
- Select the new image size. This will be 1080 by default.
