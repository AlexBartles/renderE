# This section handles displaying the map and the animated data images:

import os
#
# handle the IMAGE display
#

# Init globals
imageFile = ''
issueTime = 0 

# if we have data AND we have a map to show, show the image animation
if (imageCount > 0) and (mapAvailable > 0):
    filename = ''
    filetime = 0
    # setup a repeating image sequencer
    imageLoop = []

    count = 0
    last = imageCount - 1
    for fileData in availableData:

        # get filename without extension
        file = os.path.splitext(fileData[1])
        filename = file[0]
        filetime = fileData[0]

        gr = TIFF_Image(filename)
        gr.setSize(720,480)
        gr.setPosition(0,0)

        if count == last:
            imageLoop.append((gr, lastImageDuration))
        else:
            imageLoop.append((gr, imageDuration))

        count = count + 1



    # If there is movement
    if (imageCount > 1):
        # Find out how many complete loops we have time for.
        loopLimit = int( <%-prod.getDuration()%> / (lastImageDuration + ((imageCount - 1)*imageDuration)))

        # make it animate!
        renderUtil.animationLoop(p, imageLoop, 1, loopLimit)
    else:
        imageFile = filename
        issueTime = filetime
        p.addItem(gr)
