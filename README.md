# growrowsbot

Nothing to see here, just thinking out loud.

This is a little twitter bot that takes SQL tweeted at it and applies it to a sql database (1 database per twitter user).

The bot is running at `@growrows`.

Example dialogue:

```
@growrows create table test(color, hex)
  []
@growrows insert into test values('red','f00')
  []
@growrows insert into test values('green','0f0')
  []
@growrows select * from test
  [["red","f00"],["green","0f0"]] 
```
