from cnocr import CnOcr


def img_2():
    img_name = r"C:\Users\lonovo\Desktop\ocr_2.jpg"
    obj = CnOcr(det_model_name='naive_det')#需要添加对应的模块
    res = obj.ocr(img_name)
    for i in res:
        print(i["text"])
img_2()