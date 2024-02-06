from pdf2image import convert_from_path
#import os
path = '.\\Test\\BD - Largo Winch - T4 - Business Blues.pdf'
path2 = '.\\Test\\MCC L2 Licence Science et Technologie 22-23'

def convert_pdf_to_images(pdf_path):
    print("Starting conversion...")
    # Convert PDF to images
    images = convert_from_path(pdf_path)
    print("Conversion done. Starting saving images...")
    # Save images to files
    for i, image in enumerate(images):
        image.save(f'output_image_test{i}.png', 'PNG')

# Use the function
convert_pdf_to_images(path)