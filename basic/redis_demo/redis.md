##概述
redis是一种支持分布式的nosql数据库,他的数据是保存在内存中，
同时redis可以定时把内存数据同步到磁盘，即可以将数据持久化，
并且他比memcached支持更多的数据结构(string,list列表[队列和栈],set[集合],sorted set[有序集合],hash(hash表))。
相关参考文档：http://redisdoc.com/index.html

##redis使用场景：
登录会话存储：存储在redis中，与memcached相比，数据不会丢失。

排行版/计数器：比如一些秀场类的项目，经常会有一些前多少名的主播排名。还有一些文章阅读量的技术，或者新浪微博的点赞数等。

作为消息队列：比如celery就是使用redis作为中间人。

当前在线人数：还是之前的秀场例子，会显示当前系统有多少在线人数。

一些常用的数据缓存：比如我们的BBS论坛，板块不会经常变化的，但是每次访问首页都要从mysql中获取，可以在redis中缓存起来，不用每次请求数据库。

把前200篇文章缓存或者评论缓存：一般用户浏览网站，只会浏览前面一部分文章或者评论，那么可以把前面200篇文章和对应的评论缓存起来。用户访问超过的，就访问数据库，并且以后文章超过200篇，则把之前的文章删除。

好友关系：微博的好友关系使用redis实现。

发布和订阅功能：可以用来做聊天软件。

##redis和memcached的比较：
memcached	redis
类型	纯内存数据库	内存磁盘同步数据库
数据类型	在定义value时就要固定数据类型	不需要
虚拟内存	不支持	支持
过期策略	支持	支持
存储数据安全	不支持	可以将数据同步到dump.db中
灾难恢复	不支持	可以将磁盘中的数据恢复到内存中
分布式	支持	主从同步
订阅与发布	不支持	支持
#redis在ubuntu系统中的安装与启动
安装：
 sudo apt-get install redis-server
卸载：
 sudo apt-get purge --auto-remove redis-server
 
启动：redis安装后，默认会自动启动，可以通过以下命令查看：

 ps aux|grep redis
 
如果想自己手动启动，可以通过以下命令进行启动：

 sudo service redis-server start
 
停止：

 sudo service redis-server stop
 
#redis在windows系统中的安装与启动：
下载：redis官方是不支持windows操作系统的。但是微软的开源部门将redis移植到了windows上。因此下载地址不是在redis官网上。而是在github上：https://github.com/MicrosoftArchive/redis/releases。

安装：点击一顿下一步安装就可以了。

运行：进入到redis安装所在的路径然后执行redis-server.exe redis.windows.conf就可以运行了。

连接：redis和mysql以及mongo是一样的，都提供了一个客户端进行连接。输入命令redis-cli（前提是redis安装路径已经加入到环境变量中了）就可以连接到redis服务器了。

其他机器访问本机redis服务器：
想要让其他机器访问本机的redis服务器。那么要修改redis.conf的配置文件，将bind改成bind [自己的ip地址或者0.0.0.0]，其他机器才能访问。
注意：bind绑定的是本机网卡的ip地址，而不是想让其他机器连接的ip地址。如果有多块网卡，那么可以绑定多个网卡的ip地址。如果绑定到额是0.0.0.0，那么意味着其他机器可以通过本机所有的ip地址进行访问。

#对redis的操作
对redis的操作可以用两种方式，第一种方式采用redis-cli，第二种方式采用编程语言，比如Python、PHP和JAVA等。

使用redis-cli对redis进行字符串操作：

#启动redis：

  sudo service redis-server start
连接上redis-server：
  redis-cli -h [ip] -p [端口]
添加：

  set key value
  如：
  set username xiaotuo
将字符串值value关联到key。如果key已经持有其他值，set命令就覆写旧值，无视其类型。并且默认的过期时间是永久，即永远不会过期。

删除：

  del key
  如：
  del username
