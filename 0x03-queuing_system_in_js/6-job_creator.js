import { createQueue } from 'kue';

// Create a queue
const que = createQueue();

const job_object = {
	phoneNumber: '+251947123452',
	message: 'hello world',
}


// create job
const job = que.create('push_notification_code', job_object).save((err) => {
	if ( !err) console.log(`Notification job created: ${job.id}`);
});


// on complete
job.on('complete', () => {
	console.log('Notification job completed');
});


// on failure
job.on('failed', () => {
	console.log('Notification job failed');
});
