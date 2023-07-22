from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    with Image.open(input_image_path) as image:
        image = image.resize((size, size), Image.Resampling.NEAREST)
        image.save(output_image_path)

# Set the default input name, output name and size
default_input_name = 'output'
default_output_name = 'upscaled_output'
default_size = 1080

# Ask the user for the input name, output name and size
input_name = input(f"Please enter the input image name (default: {default_input_name}): ")
output_name = input(f"Please enter the output name (default: {default_output_name}): ")
size = input(f"Please enter the size (default: {default_size}): ")

# If the user didn't enter an input name, output name or size, use the defaults
input_name = input_name if input_name else default_input_name
output_name = output_name if output_name else default_output_name
size = int(size) if size else default_size

# Ensure the input and output names end with '.png'
if not input_name.lower().endswith('.png'):
    input_name += '.png'
if not output_name.lower().endswith('.png'):
    output_name += '.png'

# Call the resize_image function
resize_image(input_name, output_name, size)
print(f"\nThe upscaled image is saved as {output_name}")
