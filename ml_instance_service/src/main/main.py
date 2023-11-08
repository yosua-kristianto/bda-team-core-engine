"""
@todo
1. Run Spark Integrator
2. Run Tesseract 
"""

from core.ml_container import model_loader;
from ml_instance_service.src.main.core.spark_integrator import SparkIntegrator;
from ml_instance_service.src.main.spark.datalake_puller import SPARK_CONTEXT_NAME;

spark_instance = SparkIntegrator();
spark_instance.context_builder(context_name=SPARK_CONTEXT_NAME);