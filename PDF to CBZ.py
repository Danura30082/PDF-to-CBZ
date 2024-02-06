import fitz
import os
import shutil
import glob
import rarfile
import zipfile

dir_to_convert = r'C:\Users\arnau\OneDrive\Images\BD'
done_dir = r'C:\Users\arnau\OneDrive\Images\00Done'

dir_to_convert = '.\\Test'
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
    print("CBZ created successfully.")

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
        shutil.move(path, done_dir)
    print("PDF moved to Done directory.")

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
    
    output_dir = create_output_directory(pdf_path)
    
    print("Converting PDF to images in", output_dir)
    
    with fitz.open(pdf_path) as doc:
    # Iterate through the pages
        for i in range(len(doc)):
            page = doc.load_page(i)
            pix = page.get_pixmap()
            output = os.path.join(output_dir, "outfile{}.png".format(i))
            pix.save(output)
    
    return output_dir

def convert_pdf_to_cbz(path):
    dir = convert_pdf_to_images(path)
    clean_up(path)
    if dir is not None: # if the conversion was successful
        dir_to_cbz(dir)
    print("PDF converted successfully.")



def find_pdf_files(directory):
    # get all pdf files in the directory
    return glob.glob(os.path.join(directory, '**', '*.pdf'), recursive=True)

# Use the function

def find_cbr_files(directory):
    # get all rar files in the directory
    return glob.glob(os.path.join(directory, '**', '*.cbr'), recursive=True)

def zip_to_dir(path):
    output_dir = create_output_directory(path)
    # Extract the zip file
    with zipfile.ZipFile(path, 'r') as zip:
        zip.extractall(output_dir)

def rar_to_dir(path):
    output_dir = create_output_directory(path)
    with rarfile.RarFile(path, 'r') as rar:
        rar.extractall(output_dir)
    
    
    
def cbr_to_dir(path):
    
    
    # check if the file is a zip or a rar
    archive_type = get_archive_type(path)
    print(path, archive_type)
    if archive_type is not None:
        # Create a new directory for the images
        output_dir = create_output_directory(path)
    if archive_type == 'zip':
        renamed_path=os.path.join(os.path.dirname(path),os.path.basename(output_dir) + '.zip')
        os.rename(path, renamed_path)
        zip_to_dir(renamed_path)
    elif archive_type == 'rar':
        renamed_path=os.path.join(os.path.dirname(path),os.path.basename(output_dir) + '.rar')
        os.rename(path, renamed_path)
        rar_to_dir(renamed_path)
    else:
        print("File is not a zip or a rar")
        return None
    # Delete the original file
    os.remove(renamed_path)
    print("CBR extracted successfully.")
    return output_dir

def get_archive_type(file_path):
    with open(file_path, 'rb') as file:
        magic_number = file.read(4)
    if magic_number[:4] == b'PK\x03\x04' or magic_number[:4] == b'PK\x05\x06' or magic_number[:4] == b'PK\x07\x08':
        return 'zip'
    elif magic_number[:7] == b'Rar!\x1A\x07\x00' or magic_number == b'Rar!\x1A\x07\x01\x00':
        return 'rar'
    else:
        return None
    
def cbr_to_cbz(path):
    dir = cbr_to_dir(path)
    if dir is not None: # if the conversion was successful
        dir_to_cbz(dir)
        print("CBR converted successfully.")
    
if __name__ == "__main__":
    pdf_files = find_pdf_files(dir_to_convert)
    print("number of pdf files to convert: ", len(pdf_files))
    if len(pdf_files) == 0:
        print("No pdf files found")
    else:
        print ("procced? (y/n)")
        if input() != "y":
            pass
        else:
            print("proceeding...")
            for path in pdf_files:
                print( pdf_files.index(path)," of ", len(pdf_files))
                convert_pdf_to_cbz(path)
            print("done with pdf files")
    cbr_files = find_cbr_files(dir_to_convert)
    print("number of cbr files to convert: ", len(cbr_files))
    if len(cbr_files) == 0:
        print("No cbr files found")
        exit()
    else:
        print ("procced? (y/n)")
        if input() != "y":
            exit()
        else:
            print("proceeding...")
            for path in cbr_files:
                print( cbr_files.index(path)," of ", len(cbr_files))
                cbr_to_cbz(path)
            print("done with cbr files")
