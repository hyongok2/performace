
using System.Diagnostics;

var sw = Stopwatch.StartNew();
for (int i = 0; i < 1_000_000; i++)
{
    int x = i + 1229;
}
sw.Stop();
Console.WriteLine($"Elapsed time: {sw.Elapsed.TotalMilliseconds} ms");
Console.WriteLine($"Elapsed time: {sw.ElapsedTicks * (1_000_000.0 / Stopwatch.Frequency):F2}us");