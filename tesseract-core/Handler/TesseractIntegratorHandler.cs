using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using tesseract_core.Core;
using tesseract_core.Messaging.Consumer;
using tesseract_core.Messaging.Producer;

namespace tesseract_core.Handler
{
    internal class TesseractIntegratorHandler
    {
        private readonly OCRResultProducer OCRResultProducer;
        public TesseractIntegratorHandler(OCRResultProducer producer)
        {
            this.OCRResultProducer = producer;
        }

        public async void HandleOCR(string imagePath)
        {
            string extractedText = TesseractIntegration.GetInstance().Ocr(imagePath);

            // @todo: C/WER if available

            this.OCRResultProducer.Produce(extractedText);
        }
    }
}
