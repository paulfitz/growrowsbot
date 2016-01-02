import subprocess

def run_regular_sql(user_id, txt):
    import json
    import sqlite3
    db = sqlite3.connect('/tmp/{}.sqlite3'.format(user_id))
    try:
        result = db.cursor().execute(txt).fetchall()
        db.commit()
        return json.dumps(result)
    except sqlite3.Error as e:
        return e.args[0]
    db.close()

def run_slow_sql(user_id, txt):
    fname = '/tmp/{}.sqlite3'.format(user_id)

    proc = subprocess.Popen(['bash', './weakly_limited_sql.sh', fname],
                            stdout=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    proc.stdin.write(txt)
    proc.stdin.close()
    result = proc.stdout.read()
    proc.wait()
    result = result.replace('\n','')
    return result

if __name__ == '__main__':
    print run_slow_sql("zig", "create table things(a,b)")
    print run_slow_sql("zig", "insert into things values('square',14)")
    print run_slow_sql("zig", "select * from things")
    print run_slow_sql("zig", "insert into things values('circle',16)")
    print run_slow_sql("zig", "select * from things")

