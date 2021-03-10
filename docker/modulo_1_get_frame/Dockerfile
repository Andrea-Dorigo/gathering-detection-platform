FROM ubuntu:20.04

WORKDIR /home/jawadruids

COPY . .

EXPOSE 8080

RUN apt update

RUN ln -fs /usr/share/zoneinfo/Europe/Rome /etc/localtime


RUN apt-get -y install unzip python3 python3-pip python3-opencv


RUN pip3 install --no-cache-dir numpy mongoengine image_slicer


# RUN chmod +x start.sh

# CMD ["sh", "start.sh"]
CMD cd yolo-object-detection/ && python3 get_video.py
# CMD cd modulo_1_get_frame/yolo-object-detection/ && python3 get_video.py & java -jar ../../modulo_5_web_app/demo/mongodbapp/target/mongodbapp-0.0.1-SNAPSHOT.jar
