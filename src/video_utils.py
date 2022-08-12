import cv2
import os
import re 

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

def extract_by_index(index = 0, range = 100, path = ""):
    """
    Extracts a given number of frames from the video at the given absolute filepath
    """
    vid_path = path
    frame = index
    cap = cv2.VideoCapture(path)

    total = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    if frame >= 0 & frame <= total:
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame)

    i=0
    while i<range:
        ret, frame = cap.read()
        filename = "/Users/user/Desktop/walk_frames/img"+str(i)+".png"
        cv2.imwrite(filename, frame)
        print(filename+" saved!")
        i+=1

    cv2.destroyAllWindows()

def video_from_images(folder_path = "/Users/user/Desktop/frames", image_type=".png"):
    """
    Combines images in the given folder into a video file
    """
    image_folder = folder_path
    video_name = os.path.join(folder_path, 'plotted.avi')

    images = natural_sort([img for img in os.listdir(image_folder) if img.endswith(image_type)])
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 30, (width,height))

    print("Combining...")

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        print("Added "+image)

    cv2.destroyAllWindows()
    video.release()

if __name__=="__main__":
    #extract_by_index(5280, 90, path="/Users/user/Documents/desktop_cleanup/walk/walk.mp4")
    video_from_images(folder_path = "/Users/user/Desktop/walk_frames", image_type=".png")
    