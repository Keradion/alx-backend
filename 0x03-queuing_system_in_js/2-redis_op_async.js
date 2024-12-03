import { createClient } from 'redis'

const client = createClient();

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error}`)
});


client.on('connect', () => {
	console.log('Redis client connected to the server')
});


const setNewSchool = async (schoolName, value) => {
	try {
		await client.set(schoolName, value);
	} catch (error) {}
};

const displaySchoolValue = async (schoolName) => {
	try {
		const value = await client.get(schoolName);
		console.log(value)
	} catch (error) {}
}

displaySchoolValue('Holberton'); // Try to display a non existing key value
setNewSchool('HolbertonSanFrancisco', '100'); // Set a new key
displaySchoolValue('HolbertonSanFrancisco'); // Read a value under a key
