using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tesseract_core.Model.DTO
{
    public class OCRProcessorConsumerDTO
    {
        [JsonRequired]

        [JsonProperty("image_path")]
        public string ImagePath { get; set; }
    }
}
