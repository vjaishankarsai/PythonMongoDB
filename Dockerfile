FROM python
RUN apt-get update && apt-get install vim -y
COPY FirstSample.py /repo/
RUN pip install pymongo
