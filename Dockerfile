FROM jupyter/pyspark-notebook:spark-3.5.0

USER root

# Set up necessary permissions
RUN chmod -R 777 /home/jovyan

USER jovyan

RUN pip3 install delta-spark