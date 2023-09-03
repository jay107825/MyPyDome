import io
import os.path
import sys

import PyPDF2
import pdfplumber


def pdf_to_txt(pdf_path, txt_path):
    # 打开PDF文件
    with open(pdf_path, 'rb') as file:
        # reader = PyPDF2.PdfFileReader(file)
        reader = PyPDF2.PdfReader(file)
        # 读取PDF内容
        content = []
        for page_num in range(len(reader.pages)):
            page = reader.getPage(page_num)
            text = page.extractText()
            print(text)
            content.append(text)

        # 合并PDF内容
        merged_content = ''.join(content)

    # 保存到文本文件
    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(merged_content)

def psftotxt(path,pull):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding="gb18030")
    with pdfplumber.open(path) as  p:
        for i in range(482):
            page = p.pages[i]
            textber = page.extract_text()
            data = open(pull,"a",encoding="utf-8")
            data.write(textber)

if __name__ == '__main__':
    pdf_path = os.path.join("/Users","admin","Downloads","python.pdf")  # 要转换的PDF文件路径
    print(pdf_path)
    txt_path =os.path.join("/Users","admin","Downloads","jay.txt") # 转换后的TXT文件路径
    print(txt_path)
    # pdf_to_txt(pdf_path, txt_path)
    psftotxt(pdf_path,txt_path)