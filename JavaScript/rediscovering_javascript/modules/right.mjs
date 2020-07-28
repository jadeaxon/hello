console.log('executing right module');

const message = 'right called';

export const right = function() {
  console.log(message);
};