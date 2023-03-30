1. run in repo dir
    wget https://download.redis.io/redis-stable.tar.gz
2. run
    tar -xzvf redis-stable.tar.gz
    cd redis-stable
    make
3. start the redis server
    ./src/redis-server&
4. verify server is running
    ps aux | grep redis
    should respond with:
        student    4449  0.2  0.1  62256  6332 pts/4    Sl   08:34   0:00 ./redis-stable/src/redis-server *:6379
5. create a venv 
    python3 -m venv venv
6. activate the venv
    . venv/bin.activate
7. install redis and flask
    pip install redis 
    pip install flask 
    pip install scikit-build
    pip install opencv-python-headless
8. start the client 
    FLASK_NAME=client.py flask run