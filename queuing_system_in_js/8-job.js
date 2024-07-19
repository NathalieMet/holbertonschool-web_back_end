const kue = require('kue');

function createPushNotificationsJobs(jobs, queue) {
	if (!Array.isArray(jobs)) {
		throw new Error('Jobs is not an array');
	  }
	for (const jobData of jobs) {
		const job = queue.create('push_notification_code_3', jobData);
		job.save(function(err) {
			if (!err) {
			  console.log(`Notification job created: ${job.id}`);
			} else {
			  console.error('Error creating job:', err);
			}
		  });

		job.on('complete', function() {
			console.log(`Notification job ${job.id} completed`);
		  });

		job.on('failed', function(err) {
			console.log(`Notification job ${job.id} failed: ${err.message}`);
		  });
		job.on('progress', function(progress) {
			console.log(`Notification job ${job.id} ${progress}% complete`);
		  });
		}
}

module.exports = createPushNotificationsJobs;
