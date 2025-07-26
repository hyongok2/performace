const Benchmark = require('benchmark');
const suite = new Benchmark.Suite();
let sink = 0; // 결과를 저장하기 위한 변수

function testAdd() {
  let sum = 0;
  for (let i = 0; i < 1_000_000; i++) {
    sum += i + 1229;
  }
  sink = sum;
  return sum;
}

suite
  .add('testAdd', testAdd)
  .on('cycle', event => {
    console.log(String(event.target));
  })
  .on('complete', function () {
    console.log('Fastest is ' + this.filter('fastest').map('name'));
  })
  .run({ async: false }); // sync 실행이 디버깅에 좋음
