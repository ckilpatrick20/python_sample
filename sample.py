import gzip
import shutil

def zip_file(fname):
  with open(fname, 'rb') as f_in:
    with gzip.open(fname + ".gz", 'wb') as f_out:
      shutil.copyfileobj(f_in, f_out)

def unzip_file(fname):
  with gzip.open(fname, 'rb') as f_in:
    with open('[PATH_TO_FILE]', 'wb') as f_out:
      shutil.copyfileobj(f_in, f_out)

zip_file("[PATH_TO_FILE]")
unzip_file("[PATH_TO_FILE]")