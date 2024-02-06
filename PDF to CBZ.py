import fitz
import os
import shutil
import glob
import time
path = '.\\Test\\BD - Largo Winch - T4 - Business Blues.pdf'
path = '.\\Test\\MCC L2 Licence Science et Technologie 22-23.pdf'
path2 = '.\\Test'
done_dir = '.\\Done'
if not os.path.isdir(done_dir):
    os.mkdir(done_dir)

def dir_to_cbz(path):
    # Create the zip archive
    shutil.make_archive(path, 'zip', path)
    # Rename the .zip file to .cbz
    os.rename(path + '.zip', path + '.cbz')
    # Delete the original directory
    shutil.rmtree(path)

def create_output_directory(file_path):
    # Get the directory of the PDF file
    base_dir = os.path.dirname(file_path)
    # Get the base name of the PDF file (its name without the directory)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    # Create a new directory for the images
    output_dir = os.path.join(base_dir, base_name)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def clean_up(path):
    if not os.path.exists(done_dir + os.path.basename(path)): # if the file is not already in the Done directory
        print("Moving the PDF file to the Done directory...")
        print (done_dir + os.path.basename(path))
        shutil.move(path, done_dir)

def convert_pdf_to_images(pdf_path):
    # Error checking
    if not os.path.exists(pdf_path):
        print(pdf_path, "does not exist.")
        return None
    if not pdf_path.lower().endswith(".pdf"):
        print(pdf_path, "is not a PDF.")
        return None
    if os.path.exists(pdf_path.replace(".pdf", ".cbz")):
        print("CBZ file already exists.")
        return None
    
    output_dir= create_output_directory(pdf_path)
    
    print("Converting PDF to images in", output_dir)
    
    with fitz.open(pdf_path) as doc:
    # Iterate through the pages
        for i in range(len(doc)):
            page = doc.load_page(i)
            pix = page.get_pixmap()
            output = os.path.join(output_dir, "outfile{}.png".format(i))
            pix.save(output)
    
    # Close the document
    print("Closing the PDF file...")

    # Move the PDF file to the Done directory
    
    
        
    
    
    print("PDF converted successfully.")
    return output_dir

def convert_pdf_to_cbz(path):
    dir = convert_pdf_to_images(path)
    clean_up(path)
    if dir is not None: # if the conversion was successful
        dir_to_cbz(dir)



def find_pdf_files(directory):
    # get all pdf files in the directory
    return glob.glob(os.path.join(directory, '*.pdf'))

# Use the function



pdf_files = find_pdf_files(path2)
for path in pdf_files:
    convert_pdf_to_cbz(path)
print(pdf_files) 
