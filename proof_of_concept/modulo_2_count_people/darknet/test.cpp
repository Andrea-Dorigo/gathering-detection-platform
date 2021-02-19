#include <stdlib.h>
#include <stdio.h>

int main (){
  system("./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg");
  return 0;
}
