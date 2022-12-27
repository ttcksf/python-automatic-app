import glob, os
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from PyPDF2 import PdfMerger

read_file_path = r"C:/Users/ttc01/Downloads/test.pdf"
# for file_name in glob.glob(read_file_path):
#   reader = PdfReader(file_name)
#   page_number = len(reader.pages)
#   (name, e) = os.path.splitext(file_name)


# for i in range(page_number):
#   writer = PdfWriter()
#   file_obj = reader.pages[i]
#   new_file_name = name + "-" + str(i + 1) + ".pdf"
#   write_file_path = "{}".format(new_file_name)
#   with open(write_file_path, "wb") as f:
#     writer.add_page(file_obj)
#     writer.write(f)

merger = PdfMerger()
files = glob.glob("C:/python-automartic-app/pdf/files/*.pdf")
print(files)
# for i in files:
#   merger.append(files)

