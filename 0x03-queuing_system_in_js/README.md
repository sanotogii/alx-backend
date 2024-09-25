# Redis and Node.js Queuing System

## Description
This project demonstrates the use of Redis, a powerful in-memory data structure store, with Node.js. It covers basic Redis operations, asynchronous handling, and building a Redis-based queuing system using Kue. The project also integrates with Express.js to create web applications that interact with Redis.

## Learning Objectives
By the end of this project, you should be able to:
- Set up and run a Redis server on your local machine.
- Execute basic Redis operations using a client.
- Integrate Redis with Node.js to perform basic and advanced operations.
- Use hash data types and handle asynchronous Redis operations.
- Implement a simple Redis-based queue system using Kue.
- Build a basic Express app that interacts with Redis and a Redis queue.

## Requirements
- Redis 5.0.7 or later
- Node.js 12.x
- Ubuntu 18.04
- All files should end with a new line.
- A `README.md` file is mandatory at the root of the project.
- All JavaScript files should have the `.js` extension.

## Project Setup
1. **Install Redis:**
   - Download and install Redis 6.0.10 or later using:
     ```bash
     $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
     $ tar xzf redis-6.0.10.tar.gz
     $ cd redis-6.0.10
     $ make
     ```
   - Start the Redis server in the background:
     ```bash
     $ src/redis-server &
     ```

2. **Install Node.js dependencies:**
   - Run `npm install` after cloning the repository and navigating to the project folder:
     ```bash
     $ npm install
     ```

## Tasks Overview

### 0. Install Redis Instance
- Set up a Redis instance, start the server, and perform basic operations using the Redis CLI.

### 1. Node Redis Client
- Implement a Redis client that logs successful connections or errors when connecting to the Redis server.

### 2. Basic Redis Operations
- Create functions to set and get values from Redis, using callbacks to handle asynchronous operations.

### 3. Async Redis Operations
- Use the `promisify` library to handle Redis operations asynchronously with ES6 `async`/`await`.

### 4. Advanced Redis Operations
- Store and retrieve hash values in Redis using `hset` and `hgetall`.

### 5. Redis Publisher and Subscriber
- Set up a Redis-based pub/sub system where messages can be published to and received from a Redis channel.

### 6. Redis-based Queue with Kue
- Create a Redis-based job queue system using Kue. Jobs will be generated and processed asynchronously.

## Required Files
- **`package.json`**: Contains dependencies and scripts for running the project.
- **`.babelrc`**: Configures Babel to support ES6 syntax.
- **`dump.rdb`**: Redis data dump file.

## Usage
- To start any Node.js script:
  ```bash
  $ npm run dev <script_name.js>
  ```

## Repository Structure
```bash
alx-backend/
└── 0x03-queuing_system_in_js/
    ├── 0-redis_client.js
    ├── 1-redis_op.js
    ├── 2-redis_op_async.js
    ├── 4-redis_advanced_op.js
    ├── 5-subscriber.js
    ├── 5-publisher.js
    ├── dump.rdb
    ├── package.json
    └── README.md
```