import os
import shutil

def create_output_directory(file_path):
    base_dir = os.path.dirname(file_path)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join(base_dir, base_name)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def clean_up(path, done_dir, keep_original=True):
    if not keep_original:
        shutil.rmtree(path)
        # if os.path.isfile(path):
        #     os.remove(path)
        #     print("Original file deleted.")
        # elif os.path.isdir(path):
        #     shutil.rmtree(path)
        #     print("Image directory deleted.")
        # else:
        #     print("Invalid path to clean up")
                
        
    else:
        if not os.path.exists(os.path.join(done_dir, os.path.basename(path))):
            shutil.move(path, done_dir)
        print("Original file moved to Done directory.")


