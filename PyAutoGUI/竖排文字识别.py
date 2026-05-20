from cnocr import CnOcr


def img_3():
    img_name = "ocr_3.jpg"
    obj = CnOcr(rec_model_name='ch_PP-OCRv3')
    res = obj.ocr(img_name)
    for i in res:
        print(i["text"])
img_3()