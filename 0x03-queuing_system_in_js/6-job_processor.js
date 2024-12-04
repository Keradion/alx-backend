import { createQueue } from 'kue';

const que = createQueue();

const sendNotification = (phoneNumber, message) => {
	console.log(`sending notfication to ${phoneNumber}, with message: ${message}`)
}

que.process('push_notification_code', (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message);
	done();
});
