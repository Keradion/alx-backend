import { createQueue } from 'kue';

const numbersBlacklisted = ['4153518780', '4153518781'];
const que = createQueue();

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (numbersBlacklisted.includes(phoneNumber)) return (new Error(`Phone number ${phoneNumber} is blacklisted`));
  
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

que.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
