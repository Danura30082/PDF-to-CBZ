import os
from multiprocessing import Pool
from pdf_converter import convert_pdf_to_cbz, find_pdf_files
from cbr_converter import cbr_to_cbz, find_cbr_files
import logging
import patoolib.util

dir_to_convert = r'.\docs_to_convert'
done_dir = r'.\done'

if not os.path.isdir(done_dir):
    os.mkdir(done_dir)

failed_pdf_paths = []
failed_cbr_paths = []

def pdf_worker(args):
    path, pdf_files = args
    try:
        print(pdf_files.index(path), " of ", len(pdf_files))
        convert_pdf_to_cbz(path, done_dir)
    except Exception as e:
        print(f"Failed to convert {path}: {e}")
        failed_pdf_paths.append(path)

def cbr_worker(args):
    path, cbr_files = args
    # try:
    print(cbr_files.index(path), " of ", len(cbr_files))
    cbr_to_cbz(path, done_dir)
    # except Exception as e:
    #     print(f"Failed to convert {path}: {e}")
    #     failed_cbr_paths.append(path)

if __name__ == "__main__":
    logging_level=1
    logging.basicConfig(level=logging.WARNING)
    input_text = input("convert CBR or PDF files? (c/p)")
    if input_text == "p":
        pdf_files = find_pdf_files(dir_to_convert)
        print("number of pdf files to convert: ", len(pdf_files))
        if len(pdf_files) == 0:
            print("No pdf files found")
        else:
            if input("proceed? (y/n)") != "y":
                pass
            else:
                print("proceeding...")
                for path in pdf_files:
                    print(pdf_files.index(path), " of ", len(pdf_files))
                    convert_pdf_to_cbz(path, done_dir)
                #     p.map(pdf_worker, [(path, pdf_files) for path in pdf_files])
                print("done with pdf files")
            if failed_pdf_paths:
                print("Failed to convert the following PDF files:")
                print('\n'.join(failed_pdf_paths))
    elif input_text == "c":
        cbr_files = find_cbr_files(dir_to_convert)
        print("number of cbr files to convert: ", len(cbr_files))
        if len(cbr_files) == 0:
            print("No cbr files found")
            exit()
        else:
            print("proceed? (y/n)")
            if input() != "y":
                exit()
            else:
                print("proceeding...")
                for path in cbr_files:
                    print(cbr_files.index(path), " of ", len(cbr_files))
                    cbr_to_cbz(path, done_dir)
                # with Pool() as p:
                #     p.map(cbr_worker, [(path, cbr_files) for path in cbr_files])
                print("done with cbr files")
                if failed_cbr_paths:
                    print("Failed to convert the following CBR files:")
                    print('\n'.join(failed_cbr_paths))