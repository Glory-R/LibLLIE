from pdf2docx import Converter


def convert_pdf_to_word(pdf_path, word_path):
    # 创建一个转换器对象
    cv = Converter(pdf_path)

    # 转换PDF到Word
    cv.convert(word_path)

    # 释放资源
    cv.close()


if __name__ == '__main__':
    pdf_path = r"D:\race\lll.pdf"
    word_path = r"D:\race\lll.docx"
    convert_pdf_to_word(pdf_path, word_path)
    print("转换完成！")
