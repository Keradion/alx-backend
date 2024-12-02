import redis from 'redis'

const client = redis.createClient();

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error}`)
});


client.on('connect', () => {
	console.log(`Redis client connected to the server`)
});


const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, redis.print); // Set a value under key in redis cache
};

const displaySchoolValue = (schoolName) => {
	client.get(schoolName, (error, value) => { 
		console.log(value)
	});

}

displaySchoolValue('Holberton'); // Try to display a non existing key value
setNewSchool('HolbertonSanFrancisco', '100'); // Set a new key
displaySchoolValue('HolbertonSanFrancisco'); // Read a value under a key
