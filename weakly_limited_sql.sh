ulimit -Sv 5000000
timeout 10 node slow_sql.js "$@"
