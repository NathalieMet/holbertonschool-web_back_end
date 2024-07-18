const kue = require('kue');

// Créer une nouvelle file d'attente Kue
const queue = kue.createQueue();

function sendNotification(phoneNumber, message){
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}

queue.process('push_notification_code', function(job, done) {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message);
	done();
  });
