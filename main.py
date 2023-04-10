import cv2 as cv
import numpy as np


def image_setup(src):
    img_result = np.clip(src, 0, 255)
    img_result = img_result.astype('uint8')

    bw_img = cv.cvtColor(img_result, cv.COLOR_BGR2GRAY)
    _, bw_img = cv.threshold(bw_img, 40, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

    return bw_img

def find_centre(src):
    bin_img = image_setup(src)
    
    dist = cv.distanceTransform(bin_img, cv.DIST_L2, 3)
    cv.normalize(dist, dist, 0, 1.0, cv.NORM_MINMAX)
    _, dist = cv.threshold(dist, .9, 1.0, cv.THRESH_BINARY)
    # cv.imshow('normal dist', dist)
    cv.imwrite('dist.png', dist*255)

    test = cv.imread('dist.png')
   
    # Convert the image to grayscale
    test = cv.cvtColor(test, cv.COLOR_BGR2GRAY)
    
    # Apply threshold to obtain a binary image
    _, test = cv.threshold(test, 127, 255, cv.THRESH_BINARY)

    dist = cv.ximgproc.thinning(test, test, cv.ximgproc.THINNING_GUOHALL)
    # cv.imshow('thin dist',dist)
    

    dist = cv.cvtColor(dist, cv.COLOR_GRAY2BGR)
    dist = dist.astype('uint8')
    
    
    dist[np.where((dist == [255,255,255]).all(axis=2))] = [0,0,255]
    
    return dist

def main():
    src = cv.imread('track.png')
    result = src
    if src is None:
        print('ERROR: Image not found')
        exit(0)
    
    centre = find_centre(src)
    
    centre_mask = cv.inRange(centre, (0,0,255), (0,0,255))

    # Replace the corresponding pixels in image1 with those from image2
    result[centre_mask > 0] = centre[centre_mask > 0]

    cv.imshow('Source w/ centre overlay', result)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
