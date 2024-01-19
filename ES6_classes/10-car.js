const cloneCarSymbol = Symbol('cloneCar');

export default class Car {
	constructor(brand, motor, color) {
	  this._brand = brand;
	  this._motor = motor;
	  this._color = color;

	  this[cloneCarSymbol] = function () {
		return new this.constructor(this._brand, this._motor, this._color);
	  };
	}

	get brand() {
	  return this._brand;
	}

	get motor() {
	  return this._motor;
	}

	get color() {
	  return this._color;
	}

	cloneCar() {
	  return this[cloneCarSymbol]();
	}
  }
