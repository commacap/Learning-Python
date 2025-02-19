#we use nested for loops to loop over lists
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for image in picture: #image is the row
    for pixel in image: #pixel is a list in the picture
        if (pixel == 1):
            print("*",end='')
        else:
            print(" ", end='')
    print("")