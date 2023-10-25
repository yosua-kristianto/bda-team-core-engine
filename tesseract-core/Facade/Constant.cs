using Confluent.Kafka;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Tesseract;

namespace tesseract_core.Facade
{
    // This part contains constant used for the Tesseract.
    public class TesseractConstant
    {
        public static String TESSERACT_ENGINE_LANGUAGE = "eng";
        public static EngineMode TESSERACT_ENGINE_MODE = EngineMode.Default;
    }

    // This part contains constant used for Kafka Configuration.
    public class KafkaConfigConstant
    {
        public static String KAFKA_DEFAULT_GROUP_ID = "group-1";
        public static AutoOffsetReset KAFKA_DEFAULT_AUTO_OFFSET_RESET = AutoOffsetReset.Earliest;
    }
}
