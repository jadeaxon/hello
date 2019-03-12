// Constructs a symbolic integer.
function SymbolicInteger(value, template) {
  // A 2D array specifying what symbols are legal in each place of the symbolic integer.
  // Least significant place first.
  this.template = template;
  this.value = null;
  this.truncateZeros = false;

  if (typeof value == "number") {
    this.value = value;
  }
  else if (typeof value == "string") {
    // Figure out the integer value based on the symbol string.
    this.value = 0;
    var multiplier = 1;
    var symbols = value.split("").reverse();
    for (var i = 0; i < symbols.length; i++) {
      if (i > 0) {
        multiplier = multiplier * this.template[i - 1].length;
      }

      var symbol = symbols[i];
      var place_value = this.template[i].indexOf(symbol);
      if (place_value == -1) {
        console.log("ERROR: Symbol " + symbol + " not allowed at place " + i + ".");
        // TO DO: Throw exception.
      }

      /// console.log("multiplier = " + multiplier);
      /// console.log("symbol = " + symbol);
      /// console.log("place = " + i);
      /// console.log("place value = " + place_value);

      this.value = this.value + (place_value * multiplier);
    } // next symbol
  }
  else { // Illegal value type.
    console.log("ERROR: Illegal value type for SymbolicInteger: " + typeof value);
    // TO DO: Throw exception.
  }

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
  }; // toSymbols();

  this.getValue = function () {
    return this.value;
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

  var si2 = new SymbolicInteger("C-c", template1);
  console.log("si2.getValue() = " + si2.getValue());

  // Count with lowercase alphanumeric symbols.
  var lcalphanum = '0123456789abcdefghijklmnopqrstuvwxyz'.split('');
  var template2 = [
    lcalphanum,
    lcalphanum,
    lcalphanum
  ];

  var si3 = new SymbolicInteger("06w", template2); // 248
  console.log("si3.getValue() = " + si3.getValue());

  for (var i = 0; i <= 256; i++) {
    var si = new SymbolicInteger(i, template2);
    var s = si.toSymbols();
    console.log(i + ' => ' + s);
  }
}
