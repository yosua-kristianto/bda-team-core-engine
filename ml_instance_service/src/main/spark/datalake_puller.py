

from ml_instance_service.src.main.spark.datalake_puller import SparkIntegrator


SPARK_CONTEXT_NAME = "DATALAKE_PULLER_CONTEXT";

def instantiate_puller():
    SparkIntegrator