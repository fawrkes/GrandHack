from SimpleCV import Camera, Display

def contained(box1, box2):
  if box1[0] < box2[0] and box1[1] < box2[1]:
    if box1[0] + box1[2] > box2[0] + box2[2] and box1[1] + box1[3] > box2[1] + box2[3]:
      return True
  return False

def main():
    cam = Camera()
    dis = Display()
    while dis.isNotDone():
      img = cam.getImage()
      #img = img.scale(0.5)
      #img = img.smooth(aperture=(11,11))
      img = img.equalize()
      faces = img.findHaarFeatures("face.xml")
      eyes = img.findHaarFeatures("eye.xml")
      if faces:
        for face in faces:
          face.draw()
          #print face.area()
          facebox =  face.boundingBox()
        if eyes:
          for eye in eyes:
            if contained(facebox,eye.boundingBox()):
              eye.draw()
      img.show()
    

if __name__ == "__main__":
  main()
