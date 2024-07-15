const calculateNumber = require('./2-calcul_chai.js');
const chai = require('chai');
const expect = chai.expect;

describe('calculate', function () {
  describe('calculateNumber(SUM)', function () {
    it('should round a and b and return the sum of it', function () {
		expect(calculateNumber("SUM", 2, 4)).to.equal(6);
    });

	it('should round a and b and return the sum of it', function () {
		expect(calculateNumber("SUM", 2, 4.1)).to.equal(6);
	});

	it('should round a and b and return the sum of it', function () {
		expect(calculateNumber("SUM", 2.9, 4.1)).to.equal(7);
	});

	it('should round a and b and return the sum of it', function () {
		expect(calculateNumber("SUM", 2.5, 4.5)).to.equal(8);
	});

	it('should round a and b and return the sum of it', function () {
		expect(calculateNumber("SUM", 100.3, 500)).to.equal(600);
	});
  });

  describe('calculateNumber(SUBTRACT)', function () {
    it('should round the two numbers, and subtract b from a', function () {
      expect(calculateNumber("SUBTRACT", 10, 4)).to.equal(6);
    });

	it('should round the two numbers, and subtract b from a', function () {
		expect(calculateNumber("SUBTRACT", 10, 4.1)).to.equal(6);
	});

	it('should round the two numbers, and subtract b from a', function () {
		expect(calculateNumber("SUBTRACT", 7.9, 4.1)).to.equal(4);
	});

	it('should round the two numbers, and subtract b from a', function () {
		expect(calculateNumber("SUBTRACT", 8.5, 4.5)).to.equal(4);
	});

	it('should round the two numbers, and subtract b from a', function () {
		expect(calculateNumber("SUBTRACT", 600.3, 500)).to.equal(100);
	});
  });

  describe('calculateNumber(DIVIDE)', function () {
    it('should round the two numbers, and divide a with b', function () {
      expect(calculateNumber("DIVIDE", 10, 2)).to.equal(5);
    });

	it('should round the two numbers, and divide a with b', function () {
		expect(calculateNumber("DIVIDE", 10, 2.1)).to.equal(5);
	});

	it('should round the two numbers, and divide a with b', function () {
		expect(calculateNumber("DIVIDE", 7.9, 4.1)).to.equal(2);
	});

	it('should round the two numbers, and divide a with b', function () {
		expect(calculateNumber("DIVIDE", 9.5, 1.5)).to.equal(5);
	});

	it('should round the two numbers, and divide a with b', function () {
		expect(calculateNumber("DIVIDE", 600.3, 100)).to.equal(6);
	});

	it('should round the two numbers, and divide a with b', function () {
		expect(calculateNumber("DIVIDE", 10, 3)).to.equal(3.3333333333333335);
	});

	it('should return the string Error if the rounded value of b is equal to 0, ', function () {
		expect(calculateNumber("DIVIDE", 6, 0.2)).to.equal("Error");
	});
  });
});
