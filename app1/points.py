#Slow but accurate
# from . import views
import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image

# print(views.name)


def find_points(name):
    print(name)
    rcParams['figure.figsize'] = 8, 16
    reader = easyocr.Reader(['en'])
    outputs = reader.readtext('media/'+name)
    # outputs = reader.readtext(name)

    text = ""
    for output in outputs:
        text += output[1] + " "
    print(text)
    points = {'class respresentative':5,'photography':10,'blood':10,'nss':10,'ncc':5,'cricket':10,'football':10,'basketball':10,'dance':4,'drama':5,'music':5,'elocution':5,
            'yoga':5,'internship':20,'publication':10,'reporting':5,'fest':5,'hackathon':10,'harithaharam':1,'plantation':1,'debate':10,'quiz':10,'group discussion':10,'conclalve':10,'nptel':20}
    # text = 'Certificate of Participation for participating in ECON, Entrepreneurship and Business Conclalve, which was held on 31st Mrach and 1st April,2022 in CBIT Premises'
    text = text.lower()
    score=0
    bad_chars = [';', ':', '!', "*", ","]
    for i in bad_chars:
        text = text.replace(i, '')
    text = text.split()
    for i in text:
        if i in points.keys():
            score+=points[i]
            break
    print(score)
    return score

# final_score = find_points()
