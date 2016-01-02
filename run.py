from botomatic import TBot
from slow_sql import run_slow_sql
import time

class GrowRowsBot(TBot):
    debug_mode = False

    def __init__(self):
        self.acted = False
        handle = "growrows"
        super(GrowRowsBot, self).__init__(handle)

    def run(self):
        for msg in self.handle_mentions():
            txt = msg.text
            txt = txt.split('@growrows')[1]
            user_id = msg.user.id_str
            print user_id
            print txt
            result = run_slow_sql(user_id, txt)
            reply = "@%s %s" % (msg.user.screen_name, result)
            print reply
            self.tweets.append((reply, msg.id))
            self.acted = True

        self.wrap_up()

if __name__ == '__main__':
    print run_slow_sql('check', 'create table things(a,b)')
    print run_slow_sql('check', 'insert into things values("x",1)')
    print run_slow_sql('check', 'select * from things')
    while True:
        print "scanning..."
        p = GrowRowsBot()
        time.sleep(60)
