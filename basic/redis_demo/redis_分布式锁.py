#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/13 23:54
# @Author : Tom_tao
# @Site : 
# @File : redis_分布式锁.py
# @Software: PyCharm


# 分布式锁是控制分布式系统之间的同步访问共享资源的一种方式。对于分布式的目标 必须明确以下三点：
# 1.任何时间点必须只能够有一个客户端拥有锁
# 2.不能够有死锁 即最终客户端都能够获得锁，尽管可能会经历失败
# 3.错误容忍性要好  只要有大部分的redis实例存活  客户端就应该能获得锁
# 分布式锁的条件：
# 1.互斥性 在不同节点上的不同线程的互斥
# 2.可重入性 同一个节点上的同一个线程如果获取了锁之后，能够再次获取这个锁
# 3.高可用 加锁和解锁需要高效  包中高可用 防止分布式锁失效，可以增加降级
# 4.支持阻塞和非阻塞  实现超时获取失败  tryLock(long timeout)支持公平锁和非公平锁


# 1、选用Redis实现分布式锁原因：
# （1）Redis有很高的性能；
# （2）Redis命令对此支持较好，实现起来比较方便
# 2、使用命令介绍：
# （1）SETNX
# SETNX key val：当且仅当key不存在时，set一个key为val的字符串，返回1；若key存在，则什么都不做，返回0。
# （2）expire
# expire key timeout：为key设置一个超时时间，单位为second，超过这个时间锁会自动释放，避免死锁。
# （3）delete
# delete key：删除key
# 在使用Redis实现分布式锁的时候，主要就会使用到这三个命令。
# 3、实现思想：
# （1）获取锁的时候，使用setnx加锁，并使用expire命令为锁添加一个超时时间，超过该时间则自动释放锁，锁的value值为一个随机生成的UUID，通过此在释放锁的时候进行判断。
# （2）获取锁的时候还设置一个获取的超时时间，若超过这个时间则放弃获取锁。
# （3）释放锁的时候，通过UUID判断是不是该锁，若是该锁，则执行delete进行锁释放。

# 代码实例：
#连接redis
import time
import uuid
from threading import Thread

import redis

redis_client = redis.Redis(host="localhost",
                           port=6379,
                           # password=123,
                           db=10)

#获取一个锁
# lock_name：锁定名称
# acquire_time: 客户端等待获取锁的时间
# time_out: 锁的超时时间
def acquire_lock(lock_name, acquire_time=10, time_out=10):
    """获取一个分布式锁"""
    identifier = str(uuid.uuid4())
    end = time.time() + acquire_time
    lock = "string:lock:" + lock_name
    while time.time() < end:
        if redis_client.setnx(lock, identifier):
            # 给锁设置超时时间, 防止进程崩溃导致其他进程无法获取锁
            redis_client.expire(lock, time_out)
            return identifier
        elif not redis_client.ttl(lock):
            redis_client.expire(lock, time_out)
        time.sleep(0.001)
    return False

#释放一个锁
def release_lock(lock_name, identifier):
    """通用的锁释放函数"""
    lock = "string:lock:" + lock_name
    pip = redis_client.pipeline(True)
    while True:
        try:
            pip.watch(lock)
            lock_value = redis_client.get(lock)
            if not lock_value:
                return True

            if lock_value.decode() == identifier:
                pip.multi()
                pip.delete(lock)
                pip.execute()
                return True
            pip.unwatch()
            break
        except redis.excetions.WacthcError:
            pass
    return False


# 例子中使用50个线程模拟秒杀10张票，使用–运算符来实现商品减少，从结果有序性就可以看出是否为加锁状态。
count=10

def seckill(i):
    identifier=acquire_lock('resource')
    print("线程:{}--获得了锁".format(i))
    time.sleep(1)
    global count
    if count<1:
        print("线程:{}--没抢到，票抢完了".format(i))
        return
    count-=1
    print("线程:{}--抢到一张票，还剩{}张票".format(i,count))
    release_lock('resource',identifier)


for i in range(50):
    t = Thread(target=seckill,args=(i,))
    t.start()

"""
使用过Redis分布式锁么，它是怎么实现的？
    先拿setnx来争抢锁，抢到之后，再用expire给锁加一个过期时间防止锁忘记了释放。
如果在setnx之后执行expire之前进程意外crash或者要重启维护了，那会怎么样？
    set指令有非常复杂的参数，这个应该是可以同时把setnx和expire合成一条指令来用的！
使用过Redis做异步队列么，你是怎么用的？有什么缺点？
    一般使用list结构作为队列，rpush生产消息，lpop消费消息。当lpop没有消息的时候，要适当sleep一会再重试。
缺点：
    在消费者下线的情况下，生产的消息会丢失，得使用专业的消息队列如rabbitmq等。
能不能生产一次消费多次呢？
    使用pub/sub主题订阅者模式，可以实现1:N的消息队列。

什么是缓存穿透？如何避免？什么是缓存雪崩？何如避免？
缓存穿透
    一般的缓存系统，都是按照key去缓存查询，如果不存在对应的value，就应该去后端系统查找（比如DB）。一些恶意的请求会故意查询不存在的key,请求量很大，就会对后端系统造成很大的压力。这就叫做缓存穿透。

如何避免？
    1：对查询结果为空的情况也进行缓存，缓存时间设置短一点，或者该key对应的数据insert了之后清理缓存。
    2：对一定不存在的key进行过滤。可以把所有的可能存在的key放到一个大的Bitmap中，查询时通过该bitmap过滤。

缓存雪崩
    当缓存服务器重启或者大量缓存集中在某一个时间段失效，这样在失效的时候，会给后端系统带来很大压力。导致系统崩溃。
如何避免？
    1：在缓存失效后，通过加锁或者队列来控制读数据库写缓存的线程数量。比如对某个key只允许一个线程查询数据和写缓存，其他线程等待。
    2：做二级缓存，A1为原始缓存，A2为拷贝缓存，A1失效时，可以访问A2，A1缓存失效时间设置为短期，A2设置为长期
    3：不同的key，设置不同的过期时间，让缓存失效的时间点尽量均匀。
"""