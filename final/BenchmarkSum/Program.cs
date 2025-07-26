using System;
using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Running;

[MemoryDiagnoser]
public class SumBenchmarks
{
    private const int N = 100_000_000;

    // 1. For loop (basic)
    [Benchmark]
    public long ForLoop()
    {
        long sum = 0;
        for (int i = 1; i <= N; i++)
            sum += i;
        return sum;
    }

    // 2. While loop
    [Benchmark]
    public long WhileLoop()
    {
        long sum = 0;
        int i = 1;
        while (i <= N)
        {
            sum += i;
            i++;
        }
        return sum;
    }

    // 3. Enumerable.Range + Sum
    [Benchmark]
    public long LinqSum()
    {
        return System.Linq.Enumerable.Range(1, N).Sum(x => (long)x);
    }

    // 4. Arithmetic formula
    [Benchmark]
    public long Formula()
    {
        return ((long)N * ((long)N + 1)) / 2;
    }

    // 5. Parallel.For (멀티스레드 테스트)
    [Benchmark]
    public long ParallelFor()
    {
        object lockObj = new object();
        long sum = 0;

        System.Threading.Tasks.Parallel.For(1, N + 1, () => 0L,
            (i, _, localSum) => localSum + i,
            localSum => {
                lock (lockObj) sum += localSum;
            });

        return sum;
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        BenchmarkRunner.Run<SumBenchmarks>();
    }
}
