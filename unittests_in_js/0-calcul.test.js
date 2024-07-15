const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe('calculate', function () {
  describe('calculateNumber()', function () {
    it('should round a and b and return the sum of it', function () {
      assert.equal(calculateNumber(2, 4), 6);
    });

	it('should round a and b and return the sum of it', function () {
		assert.equal(calculateNumber(2, 4.1), 6);
	});

	it('should round a and b and return the sum of it', function () {
		assert.equal(calculateNumber(2.9, 4.1), 7);
	});

	it('should round a and b and return the sum of it', function () {
		assert.equal(calculateNumber(2.5, 4.5), 7);
	});

	it('should round a and b and return the sum of it', function () {
		assert.equal(calculateNumber(100.3, 500), 600);
	});
  });
});
