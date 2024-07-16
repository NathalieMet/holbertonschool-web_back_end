const request = require('supertest');
const app = require('./api'); // Assurez-vous que ceci pointe vers votre fichier api.js
const { expect } = require('chai');

describe('Index Page', () => {
  it('should return status code 200', (done) => {
    request(app)
      .get('/')
      .expect(200, done);
  });

  it('should return the correct result', (done) => {
    request(app)
      .get('/')
      .expect('Content-Type', /text/)
      .expect((res) => {
        expect(res.text).to.equal('Welcome to the payment system');
      })
      .end(done);
  });
});
