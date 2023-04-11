import cv2 as cv
import numpy as np
import csv

def image_setup(src):
    img_result = np.clip(src, 0, 255)
    img_result = img_result.astype('uint8')

    bw_img = cv.cvtColor(img_result, cv.COLOR_BGR2GRAY)
    _, bw_img = cv.threshold(bw_img, 40, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

    return bw_img

def find_centre(src):
    bin_img = image_setup(src)

    dist_map = cv.distanceTransform(bin_img, cv.DIST_L2, 3)
    
    mask = dist_map.copy()

    cv.normalize(mask, mask, 0, 1.0, cv.NORM_MINMAX)
    _, mask = cv.threshold(mask, 0, 1, cv.THRESH_BINARY)
    mask = mask.astype('uint8')
    mask *= 255
    
    mask = cv.ximgproc.thinning(mask, mask, cv.ximgproc.THINNING_GUOHALL)
        
    widths = cv.bitwise_and(dist_map, dist_map, mask=mask)
        
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    mask[np.where((mask == [255,255,255]).all(axis=2))] = [0,0,255]
    
    return mask, widths

def extract_points(array: np.array):
    result = []
    x_coords, y_coords = np.nonzero(array)

    for i in range(len(x_coords)):
        x, y = x_coords[i], y_coords[i]
        result.append((x,y,array[x,y]))

    with open('output/centre_line.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(result)

    return result

def main():
    src = cv.imread('input/track.png')
    result = src
    if src is None:
        print('ERROR: Image not found')
        exit(0)
    
    centre, widths = find_centre(src)
    
    extract_points(widths)

    centre_mask = cv.inRange(centre, (0,0,255), (0,0,255))

    # Replace the corresponding pixels in image1 with those from image2
    result[centre_mask > 0] = centre[centre_mask > 0]

    cv.imshow('Source w/ centre overlay', result)
    cv.imwrite('output/track_centre.png', result)
    cv.imwrite('output/track_widths.png', widths)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
