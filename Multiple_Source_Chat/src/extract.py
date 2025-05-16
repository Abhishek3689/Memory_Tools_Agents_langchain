import os,time
import sys


# Add the root directory (Multiple_Source_Chat) to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.utils import extract_webpage_data,download_pdf

start=time.time()
url='https://en.wikipedia.org/wiki/BrahMos'

text, links, pdfs = extract_webpage_data(url)

## Save the text in a file
with open('Multiple_Source_Chat/data/text.txt','w',encoding="utf-8") as file:
    file.write(text)

# Download PDFs
for pdf_url in pdfs:
    download_pdf(pdf_url)

print(text[:200])
print('-'*130)
print(time.time()-start)