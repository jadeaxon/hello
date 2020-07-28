/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
const fibonocciSeries = function*() {
  let current = 1;
  let next = 1;

  yield* [current, next];

  while(true) {
    const temp = current;
    current = next;
    next = next + temp;

    yield next;
  }
}

for(const value of fibonocciSeries()) {
  if(value > 25) break;
  process.stdout.write(value + ", ");
}
