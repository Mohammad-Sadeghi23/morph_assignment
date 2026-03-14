import cv2
import numpy as np

# run a loop 8 times
for i in range(1, 9):

    # import the (i)th warped version of image 0 and image 1 for the current step
    w0 = cv2.imread(f"images/W0.t{i}.jpg")
    w1 = cv2.imread(f"images/W1.t{i}.jpg")

    # Get How long we are into the morphing.
    t = i / 9

    # Blend the two images.
    blend = (1 - t) * w0 + t * w1

    # convert to a image format 
    blend = blend.astype(np.uint8)

    # write the new blended image
    cv2.imwrite(f"output/blend_t{i}.jpg", blend)
