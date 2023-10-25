using Confluent.Kafka;
using Microsoft.Extensions.Configuration;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using tesseract_core.Facade;

namespace tesseract_core.Messaging
{
    public abstract class BaseMessaging
    {
        // Uncontainerized configurations

        // Containerized configurations
        protected ConsumerConfig ConsumerConfig { get; }
        protected ProducerConfig ProducerConfig { get; }

        public BaseMessaging(IConfiguration config)
        {
            this.ConsumerConfig = new ConsumerConfig
            {
                BootstrapServers = config.GetValue<string>("KafkaServer") ?? "localhost:9092",
                GroupId = KafkaConfigConstant.KAFKA_DEFAULT_GROUP_ID,
                AutoOffsetReset = KafkaConfigConstant.KAFKA_DEFAULT_AUTO_OFFSET_RESET
            };

            this.ProducerConfig = new ProducerConfig
            {
                BootstrapServers = config.GetValue<string>("KafkaServer") ?? "localhost:9092",
            };
        }
    }
}
