sudo docker pull mongo

sudo docker network rm jawadruids-net
sudo docker network create jawadruids-net

sudo docker run -d --name mdb --rm --net jawadruids-net -p 27017:27017  mongo

sudo docker build -t gdp-be modulo_1_get_frame


sudo docker build -t gdp-fe modulo_5_web_app


sudo docker run -d --net jawadruids-net --rm -p 1111:1111 --name gdp-be gdp-be

sudo docker run -d --net jawadruids-net --rm -p 8080:8080 --name gdp-fe gdp-fe
