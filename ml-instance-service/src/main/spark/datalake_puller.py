

from "ml-instance-service.src.main.core.spark_integrator" import SparkIntegrator


SPARK_CONTEXT_NAME = "DATALAKE_PULLER_CONTEXT";

def instantiate_puller():
    SparkIntegrator