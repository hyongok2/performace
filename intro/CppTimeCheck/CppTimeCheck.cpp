#include <iostream>
#include <chrono>

int main() {

	int repeat = 100;
	long total = 0;

    for(int outloop = 0; outloop < repeat; ++outloop) {
        // 시간 측정 시작
        auto start = std::chrono::high_resolution_clock::now();

        // 측정 대상 연산
        volatile int x = 0; // 최적화 방지를 위해 volatile 사용
        for (int i = 0; i < 1'000'000; ++i) {
            x = i + 1229;
        }

        // 시간 측정 종료
        auto end = std::chrono::high_resolution_clock::now();
        // us 단위로 변환
        auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();
		total += duration;
	}

    std::cout << "Elapsed time: " << total / repeat << " ns" << std::endl;

	std::cin.get(); // Wait for user input before exiting

    return 0;
}