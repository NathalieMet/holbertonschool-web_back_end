const request = require('supertest');
const { expect } = require('chai');
const app = require('./api');
let server;

describe('Index Page', () => {
  // Démarrer le serveur avant les tests
  before((done) => {
    server = app.listen(7865, done);
  });

  // Arrêter le serveur après les tests
  after((done) => {
    server.close(done);
  });

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

