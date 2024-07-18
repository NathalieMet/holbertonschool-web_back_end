const kue = require('kue');

// Créer une nouvelle file d'attente Kue
const queue = kue.createQueue();

// Définir les données de l'emploi
const jobData = {
  phoneNumber: 'my phone number',
  message: 'this is a phone number',
};

// Créer un travail dans la file d'attente 'push_notification_code'
const job = queue.create('push_notification_code', jobData)
  .save(function(err) {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error('Error creating job:', err);
    }
  });

// Écouter les événements sur le travail
job.on('complete', function() {
  console.log('Notification job completed');
});

job.on('failed', function() {
  console.log('Notification job failed');
});
