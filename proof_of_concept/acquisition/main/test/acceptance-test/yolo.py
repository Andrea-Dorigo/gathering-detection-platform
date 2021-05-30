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

def count_objects_in_frame(frame_part):
    """
    Uses yolov3 and opencv2 for object detection and prints the result
    """


    confidence = 0.5
    base_threshold = 0.3
    yolo_path = "../../yolo-coco"

    # load the COCO class labels our YOLO model was trained on
    labels = open(os.path.sep.join([yolo_path, "coco.names"])).read().strip().split("\n")

    net = cv2.dnn.readNetFromDarknet(os.path.sep.join([yolo_path, "yolov3.cfg"]),
                                     os.path.sep.join([yolo_path, "yolov3.weights"]))

    # load our input image and grab its spatial dimensions
    counter_frame = 0;
    count_person = 0;
    for frame in frame_part:
        image = frame_part[counter_frame]
        (height, width) = image.shape[:2]

        # determine only the *output* layer names that we need from YOLO
        layer_names = net.getLayerNames()
        layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        # construct a blob from the input image and then perform a forward
        # pass of the YOLO object detector, giving us our bounding boxes and
        # associated probabilities
        net.setInput(cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                           swapRB=True, crop=False))
        start = time.time()
        layerOutputs = net.forward(layer_names)
        end = time.time()

        # show timing information on YOLO
        print("[INFO] YOLO took {:.6f} seconds".format(end - start))

        # initialize our lists of detected bounding boxes, confidences, and
        # class IDs, respectively
        boxes = []
        confidences = []
        class_ids = []

        # loop over each of the layer outputs
        for output in layerOutputs:
            # loop over each of the detections
            for detection in output:
                # extract the class ID and confidence (i.e., probability) of
                # the current object detection
                scores = detection[5:]
                #classID = np.argmax(scores)
                confidence_score = scores[np.argmax(scores)]

                # filter out weak predictions by ensuring the detected
                # probability is greater than the minimum probability
                if confidence_score > confidence:
                    # scale the bounding box coordinates back relative to the
                    # size of the image, keeping in mind that YOLO actually
                    # returns the center-coordinates of the bounding
                    # box followed by the boxes' box_width and box_height
                    box = detection[0:4] * np.array([width, height, width, height])
                    (centerX, centerY, box_width, box_height) = box.astype("int")

                    # use the center-coordinates to derive the top and
                    # and left corner of the bounding box
                    x = int(centerX - (box_width / 2))
                    y = int(centerY - (box_height / 2))

                    # update our list of bounding box coordinates, confidences,
                    # and class IDs
                    boxes.append([x, y, int(box_width), int(box_height)])

                    confidences.append(float(confidence_score))
                    class_ids.append(np.argmax(scores))

        # apply non-maxima suppression to suppress weak, overlapping bounding
        # boxes
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidence_score,
                                base_threshold)

        # ensure at least one detection exists
        if len(idxs) > 0:
            # loop over the indexes we are keeping
            for i in idxs.flatten():
                # extract the bounding box coordinates
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])

                text = "{}: {:.4f}".format("", confidences[i])
                print(labels[class_ids[i]])
                if labels[class_ids[i]] == "person":

                    # draw a bounding box rectangle and label on the image
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 2)
                    cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (0,255,0), 2)
                    count_person = count_person + 1

                print(text)

        # show the output image
        cv2.imwrite('detection'+str(counter_frame)+'.jpg', image)
        counter_frame = counter_frame + 1

    return count_person
