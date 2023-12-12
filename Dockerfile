FROM python:3

RUN mkdir -p /app
COPY /src/* /app/
WORKDIR /app
#RUN pip install -r requirements.lock
#EXPOSE 8080
CMD [ "python", "/app/newton.py" ]
#ENTRYPOINT [ "python" ]
