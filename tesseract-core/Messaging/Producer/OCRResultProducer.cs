using Confluent.Kafka;
using Microsoft.Extensions.Configuration;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using tesseract_core.Facade;
using tesseract_core.Messaging.Consumer;
using tesseract_core.Model.DTO;

namespace tesseract_core.Messaging.Producer
{
    internal class OCRResultProducer : BaseMessaging
    {
        public static string TOPIC = "IMAGE_OCR_RESULTANT_TOPIC";

        public OCRResultProducer(IConfiguration config): base(config) { }

        public async void Produce(String ocrResult)
        {
            // @link https://github.com/confluentinc/confluent-kafka-dotnet
            Action<DeliveryReport<Null, string>> handler = r =>
                Console.WriteLine(!r.Error.IsError
                    ? $"Delivered message to {r.TopicPartitionOffset}"
                    : $"Delivery Error: {r.Error.Reason}");

            using(var producer = new ProducerBuilder<string, OCRResultProducerDTO>(this.ProducerConfig).Build())
            {

                try
                {
                    producer.Produce(OCRResultProducer.TOPIC, new Message<string, OCRResultProducerDTO> 
                    { 
                        Value = new OCRResultProducerDTO 
                        { ExtractedText = ocrResult } 
                    });
                }
                catch (Exception e)
                {
                    Log.E("Error when producing topic of " + OCRResultProducer.TOPIC + ": " + e.Message);
                }
            }
        }
    }
}
