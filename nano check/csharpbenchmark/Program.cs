using System;
using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Running;

public class MyBenchmark
{
    public int Result{ get; set; }
    [Benchmark]
    public void AddOperation()
    {
        int x = 0;
        for (int i = 0; i < 1_000_000; i++)
        {
            x += i + 1229;
        }

        Result = x; // Prevent optimization
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        BenchmarkRunner.Run<MyBenchmark>();
    }
}
