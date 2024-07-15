const calculateNumber = require('./1-calcul.js');
const assert = require('assert');

describe('calculate', function () {
  describe('calculateNumber(SUM)', function () {
    it('should round a and b and return the sum of it', function () {
      assert.equal(calculateNumber("SUM", 2, 4), 6);
    });

	it('should round a and b and return the sum of it', function () {
		assert.equal(calculateNumber("SUM", 2, 4.1), 6);
	});

	it('should round a and b and return the sum of it', function () {
		assert.equal(calculateNumber("SUM", 2.9, 4.1), 7);
	});

	it('should round a and b and return the sum of it', function () {
		assert.equal(calculateNumber("SUM", 2.5, 4.5), 8);
	});

	it('should round a and b and return the sum of it', function () {
		assert.equal(calculateNumber("SUM", 100.3, 500), 600);
	});
  });

  describe('calculateNumber(SUBTRACT)', function () {
    it('should round the two numbers, and subtract b from a', function () {
      assert.equal(calculateNumber("SUBTRACT", 10, 4), 6);
    });

	it('should round the two numbers, and subtract b from a', function () {
		assert.equal(calculateNumber("SUBTRACT", 10, 4.1), 6);
	});

	it('should round the two numbers, and subtract b from a', function () {
		assert.equal(calculateNumber("SUBTRACT", 7.9, 4.1), 4);
	});

	it('should round the two numbers, and subtract b from a', function () {
		assert.equal(calculateNumber("SUBTRACT", 8.5, 4.5), 4);
	});

	it('should round the two numbers, and subtract b from a', function () {
		assert.equal(calculateNumber("SUBTRACT", 600.3, 500), 100);
	});
  });

  describe('calculateNumber(DIVIDE)', function () {
    it('should round the two numbers, and divide a with b', function () {
      assert.equal(calculateNumber("DIVIDE", 10, 2), 5);
    });

	it('should round the two numbers, and divide a with b', function () {
		assert.equal(calculateNumber("DIVIDE", 10, 2.1), 5);
	});

	it('should round the two numbers, and divide a with b', function () {
		assert.equal(calculateNumber("DIVIDE", 7.9, 4.1), 2);
	});

	it('should round the two numbers, and divide a with b', function () {
		assert.equal(calculateNumber("DIVIDE", 9.5, 1.5), 5);
	});

	it('should round the two numbers, and divide a with b', function () {
		assert.equal(calculateNumber("DIVIDE", 600.3, 100), 6);
	});

	it('should round the two numbers, and divide a with b', function () {
		assert.equal(calculateNumber("DIVIDE", 10, 3), 3.3333333333333335);
	});

	it('should return the string Error if the rounded value of b is equal to 0, ', function () {
		assert.equal(calculateNumber("DIVIDE", 6, 0.2), "Error");
	});
  });
});
