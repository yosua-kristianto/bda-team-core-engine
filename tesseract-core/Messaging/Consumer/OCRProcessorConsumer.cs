using Confluent.Kafka;
using Microsoft.Extensions.Configuration;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using tesseract_core.Facade;
using tesseract_core.Handler;
using tesseract_core.Model.DTO;

namespace tesseract_core.Messaging.Consumer
{
    internal class OCRProcessorConsumer : BaseMessaging
    {
        public static string TOPIC = "IMAGE_OCR_PROCESSOR_TOPIC";
        private readonly TesseractIntegratorHandler Handler;

        public OCRProcessorConsumer(IConfiguration config, TesseractIntegratorHandler handler): base(config)
        {
            this.Handler = handler;
        }

        public void Consume()
        {
            using (var consumer = new ConsumerBuilder<string, OCRProcessorConsumerDTO>(this.ConsumerConfig).Build())
            {
                consumer.Subscribe(OCRProcessorConsumer.TOPIC);
                Console.WriteLine("IMAGE_OCR_PROCESSOR_TOPIC Consumer is running");

                try
                {
                    while (true)
                    {
                        var session = consumer.Consume();

                        OCRProcessorConsumerDTO message = session.Message.Value;

                        this.Handler.HandleOCR(message.ImagePath);
                    }
                }
                catch (Exception e)
                {
                    Log.E("Error when consuming topic of " + OCRProcessorConsumer.TOPIC + ": " + e.Message);
                    consumer.Close();
                }
            }
        }
    }
}
