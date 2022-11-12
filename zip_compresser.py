import zipfile
import pathlib



def make_archive(filepaths,dest_dir):
    dest  = pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(dest,'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)

