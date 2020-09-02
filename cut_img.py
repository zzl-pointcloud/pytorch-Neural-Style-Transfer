import cv2

cut_img = "./shangkeroad/shanghai_night.jpg"
store_img = cut_img[:-4] + "_cut.jpg"

cut_img = cv2.imread(cut_img)
bbox = cv2.selectROI(cut_img, False)
cut = cut_img[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]

cv2.imwrite(store_img, cut)
