// Constructs a symbolic integer.
function SymbolicInteger(value, template) {
  // A 2D array specifying what symbols are legal in each place of the symbolic integer.
  // Least significant place first.
  this.template = template;

  this.value = value;
  this.truncateZeros = false;

  this.toSymbols = function () {
    var remaining = this.value;
    var symbols = '';

    // Figure out the symbols from left to right (most significant to least).
    for (var place = this.template.length - 1; place >= 0; place--) {
      var multiplier = 1;
      var symbol = '';
      // Incrementing each place results in using up the value of
      // the multiple of the sizes of all the places before it.
      // Like with 10-base digits you have n0*10^0 + n1*10^1 + n2*10^2.
      // This is like that but each place has a variable size.
      for (var i = place - 1; i >= 0; i--) {
        /// console.log("i = " + i);
        multiplier = multiplier * this.template[i].length;
      } // next factor

      /// console.log("place = " + place);
      /// console.log("multiplier = " + multiplier);

      // If no remaining value is left, all symbols are zero equivalents.
      if (remaining == 0) {
        symbol = this.template[place][0];
        symbols = symbols + symbol;
        /// console.log(place + '-' + place_value + ' => ' + symbol);
        continue;
      }

      // Determine the biggest value we can use for the current most significant place.
      var max_place_value = this.template[place].length - 1;
      for (var place_value = max_place_value; place_value >= 0; place_value--) {
        /// console.log('remaining = ' + remaining);
        remaining = remaining - (place_value * multiplier);
        if (remaining < 0) {
          // We could not use this big a value for this place.  Give remaining value back.
          remaining = remaining + (place_value * multiplier);
        } else { // remaining >= 0
          // We've found the biggest value we can use for this place.
          symbol = this.template[place][place_value];
          symbols = symbols + symbol;
          /// console.log(place + '-' + place_value + ' => ' + symbol);
          break;
        }
      } // next potential biggest place value
    } // next most significant place

    if (remaining != 0) {
      // The value is to big to be represented given the template constraints.
      console.log("ERROR: Value overflow: " + this.value);
    }
    return symbols;
  };

} // SymbolicInteger()


function testSymbolicInteger() {
  var template1 = [
    ['a', 'b', 'c'], // Least significant place (rightmost).
    ['-'],
    ['A', 'B', 'C']
  ];

  for (var i = 0; i <= 8; i++) {
    var si = new SymbolicInteger(i, template1);
    var s = si.toSymbols();
    console.log(i + ' => ' + s);
  }

  // Count with lowercase alphanumeric symbols.
  var lcalphanum = '0123456789abcdefghijklmnopqrstuvwxyz'.split('');
  var template2 = [
    lcalphanum,
    lcalphanum,
    lcalphanum
  ];

  for (var i = 0; i <= 256; i++) {
    var si = new SymbolicInteger(i, template2);
    var s = si.toSymbols();
    console.log(i + ' => ' + s);
  }
}
