class Year { 
  constructor(input) {
    this.year = input;
  }

  isLeap() {
    if (this.year % 4 !== 0) {
      return false;
    }

    return (this.year % 100 === 0 && this.year % 400 === 0) || (this.year % 100 != 0);
  }
}

module.exports = Year;