设置过期时间：

  expire key timeout(单位为秒)
也可以在设置值的时候，一同指定过期时间：

  set key value EX timeout
  或：
  setex key timeout value
查看过期时间：

  ttl key
  如：
  ttl username
查看当前redis中的所有key：

  keys *
#列表操作：

在列表左边添加元素：

  lpush key value
将值value插入到列表key的表头。如果key不存在，一个空列表会被创建并执行lpush操作。当key存在但不是列表类型时，将返回一个错误。

在列表右边添加元素：

  rpush key value
将值value插入到列表key的表尾。如果key不存在，一个空列表会被创建并执行RPUSH操作。当key存在但不是列表类型时，返回一个错误。

查看列表中的元素：

  lrange key start stop
返回列表key中指定区间内的元素，区间以偏移量start和stop指定,如果要左边的第一个到最后的一个lrange key 0 -1。

移除列表中的元素：

移除并返回列表key的头元素：
  lpop key
移除并返回列表的尾元素：
rpop key
移除并返回列表key的中间元素：

  lrem key count value
将删除key这个列表中，count个值为value的元素。

指定返回第几个元素：

  lindex key index
将返回key这个列表中，索引为index的这个元素。

获取列表中的元素个数：

  llen key
  如：
  llen languages
删除指定的元素：

  lrem key count value
  如：
  lrem languages 0 php
根据参数 count 的值，移除列表中与参数 value 相等的元素。count的值可以是以下几种：

count > 0：从表头开始向表尾搜索，移除与value相等的元素，数量为count。
count < 0：从表尾开始向表头搜索，移除与 value相等的元素，数量为count的绝对值。
count = 0：移除表中所有与value 相等的值。
#set集合的操作：

添加元素：
  sadd set value1 value2....
  如：
  sadd team xiaotuo datuo
查看元素：
  smembers set
  如：
  smembers team
移除元素：
  srem set member...
  如：
  srem team xiaotuo datuo
查看集合中的元素个数：
  scard set
  如：
  scard team1
获取多个集合的交集：
  sinter set1 set2
  如：
  sinter team1 team2
获取多个集合的并集：
  sunion set1 set2
  如：
  sunion team1 team2
获取多个集合的差集：
sdiff set1 set2
如：
sdiff team1 team2

#hash哈希操作：

添加一个新值：

  hset key field value
  如：
  hset website baidu baidu.com
将哈希表key中的域field的值设为value。
如果key不存在，一个新的哈希表被创建并进行 HSET操作。如果域 field已经存在于哈希表中，旧值将被覆盖。

获取哈希中的field对应的值：

  hget key field
  如：
  hget website baidu
删除field中的某个field：

  hdel key field
  如：
  hdel website baidu
获取某个哈希中所有的field和value：

  hgetall key
  如：
  hgetall website
获取某个哈希中所有的field：

  hkeys key
  如：
  hkeys website
获取某个哈希中所有的值：

hvals key
如：
hvals website
判断哈希中是否存在某个field：

hexists key field
如：
hexists website baidu
获取哈希中总共的键值对：

hlen field
如：
hlen website

#事务操作：Redis事务可以一次执行多个命令，事务具有以下特征：

###隔离操作：事务中的所有命令都会序列化、按顺序地执行，不会被其他命令打扰。
###原子操作：事务中的命令要么全部被执行，要么全部都不执行。
###开启一个事务：

  multi
以后执行的所有命令，都在这个事务中执行的。

###执行事务：

  exec
###会将在multi和exec中的操作一并提交。

###取消事务：

  discard
会将multi后的所有命令取消。

###监视一个或者多个key：

  watch key...
监视一个(或多个)key，如果在事务执行之前这个(或这些) key被其他命令所改动，那么事务将被打断。

###取消所有key的监视：

  unwatch
#发布/订阅操作：

###给某个频道发布消息：
  publish channel message
###订阅某个频道的消息：
  subscribe channel