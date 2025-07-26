
using System.Diagnostics;

double total = 0;
long ticks = 0;

int repeat = 100;
long x = 0;

for (int outloop = 0; outloop < repeat; outloop++)
{
    var sw = Stopwatch.StartNew();
    for (int i = 0; i < 1_000_000; i++)
    {
        x += i + 1229;
    }
    sw.Stop();
    total += sw.Elapsed.TotalMilliseconds;
    ticks += sw.ElapsedTicks;
}

Console.WriteLine($"Elapsed time: {total / repeat} ms");
Console.WriteLine($"Elapsed time: {ticks / repeat * (1_000_000.0 / Stopwatch.Frequency):F2}us");
Console.WriteLine($"temp: {x}");

Console.ReadLine();