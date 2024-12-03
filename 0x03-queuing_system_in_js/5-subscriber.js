import { createClient } from 'redis';

const subscriber = createClient(); // Create Redis Client

subscriber.on('connect', () => {
	console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err}`);
});

subscriber.subscribe('holberton school channel'); // Subscribe to the channel

subscriber.on('message', (channel, message) => {  // Display the recieved message
	console.log(`${message}`);
	if (message == 'KILL_SERVER') {
		subscriber.unsubscribe(channel)
		subscriber.quit();
	}
});
