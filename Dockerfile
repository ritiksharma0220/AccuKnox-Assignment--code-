FROM alpine:latest

RUN apk --no-cache add fortune cowsay

ENV SRVPORT=4499
ENV RSPFILE=response

COPY wisecow.sh /wisecow.sh

RUN chmod +x /wisecow.sh

EXPOSE $SRVPORT

CMD ["/wisecow.sh"]

#docker build -t wisecow-image run to build image 

#docker run -p 4499:4499 wisecow-image to run the container from image