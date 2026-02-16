
## SPONSOR LOGO
import os
import os.path

<%!
logo = getattr(params, 'sponsorLogo', None)
%>

logo = <%-logo%>

# if a logo is defined...
if logo != None:

    logoFile = '/rsrc/logos/' + logo

    # and if the file actually exists...
    # this is in case, the SCMT tries to configure a logo that doesn't
    # exist on the box. Now the entire package won't come crashing down.
    if os.path.exists(logoFile + '.tif'):
        # show the logo
        r = TIFF_Image(logoFile)
        r.setTransitionable(0)
        # logos need to be right justified
        w, h = r.size()
        r.setPosition(658 - w, 405)

        # Shadow on the right and bottom edges
        shadW = 5 
        offset = 3
        a1 = 0 
        a2 = .6
        shad = Polygon()
        shad.addVertex(0, 0, 0, 0, 0, a1)
        shad.addVertex(w+shadW-offset, 0, 0, 0, 0, a1)
        shad.addVertex(w-offset, shadW, 0, 0, 0, a2)
        shad.addVertex(0, shadW, 0, 0, 0, a2)
        shad.setPosition(658-w+offset, 405-shadW)
        p.addItem(shad)
        shad2 = Polygon()
        shad2.addVertex(0, shadW, 0, 0, 0, a2)
        shad2.addVertex(0, h+shadW-offset, 0, 0, 0, a2)
        shad2.addVertex(shadW, h+shadW-offset, 0, 0, 0, a1)
        shad2.addVertex(shadW, 0, 0, 0, 0, a1)
        shad2.setPosition(658, 405-shadW)
        p.addItem(shad2)

        p.addItem(r)
