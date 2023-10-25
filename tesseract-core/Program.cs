using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System;
using System.Runtime.CompilerServices;
using tesseract_core.Facade;
using tesseract_core.Handler;
using tesseract_core.Messaging;
using tesseract_core.Messaging.Consumer;
using tesseract_core.Messaging.Producer;

public class TesseractCore
{
    public IConfiguration Config { get; }

    // Dependency Injection
    private void ConfigureServices(IServiceCollection services)
    {
        Console.WriteLine("Calling Confiugre Services");

        Dictionary<string, string> envDictionary = new();

        foreach (var a in this.Config.AsEnumerable().ToList())
        {
            Console.WriteLine(a);
        }

    }

    public TesseractCore(IConfiguration configuration)
    {
        this.Config = configuration;
    }

    public static void Main(String[] args)
    {
        IHostBuilder host = Host.CreateDefaultBuilder(args)
            .ConfigureAppConfiguration((hostingContext, config) =>
            {
                config.SetBasePath(AppDomain.CurrentDomain.BaseDirectory);
                config.AddJsonFile("appsettings.json", optional: false, reloadOnChange: true);
            })
            .ConfigureServices((hostContext, services) =>
            {
                Console.WriteLine("-----Resolving DI");

                services.AddScoped<TesseractIntegratorHandler, TesseractIntegratorHandler>();
                
                services.AddScoped<BaseMessaging, OCRProcessorConsumer>();
                services.AddScoped<BaseMessaging, OCRResultProducer>();

                Console.WriteLine("-----Getting all data within appsettings.json");
                
                var config = hostContext.Configuration;
                
                Dictionary<string, string> envDictionary = new();

                foreach (var a in config.AsEnumerable().ToList())
                {
                    envDictionary.Add(a.Key, a.Value ?? "");
                }

                EnvironmentVariables.Instance(envDictionary);
            });
        Console.WriteLine(" _____                                  _      _____       _                       _             \r\n/__   \\___  ___ ___  ___ _ __ __ _  ___| |_    \\_   \\_ __ | |_ ___  __ _ _ __ __ _| |_ ___  _ __ \r\n  / /\\/ _ \\/ __/ __|/ _ \\ '__/ _` |/ __| __|    / /\\/ '_ \\| __/ _ \\/ _` | '__/ _` | __/ _ \\| '__|\r\n / / |  __/\\__ \\__ \\  __/ | | (_| | (__| |_  /\\/ /_ | | | | ||  __/ (_| | | | (_| | || (_) | |   \r\n \\/   \\___||___/___/\\___|_|  \\__,_|\\___|\\__| \\____/ |_| |_|\\__\\___|\\__, |_|  \\__,_|\\__\\___/|_|   \r\n                                                                   |___/                         ");
        host.Build().Run();
    }
}