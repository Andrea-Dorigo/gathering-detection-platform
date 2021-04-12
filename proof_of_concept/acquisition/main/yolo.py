# USAGE
# python yolo.py --image images/baggage_claim.jpg --yolo yolo-coco
"""
This file is used in get_video.py
It uses yolov3 and opencv2 for object detection
"""

# import the necessary packages
import os
import argparse
import time
import cv2
import numpy as np

def detect():
    """
    Uses yolov3 and opencv2 for object detection and prints the result
    """
    print("inside YOLO")
    # construct the argument parse and parse the arguments
    argpars = argparse.ArgumentParser()
    argpars.add_argument("-i", "--image", required=True,
                         help="path to input image")
    argpars.add_argument("-y", "--yolo", default="yolo-coco",
                         help="base path to YOLO directory")
    argpars.add_argument("-c", "--confidence", type=float, default=0.5,
                         help="min probability to filter weak detections")
    argpars.add_argument("-t", "--threshold", type=float, default=0.3,
                         help="threshold when applyong non-maxima suppression")
    args = vars(argpars.parse_args())

    # load the COCO class labels our YOLO model was trained on
    # labels_path = os.path.sep.join([args["yolo"], "coco.names"])
    labels = open(os.path.sep.join([args["yolo"], "coco.names"])).read().strip().split("\n")

    # initialize a list of colors to represent each possible class label
    #np.random.seed(42)
    #COLORS = np.random.randint(0, 255, size=(len(labels), 3),
    #                           dtype="uint8")

    # derive the paths to the YOLO weights and model configuration
    #weightsPath = os.path.sep.join([args["yolo"], "yolov3.weights"])
    #configPath = os.path.sep.join([args["yolo"], "yolov3.cfg"])

    # load our YOLO object detector trained on COCO dataset (80 classes)
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet(os.path.sep.join([args["yolo"], "yolov3.cfg"]),
                                     os.path.sep.join([args["yolo"], "yolov3.weights"]))
    # load our input image and grab its spatial dimensions
    image = cv2.imread(args["image"])
    (height, width) = image.shape[:2]

    # determine only the *output* layer names that we need from YOLO
    layer_names = net.getLayerNames()
    layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # construct a blob from the input image and then perform a forward
    # pass of the YOLO object detector, giving us our bounding boxes and
    # associated probabilities
    # blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
    #                              swapRB=True, crop=False)
    net.setInput(cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                       swapRB=True, crop=False))
    start = time.time()
    net.forward(layer_names)
    end = time.time()

    # show timing information on YOLO
    print("[INFO] YOLO took {:.6f} seconds".format(end - start))

    # initialize our lists of detected bounding boxes, confidences, and
    # class IDs, respectively
    boxes = []
    confidences = []
    class_ids = []

    # loop over each of the layer outputs
    for output in net.forward(layer_names):
        # loop over each of the detections
        for detection in output:
            # extract the class ID and confidence (i.e., probability) of
            # the current object detection
            scores = detection[5:]
            #classID = np.argmax(scores)
            confidence = scores[np.argmax(scores)]

            # filter out weak predictions by ensuring the detected
            # probability is greater than the minimum probability
            if confidence > args["confidence"]:
                # scale the bounding box coordinates back relative to the
                # size of the image, keeping in mind that YOLO actually
                # returns the center (x, y)-coordinates of the bounding
                # box followed by the boxes' box_width and box_height
                box = detection[0:4] * np.array([width, height, width, height])
                (width, height, box_width, box_height) = box.astype("int")

                # use the center (x, y)-coordinates to derive the top and
                # and left corner of the bounding box
                #x =
                #y =

                # update our list of bounding box coordinates, confidences,
                # and class IDs
                boxes.append([int(width - (box_width / 2)), int(height - (box_height / 2)),
                              int(box_width), int(box_height)])
                confidences.append(float(confidence))
                class_ids.append(np.argmax(scores))

    # apply non-maxima suppression to suppress weak, overlapping bounding
    # boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"],
                            args["threshold"])

    # ensure at least one detection exists
    if len(idxs) > 0:
        # loop over the indexes we are keeping
        for i in idxs.flatten():
            # extract the bounding box coordinates
            #(x, y) = (boxes[i][0], boxes[i][1])
            #(w, h) = (boxes[i][2], boxes[i][3])

            # draw a bounding box rectangle and label on the image
            #color = [int(c) for c in COLORS[class_ids[i]]]
            #cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(labels[class_ids[i]], confidences[i])
            #cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
            #    0.5, color, 2)
            print(text)
    # show the output image
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)
detect()
