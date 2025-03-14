import patoolib

path = r"C:\Users\arnau\OneDrive\Documents\2 Interesting Documents\PDF to CBZ\docs_to_convert\BD - Mages - T08 - Belkiane.cbr"

new_path = path.replace(".cbr", ".cbz")
patoolib.repack_archive(archive=path, archive_new=path.replace(".cbr", ".cbz"))