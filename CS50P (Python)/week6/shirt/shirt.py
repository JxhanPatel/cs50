#wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png
#wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip


import sys
import os
from PIL import Image, ImageOps


def edit(input_img, output_img):
    try:
        shirt_image = Image.open("shirt.png")
        with Image.open(input_img) as input_image:
            input_cropped = ImageOps.fit(input_image, shirt_image.size)
            input_cropped.paste(shirt_image, mask=shirt_image)
            input_cropped.save(output_img)
    except FileNotFoundError:
        sys.exit(f"Input image does not exist")


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        allowed_formats = [".jpg", ".jpeg", ".png"]
        input_ext = os.path.splitext(sys.argv[1])[1].lower()
        output_ext = os.path.splitext(sys.argv[2])[1].lower()

        if output_ext not in allowed_formats:
            sys.exit("Invalid output format")
        elif input_ext != output_ext:
            sys.exit("Input and Output have different Extensions")
        else:
            edit(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
