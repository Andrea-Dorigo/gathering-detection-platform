sudo docker pull mongo

sudo docker network create jawadruids-net

sudo docker run -d --name mdb --net jawadruids-net -p 27017:27017 -e "discovery.type=single-node" mongo

sudo docker build -t gdp-be modulo_1_get_frame

sudo docker run -d --net jawadruids-net -p 1111:1111 --name gdp-be gdp-be

sudo docker build -t gdp-fe modulo_5_web_app

sudo docker run -d --net jawadruids-net -p 8080:8080 --name gdp-fe gdp-fe
