1. run in repo dir\n\twget https://download.redis.io/redis-stable.tar.gz
2. run
    tar -xzvf redis-stable.tar.gz
    cd redis-stable
    make
3. start the redis server
    ./redis-stable/src/redis-server&
4. verify server is running
    ps aux | grep redis
    should respond with:
        student    4449  0.2  0.1  62256  6332 pts/4    Sl   08:34   0:00 ./redis-stable/src/redis-server *:6379
5. install redis client 
    pip install redis
5. run the client code pip
    python client.py 