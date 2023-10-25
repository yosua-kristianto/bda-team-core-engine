using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tesseract_core.Model.DTO
{
    public class OCRResultProducerDTO
    {
        [JsonRequired]

        [JsonProperty("extracted_text")]
        public string ExtractedText { get; set; }
    }
}
