"""
@todo
1. Run Spark Integrator
2. Run Tesseract 
"""

import sys;
from core.ml_container import model_loader;
from handler.datalake_puller_handler import handle_datalake_puller;

# from ml_instance_service.src.main.core.spark_integrator import SparkIntegrator;
# from ml_instance_service.src.main.spark.datalake_puller import SPARK_CONTEXT_NAME;

# spark_instance = SparkIntegrator();
# spark_instance.context_builder(context_name=SPARK_CONTEXT_NAME);

# spark_instance.__contexts[SPARK_CONTEXT_NAME];

print("""\n
   /  |/  /___ ______/ /_  (_)___  ___     / /   ___  ____ __________  (_)___  ____ _
  / /|_/ / __ `/ ___/ __ \\/ / __ \\/ _ \\   / /   / _ \\/ __ `/ ___/ __ \\/ / __ \\/ __ `/
 / /  / / /_/ / /__/ / / / / / / /  __/  / /___/  __/ /_/ / /  / / / / / / / / /_/ / 
/_/  /_/\\__,_/\\___/_/_/_/_/_/ /_/\\___/  /_____/\\___/\\__,_/_/  /_/ /_/_/_/ /_/\\__, /  
                    /  _/___  _____/ /_____ _____  ________                 /____/   
                    / // __ \\/ ___/ __/ __ `/ __ \\/ ___/ _ \\                         
                  _/ // / / (__  ) /_/ /_/ / / / / /__/  __/                         
                 /___/_/ /_/____/\\__/\\__,_/_/ /_/\\___/\\___/                          
                                                                                     
""")

SPARK_AVAILABILITY = "yes";

# Get configuration within argument variables
for i in sys.argv:
    if "--spark=" in i:
        separator_index = i.find("=");
        config_value = i[(separator_index+1):];

        if config_value != "yes" and config_value != "no":
            raise Exception("The argument of \"--spark\" configuration must be either \"yes\" or \"no\"");

        SPARK_AVAILABILITY = config_value;

# Call out the the business logic

handle_datalake_puller(SPARK_AVAILABILITY);