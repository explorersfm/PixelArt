from PIL import Image

def image_to_pixel_art(image_path, output_path, size):
    # Open the image
    image = Image.open(image_path)

    # Resize the image
    image = image.resize((size, size), Image.Resampling.NEAREST)

    # Convert to pixel art
    image = image.convert('P')

    # Save the result
    image.save(output_path)

# Set the default output name and size
default_output_name = 'output'
default_size = 36

# Ask the user for the output name and size
output_name = input(f"Please enter the output name (default: {default_output_name}): ")
size = input(f"Please enter the size (default: {default_size}): ")

# If the user didn't enter an output name or size, use the defaults
output_name = output_name if output_name else default_output_name
size = int(size) if size else default_size

# Ensure the output name ends with '.png'
if not output_name.lower().endswith('.png'):
    output_name += '.png'

# Use the function
image_to_pixel_art('input.png', output_name, size)
print(f"\nThe pixelated image is saved as {output_name}")
