public class TimeTest {
    public static void main(String[] args) {

        int repeat = 100;
        long total = 0;
        long x = 0;
        for (int outloop = 0; outloop < repeat; outloop++) {
            long start = System.nanoTime(); // 나노초 단위
            for (int i = 0; i < 1_000_000; i++) {
                x += i + 1229;
            }
            long end = System.nanoTime();
            total += (end - start) / 1_000; // 마이크로초 단위로 변환
        }
        System.out.println("소요 시간: " + total / repeat + " μs");
        System.out.println("x: " + x);
    }
}
