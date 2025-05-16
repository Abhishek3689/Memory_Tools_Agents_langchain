import requests
from bs4 import BeautifulSoup
import os

def extract_webpage_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text content
    text_content = soup.get_text()
    # Clean up extra spaces and line breaks
    lines = (line.strip() for line in text_content.splitlines())
    text_clean = '\n'.join(line for line in lines if line)

    # Extract hyperlinks
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # Extract PDF links
    pdf_links = [link for link in links if link.endswith('.pdf')]

    return text_clean, links, pdf_links

def download_pdf(pdf_url, save_dir='Multiple_Source_Chat\data\pdfs'):
    os.makedirs(save_dir, exist_ok=True)
    response = requests.get(pdf_url)
    file_name = os.path.join(save_dir, pdf_url.split('/')[-1])
    with open(file_name, 'wb') as f:
        f.write(response.content)
    return file_name

def load_pdf_file(Directory):
    pdf_file_list=[]
    pdf_directory=os.path.join(Directory,'pdfs')
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            filepath=os.path.join(pdf_directory,filename)
            pdf_file_list.append(filepath)
    return pdf_file_list

def load_text_file(Directory):
    txt_file_list=[]
    for filename in os.listdir(Directory):
        if filename.endswith('.txt'):
            filepath=os.path.join(Directory,filename)
            txt_file_list.append(filepath)
    return txt_file_list