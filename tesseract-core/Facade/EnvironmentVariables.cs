using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tesseract_core.Facade
{
    /**
     * @config
     * @singleton
     * EnvironmentVariables
     * 
     * This class is the helper for extracting selected values from the appsettings file to 
     * serialized value for easier accessibility.
     */
    public class EnvironmentVariables
    {
        private static EnvironmentVariables _instance = null;
        private Dictionary<string, string> keys = new();

        private EnvironmentVariables() { }

        public static EnvironmentVariables Instance(Dictionary<string, string> setupKeys)
        {
            if (_instance == null)
            {
                _instance = new EnvironmentVariables();
                _instance.keys = setupKeys;
            }
            return _instance;
        }

        public static EnvironmentVariables GetInstance() => _instance;

        /**
         * @public 
         * Key
         * 
         * This function used for retrieving registered value within keys by determined key name.
         */
        public string Key(string key)
        {
            return this.keys[key];
        }
    }
}
