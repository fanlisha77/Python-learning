from cnocr import CnOcr
def img_1():
    # img_name = "ocr_1.jpg"
    img_name = r"C:\Users\lonovo\Desktop\ocr_1.jpg"
    obj = CnOcr()
    res = obj.ocr(img_name)   #列表
    # print(res)
    # print(type(res))
    for i in res:
        # print(i)   #字典
        # print(type(i))
        print(i["text"])
        # print("------------------------------------------------")
img_1()