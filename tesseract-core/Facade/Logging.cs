using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tesseract_core.Facade
{
    /**
     * Logging
     * 
     * This class used for making custom-made log. 
     * The target of this functionality is writing the log with given format for better text-mining searching. 
     */
    public class Log
    {
        private static readonly string INFO = "INFO";
        private static readonly string ERROR = "ERROR";

        // Prevent any instance creation outside this class
        private Log() { }

        /**
         * @private
         * @void
         * WriteLog
         * 
         * This function will directly organize log message to be written in the respective place.
         * 
         * This function's algorithm will be executed as below:
         * 
         * 1. Get current time with format of Y-m-d H:i:s
         * 2. Get current time with format of Ymd
         * 3. Write log with format of [Y-m-d H:i:s] [LOG_TYPE] [Message]
         * 4. If there is file named as number 2 in destinated folder on "CustomLogRepository" in appsettings.json
         *      4.1 Append the generated log in number 3 to the file
         *      4.2 Else, write new file with name as number 2 with format of *.log
         */
        private static void WriteLog(string message, string logType)
        {
            DateTime currentTime = DateTime.Now;

            // Call out step 1 & 2
            string currentTimeInString = currentTime.ToString("yyyy-MM-dd H:m:s.FFFF zzz");
            string currentDateInString = currentTime.ToString("yyyyMMdd");

            // Call out step 3
            string logToBeWritten = "[" + currentTimeInString + "]"
                                        + "[" + logType + "]"
                                        + message;

            string directoryPath = EnvironmentVariables.GetInstance().Key("default-log-path");
            string pathToLog = directoryPath + "/" + currentDateInString + ".log";

            FileStream stream;
            // Call out 4 & 4.1
            if (!File.Exists(pathToLog))
            {
                if (!Directory.Exists(directoryPath))
                {
                    Directory.CreateDirectory(directoryPath);
                }

                File.Create(pathToLog);
            }

            // I'm expecting that in this step, the log file has been created and ready to be written off
            File.AppendAllText(pathToLog, logToBeWritten + "\n");
        }

        /**
         * @static
         * @public
         * @void
         * I
         * 
         * This function will help with writing the INFO type log to the destinated path.
         */
        public static void I(string logContent)
        {
            Log.WriteLog(logContent, Log.INFO);
        }

        /**
         * @static
         * @public
         * @void
         * E
         * 
         * This function will help with writing the ERROR type log to the destinated path.
         */
        public static void E(string logContent)
        {
            Log.WriteLog(logContent, Log.ERROR);
        }
    }
}
