import PySimpleGUI as hp
from zip_compresser import make_archive


label1 = hp.Text("Select files to compress: ")
box1 = hp.InputText()
choose1 = hp.FilesBrowse("Choose",key="files")

label2 = hp.Text("Select destination folder: ")
box2 = hp.InputText()
choose2 = hp.FolderBrowse("Choose",key="folder")

compress = hp.Button("Compress")
output_label = hp.Text(key='output',text_color="green")

window = hp.Window("Area King App",layout=[[label1,box1,choose1],[label2,box2,choose2],[compress,output_label]])
while True:
    event , value  = window.read()
    print(event)
    print(value)
    filepaths = value["files"].split(";")
    folder = value["folder"]
    make_archive(filepaths,folder)
    window['output'].update(value="Compression successfully!!!")


window.close()