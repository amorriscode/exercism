//
// This is only a SKELETON file for the "Leap" exercise. It's been provided as a
// convenience to get you started writing code faster.
//

class Year { 
  constructor(input) {
    this.value = input;
  }

  isLeap() {
    if (this.value % 4 === 0) {
      if (this.value % 100 === 0 && this.value % 400 === 0) {
        return true;
      } else if (this.value % 100 != 0) {
        return true;
      }
    }
  
    return false;
  }
}

module.exports = Year;
