using Confluent.Kafka;
using Microsoft.Extensions.Configuration;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Resources;
using System.Text;
using System.Threading.Tasks;
using Tesseract;
using tesseract_core.Facade;

namespace tesseract_core.Core
{
    /**
    * TesseractIntegration
    * @singleton
    * 
    * This class contains integration to Tesseract model.
    */
    internal class TesseractIntegration
    {
        private static TesseractIntegration _instance = null;
        private string tesseractFeederPath { get; }
        private TesseractEngine tesseractModel { get; }

        private TesseractIntegration()
        {
            this.tesseractFeederPath = AppDomain.CurrentDomain.BaseDirectory + "\\Resources\\Data\\";
            this.tesseractModel = new TesseractEngine(
                this.tesseractFeederPath,
                TesseractConstant.TESSERACT_ENGINE_LANGUAGE,
                TesseractConstant.TESSERACT_ENGINE_LANGUAGE
            );
        }

        public static TesseractIntegration GetInstance()
        {
            if (_instance == null)
            {
                _instance = new TesseractIntegration();
            }

            return _instance;
        }

        /**
         * Ocr
         * @public
         * 
         * This function will perform the TesseractEngine reading by loading
         * installed tesseract model, and using it to reverse image to text.
         * And then will return the string of the result of the reversed image.
         * 
         * @param string path
         *  The path to file.
         *  
         * @return string
         */
        public string Ocr(string path)
        {
            Pix imageToBeLoad = Pix.LoadFromFile(path);

            Page page = this.tesseractModel.Process(imageToBeLoad);

            return page.GetText();
        }
    }
}
