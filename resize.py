import os
from PIL import Image

def resize_images(directory, max_size=(1920, 1920), quality=80):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    # Only resize if the image is larger than max_size
                    if img.width > max_size[0] or img.height > max_size[1]:
                        img.thumbnail(max_size, Image.Resampling.LANCZOS)
                        img.save(filepath, optimize=True, quality=quality)
                        print(f"Resized and compressed {filename}")
                    else:
                        img.save(filepath, optimize=True, quality=quality)
                        print(f"Compressed {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == '__main__':
    images_dir = r"c:\Users\samue\Documents\GitHub\ChippewaRifleClub.github.io\images"
    resize_images(images_dir)
