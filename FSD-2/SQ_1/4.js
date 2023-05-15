class CLASS {
  constructor(arg1, arg2) {
    this.a = arg1;
    this.b = arg2;
  }

  // Methods
  msg() {
    return `Text running`;
  }
  // Static method
  static add(a, b) {
    return a + b;
  }
}
obj1 = new CLASS("value1", "value2");
console.log(obj1.msg());
console.log(CLASS.add(34, 5));
