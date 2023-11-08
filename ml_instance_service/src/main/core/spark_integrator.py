from pyspark import SparkContext, SparkConf;

class SparkIntegrator:
    """
    @private
    Just in case we need another integration from spark.
    """
    __contexts = {};

    """
    @public
    context_builder

    This will create / return SparkContext instances by its App name.
    """
    def context_builder(self, context_name: str):
        
        try:
            self.__contexts[context_name]; # This line of code should throw an exception if the context with designated name is not available
        except:
            self.__contexts[context_name] = SparkContext(SparkConf().setAppName(context_name));
        
        return self.__contexts[context_name];

    def context_stop_session(self, context_name: str):
        self.context_builder(context_name).stop();
