#include <iostream>
#include <chrono>

int main() {

	int repeat = 100;
	long total = 0;
    // 측정 대상 연산
    long long x = 0; 

    for(int outloop = 0; outloop < repeat; outloop++) {
        // 시간 측정 시작
        auto start = std::chrono::high_resolution_clock::now();

        for (int i = 0; i < 1'000'000; i++) {
            x += i + 1229;
        }

        // 시간 측정 종료
        auto end = std::chrono::high_resolution_clock::now();
        // us 단위로 변환
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
		total += duration;
	}

    std::cout << "Elapsed time: " << total / repeat << " us" << std::endl;

    std::cout << "temp: " << x << std::endl;
    

	std::cin.get(); // Wait for user input before exiting

    return 0;
}