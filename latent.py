import cv2



def latent():
  src = cv2.imread( "/content/ImageInpaintingDeepfill/ip/input_img.png")
  print(src.shape)
  cv2_imshow(src) 
  grayScale = cv2.cvtColor( src, cv2.COLOR_RGB2GRAY )
  cv2_imshow(grayScale)
  cv2.imwrite('grayScale_sample1.jpg', grayScale, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
  kernel = cv2.getStructuringElement(1,(17,17))
  blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
  cv2_imshow(blackhat)
  cv2.imwrite('blackhat_sample1.jpg', blackhat, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
  ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
  print( thresh2.shape )
  cv2_imshow(thresh2)
  cv2.imwrite('thresholded_sample1.jpg', thresh2, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
  dst = cv2.inpaint(src,thresh2,1,cv2.INPAINT_TELEA)
  cv2_imshow(dst)
  cv2.imwrite('/content/ImageInpaintingDeepfill/output/inpt.jpg', dst, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
