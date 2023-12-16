#Tutorial: https://stackoverflow.com/questions/3444645/merge-pdf-files
#Installation: pip install pypdf

from pypdf import PdfMerger
import os

path1 = "./folder1/"
path2 = "./folder2/"
folder1 = os.listdir(path1)
folder2 = os.listdir(path2)

#Check the number of files
if len(folder1) != len(folder2):
    print("The folders must have the same number of files.")
    exit(-1)

#Padronizar os nomes dos arquivos
for idx in range(len(folder1)):
    filename1 = folder1[idx]
    filename2 = folder2[idx]
    print(filename1, filename2)
    
    merger = PdfMerger()
    merger.append(path1+filename1)
    merger.append(path2+filename2)

    output_name = "CompiledFiles"
    os.mkdir(output_name)
    
    merger.write("./"+output_name+"/"+output_name+".pdf")
    merger.close()