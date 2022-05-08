import cv2

def boundingRectForContours(contours):
    first = True
    x1 = y1 = x2 = y2 = 0
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        if first:
            x1 = x
            y1 = y
            x2 = x+w
            y2 = y+h
            first = False
        if (x < x1):
            x1 = x
        if (y < y1):
            y1 = y
        if (x2 < x + w ):
            x2 = x + w
        if (y2 < y + h):
            y2 = y + h

    # expand
    ext = 40
    x1 = x1 - ext
    y1 = y1 - ext
    x2 = x2 + ext
    y2 = y2 + ext
    
    return x1, y1, x2, y2
