const repeat = 100;
let total = 0;
let x = 0;

for (let outloop = 0; outloop < repeat; outloop++) {
    const start = process.hrtime.bigint();  // 나노초 단위 정밀 시간
    for (let i = 0; i < 1_000_000; i++) {
        x += i + 1229;
    }
    const end = process.hrtime.bigint();
    total += Number(end - start) / 1000;  // 마이크로초 단위로 변환
}

console.log(`소요 시간: ${Math.round(total / repeat)} μs`);
console.log(`임시: ${x}`);
