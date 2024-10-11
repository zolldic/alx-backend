import { createClient } from 'redis';

try {
  const client = await createClient()
  await client.connect()
} catch (err) {
  console.log(`Redis client not connected to the server: ${err}`);
}
