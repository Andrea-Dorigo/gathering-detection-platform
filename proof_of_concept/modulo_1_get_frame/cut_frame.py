#altezza/2
#lunghezza/3
import image_slicer
frame=image_slicer.slice('Frame/frame8.jpg', 6, save=False)
image_slicer.save_tiles(frame, directory='FrameCut/')
