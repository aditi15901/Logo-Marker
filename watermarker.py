import cvzone, cv2
from zipfile import ZipFile
import numpy as np
import sys
import tempfile, os

class Logo:
    def __init__(self,logoname):
        self.overlay = cv2.imread(logoname,cv2.IMREAD_UNCHANGED)
        self.zipObj=Zipper()

    def image(self,filename): 
        background = cv2.imread(filename)
        x,y,h=background.shape
        x1,y1,h1=self.overlay.shape
        x1=min(x,x1)/max(x1,x)
        y1=min(y,y1)/max(y1,y)
        scale_down=min(x1,y1)/6

        rescale_png= cv2.resize(self.overlay, None, fx=scale_down, fy=scale_down, interpolation= cv2.INTER_AREA)  
        pixel =10
        if x<1000 | y<1000:
            pixel=0
        output=cvzone.overlayPNG(background,rescale_png,[pixel,pixel])
        self.zipObj.zip_write(output,filename)   
    
    def close(self):
        self.zipObj.zip_close()

class Zipper:

    def __init__(self):
        self.zipObj = ZipFile('sample.zip', 'w')

    def zip_write(self,output,filename):
        cv2.imwrite("logo_"+filename, output)
        self.zipObj.write("logo_"+filename)
        try: 
            os.remove("logo_"+filename)
        except: pass

    def zip_close(self):
        self.zipObj.close()

def main(): 
    ob_logo= Logo(sys.argv[1])
    n = len(sys.argv)

    for i in range(2, n):
        ob_logo.image(sys.argv[i])

    ob_logo.close()

if __name__=="__main__":
    main()


