import fitz
import os
import patoolib
import glob
from utils import create_output_directory, clean_up

def convert_pdf_to_images(pdf_path):
    if not os.path.exists(pdf_path):
        print(pdf_path, "does not exist.")
        return None
    if not pdf_path.lower().endswith(".pdf"):
        print(pdf_path, "is not a PDF.")
        return None
    if os.path.exists(pdf_path.replace(".pdf", ".cbz")):
        print("CBZ file already exists.")
        return None
    
    output_dir = create_output_directory(pdf_path)
    print("Converting PDF to images in", output_dir)
    
    with fitz.open(pdf_path) as doc:
        for i in range(len(doc)):
            page = doc.load_page(i)
            pix = page.get_pixmap()
            output = os.path.join(output_dir, "outfile{}.png".format(i))
            pix.save(output)
    
    return output_dir


def convert_pdf_to_cbz(path, done_dir):
    dir = convert_pdf_to_images(path)
    if dir is not None:
        images=sorted(glob.glob(os.path.join(dir, "*.png")))
        patoolib.create_archive(dir + ".cbz", images,verbosity=-1) 
        clean_up(dir, done_dir, keep_original=False)
        clean_up(path, done_dir, keep_original=True)
    print("PDF converted successfully.")

def find_pdf_files(directory):
    return glob.glob(os.path.join(directory, '**', '*.pdf'), recursive=True)