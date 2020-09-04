# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x0 = 6
    y0 = 17
    x1 = 847
    y1 = 838
    deltaX= 41.5
    deltaY= 41.5

    img = cv2.imread('TrainingSet.jpg')
    for x in range(0, 20):
        for y in range(0, 20):
            xA= x0+int(deltaX*x)-4
            yA= y0+int(deltaY*y)-4
            XYsize = 48
            cropped_img = img[xA:xA+XYsize, yA:yA+XYsize]
            sname = 'part/' + repr(x) +'_'+repr(y) +'.jpg'
            cv2.imwrite(sname, cropped_img)

#    plt.imshow(cropped_img)
#   plt.show()
    print_hi('PyCharm')


## Teaching Alogrithm
## Scale and Rotaion small angle



## ds
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
