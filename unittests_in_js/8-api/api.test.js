const request = require('supertest');
const chai = require('chai');
const expect = chai.expect;
const app = require('./api');

describe('Index Page', () => {
  it('should return status code 200', (done) => {
    request(app)
      .get('/')
      .end((err, res) => {
        expect(res.status).to.equal(200);
        done();
      });
  });

  it('should return the correct result', (done) => {
    request(app)
      .get('/')
      .end((err, res) => {
        expect(res.text).to.equal('Welcome to the payment system');
        done();
      });
  });
});

