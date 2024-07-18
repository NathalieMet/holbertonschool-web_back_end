import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to create the hash using hset
function createHash() {
	client.hset('HolbertonSchools', 'Portland', 50, redis.print);
	client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
	client.hset('HolbertonSchools', 'New York', 20, redis.print);
	client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
	client.hset('HolbertonSchools', 'Cali', 40, redis.print);
	client.hset('HolbertonSchools', 'Paris', 2, redis.print);
  }

  // Function to display the hash using hgetall
  function displayHash() {
	client.hgetall('HolbertonSchools', (err, reply) => {
	  if (err) {
		console.error('Error fetching hash:', err);
		return;
	  }
	  console.log(reply);
	});
  }

  // Execute the operations
  createHash();

  // Introducing a small delay to ensure that createHash() operations complete before displayHash()
  setTimeout(() => {
	displayHash();
  }, 500); // Adjust the delay as needed based on your Redis server response time
