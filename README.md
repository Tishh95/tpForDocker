
```` bash
.
├── app
│   ├── app.py
│   ├── Dockerfile
│   ├── __pycache__
│   │   ├── app.cpython-36.pyc
│   │   └── app.cpython-38.pyc
│   ├── requirements.txt
│   ├── templates
│   │   ├── admin.html
│   │   ├── cssTemplates
│   │   │   └── index.css
│   │   └── index.html
│   └── tests
│       └── test.py
├── docker-compose.yml
├── nginx
│   └── nginx.conf
└── README.md

````
Clone le projet

ensuite lance dans le cmd:
````
    sudo docker-compose build 
    sudo docker-compose up (lance les containers)
````
# Résultat du docker-compose up
````
Starting tpfordocker_db_1 ... done
Starting container_web    ... done
Starting tpfordocker_nginx_1 ... done
Starting tpfordocker_tests_1 ... done
Attaching to tpfordocker_db_1, container_web, tpfordocker_tests_1, tpfordocker_nginx_1
container_web |  * Serving Flask app 'app' (lazy loading)
container_web |  * Environment: production
container_web |    WARNING: This is a development server. Do not use it in a production deployment.
container_web |    Use a production WSGI server instead.
container_web |  * Debug mode: off
container_web |  * Running on all addresses.
container_web |    WARNING: This is a development server. Do not use it in a production deployment.
db_1     | {"t":{"$date":"2022-10-11T14:57:25.641+00:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"-","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.642+00:00"},"s":"I",  "c":"NETWORK",  "id":4915701, "ctx":"main","msg":"Initialized wire specification","attr":{"spec":{"incomingExternalClient":{"minWireVersion":0,"maxWireVersion":17},"incomingInternalClient":{"minWireVersion":0,"maxWireVersion":17},"outgoing":{"minWireVersion":6,"maxWireVersion":17},"isInternalClient":true}}}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.643+00:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
container_web |  * Running on http://172.23.0.3:5000/ (Press CTRL+C to quit)
db_1     | {"t":{"$date":"2022-10-11T14:57:25.644+00:00"},"s":"I",  "c":"REPL",     "id":5123008, "ctx":"main","msg":"Successfully registered PrimaryOnlyService","attr":{"service":"TenantMigrationDonorService","namespace":"config.tenantMigrationDonors"}}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.644+00:00"},"s":"I",  "c":"REPL",     "id":5123008, "ctx":"main","msg":"Successfully registered PrimaryOnlyService","attr":{"service":"TenantMigrationRecipientService","namespace":"config.tenantMigrationRecipients"}}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.644+00:00"},"s":"I",  "c":"REPL",     "id":5123008, "ctx":"main","msg":"Successfully registered PrimaryOnlyService","attr":{"service":"ShardSplitDonorService","namespace":"config.tenantSplitDonors"}}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.644+00:00"},"s":"I",  "c":"CONTROL",  "id":5945603, "ctx":"main","msg":"Multi threading initialized"}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.645+00:00"},"s":"I",  "c":"CONTROL",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":1,"port":27017,"dbPath":"/data/db","architecture":"64-bit","host":"test_mongodb"}}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.645+00:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"6.0.2","gitVersion":"94fb7dfc8b974f1f5343e7ea394d0d9deedba50e","openSSLVersion":"OpenSSL 1.1.1f  31 Mar 2020","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu2004","distarch":"x86_64","target_arch":"x86_64"}}}}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.645+00:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"20.04"}}}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.645+00:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"*"},"security":{"authorization":"enabled"}}}}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.646+00:00"},"s":"I",  "c":"STORAGE",  "id":22270,   "ctx":"initandlisten","msg":"Storage engine to use detected by data files","attr":{"dbpath":"/data/db","storageEngine":"wiredTiger"}}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.646+00:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
db_1     | {"t":{"$date":"2022-10-11T14:57:25.646+00:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=4298M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,remove=true,path=journal,compressor=snappy),builtin_extension_config=(zstd=(compression_level=6)),file_manager=(close_idle_time=600,close_scan_interval=10,close_handle_minimum=2000),statistics_log=(wait=0),json_output=(error,message),verbose=[recovery_progress:1,checkpoint_progress:1,compact_progress:1,backup:0,checkpoint:0,compact:0,evict:0,history_store:0,recovery:0,rts:0,salvage:0,tiered:0,timestamp:0,transaction:0,verify:0,log:0],"}}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.424+00:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":778}}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.424+00:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.431+00:00"},"s":"W",  "c":"CONTROL",  "id":5123300, "ctx":"initandlisten","msg":"vm.max_map_count is too low","attr":{"currentValue":65530,"recommendedMinimum":1677720,"maxConns":838860},"tags":["startupWarnings"]}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.433+00:00"},"s":"I",  "c":"NETWORK",  "id":4915702, "ctx":"initandlisten","msg":"Updated wire specification","attr":{"oldSpec":{"incomingExternalClient":{"minWireVersion":0,"maxWireVersion":17},"incomingInternalClient":{"minWireVersion":0,"maxWireVersion":17},"outgoing":{"minWireVersion":6,"maxWireVersion":17},"isInternalClient":true},"newSpec":{"incomingExternalClient":{"minWireVersion":0,"maxWireVersion":17},"incomingInternalClient":{"minWireVersion":17,"maxWireVersion":17},"outgoing":{"minWireVersion":17,"maxWireVersion":17},"isInternalClient":true}}}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.433+00:00"},"s":"I",  "c":"REPL",     "id":5853300, "ctx":"initandlisten","msg":"current featureCompatibilityVersion value","attr":{"featureCompatibilityVersion":"6.0","context":"startup"}}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.433+00:00"},"s":"I",  "c":"STORAGE",  "id":5071100, "ctx":"initandlisten","msg":"Clearing temp directory"}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.434+00:00"},"s":"I",  "c":"CONTROL",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.434+00:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/data/db/diagnostic.data"}}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.437+00:00"},"s":"I",  "c":"REPL",     "id":6015317, "ctx":"initandlisten","msg":"Setting new configuration state","attr":{"newState":"ConfigReplicationDisabled","oldState":"ConfigPreStart"}}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.437+00:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.438+00:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"/tmp/mongodb-27017.sock"}}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.438+00:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"0.0.0.0"}}
db_1     | {"t":{"$date":"2022-10-11T14:57:26.438+00:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":27017,"ssl":"off"}}
nginx_1  | 2022/10/11 14:57:26 [notice] 1#1: using the "epoll" event method
nginx_1  | 2022/10/11 14:57:26 [notice] 1#1: nginx/1.23.1
nginx_1  | 2022/10/11 14:57:26 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6)
nginx_1  | 2022/10/11 14:57:26 [notice] 1#1: OS: Linux 5.15.0-48-generic
nginx_1  | 2022/10/11 14:57:26 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
nginx_1  | 2022/10/11 14:57:26 [notice] 1#1: start worker processes
nginx_1  | 2022/10/11 14:57:26 [notice] 1#1: start worker process 8
nginx_1  | 2022/10/11 14:57:26 [notice] 1#1: start worker process 9
nginx_1  | 2022/10/11 14:57:26 [notice] 1#1: start worker process 10
nginx_1  | 2022/10/11 14:57:26 [notice] 1#1: start worker process 11
nginx_1  | 2022/10/11 14:57:26 [notice] 1#1: start worker process 12
tests_1  | ============================= test session starts ==============================
tests_1  | platform linux -- Python 3.6.15, pytest-7.0.1, pluggy-1.0.0
tests_1  | rootdir: /app
tests_1  | collected 1 item
tests_1  |
tests_1  | app/tests/test.py .                                                      [100%]
tests_1  |
tests_1  | ============================== 1 passed in 0.21s ===============================
tpfordocker_tests_1 exited with code 0
````

## a venir

modification de l'architecture pour un type mvc + crud

