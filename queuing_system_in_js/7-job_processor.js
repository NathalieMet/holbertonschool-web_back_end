const kue = require('kue');

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done){
	job.progress(0, 100); // Initialiser la progression à 0%

	if (blacklistedNumbers.includes(phoneNumber)) {
		return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
	}

	// Mettre à jour la progression à 50%
	job.progress(50, 100);

	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

	done();
  }

  const queue = kue.createQueue();

  // Configurer le traitement des travaux de la file d'attente push_notification_code_2
  queue.process('push_notification_code_2', 2, function(job, done) {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message, job, done);
  });
