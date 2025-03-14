import os
import patoolib
import glob
from utils import clean_up


def cbr_to_cbz(path, done_dir, keep_original=True):
    if os.path.exists(path.replace(".cbr", ".cbz")):
        print("CBZ file already exists.")
        return None
    patoolib.repack_archive(archive=path, archive_new=path.replace(".cbr", ".cbz"),verbosity=-1)
    clean_up(path, done_dir, keep_original)

def find_cbr_files(directory):
    return glob.glob(os.path.join(directory, '**', '*.cbr'), recursive=True)

def cbz_to_cbr(path, done_dir, keep_original=True):
    if os.path.exists(path.replace(".cbz", ".cbr")):
        print("CBR file already exists.")
        return None
    patoolib.repack_archive(archive=path, archive_new=path.replace(".cbz", ".cbr"),verbosity=-1)
    clean_up(path, done_dir, keep_original)
    
def find_cbz_files(directory):
    return glob.glob(os.path.join(directory, '**', '*.cbz'), recursive=True)