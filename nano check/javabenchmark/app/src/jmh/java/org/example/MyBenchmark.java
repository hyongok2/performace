package org.example;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import java.util.concurrent.TimeUnit;

public class MyBenchmark {

    @BenchmarkMode(Mode.AverageTime)
    @OutputTimeUnit(TimeUnit.NANOSECONDS)
    @Benchmark
    public int testAdd() {
        int sum = 0;
        for (int i = 0; i < 1_000_000; i++) {
            sum += i + 1229;
        }
        return sum;
    }
}
