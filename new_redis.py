import redis


class Base(object):
	def __init__(self):
		self.r = redis.StrictRedis(host="localhost", port=6379, db=0)


class TestString(object):
	"""
	set -- 设置值
	get -- 获取值
	mset -- 设置多个键值对
	mget -- 获取多个键值对
	append -- 添加字符串
	del -- 删除
	incr/decr -- 增加/减少
	"""
	def __init__(self):
		self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

	def test_set(self,key,value):
		res = self.r.set(key, value)
		print(res)
		return res

	def test_get(self):
		res = self.r.get('user2')
		print(res)
		return res

	def test_mset(self):
		d = {
			'user3': 'aaaa',
			'user4': 'nnnnn'
		}
		res = self.r.mset(d)
		print(res)
		return res

	def test_mget(self, *keys):	
		res = self.r.mget(*keys)
		print(res)
		return res

	def test_del(self):
		res = self.r.delete('user4')
		print(res)
		return res

	def test_append(self):
		res = self.r.append('user3', 'bbb')
		print(res)
		return res

	def test_incr(self):
		res = self.r.incr('user2')
		print(res)
		return res

	def test_decr(self):
		res = self.r.decr('user1')
		print(res)
		return res


class TestList(object):
	"""
	lpush/rpush -- 从左/右插入数据
	lrange -- 获取指定长度的数据
	ltrim -- 截取一定长度的数据
	lpop/rpop -- 移除最左/右的元素并返回
	lpushx/rpushx -- key存在的时候才插入数据，不存在的时候不做任何处理
	"""
	def __init__(self):
		self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

	def test_lpush(self, key, *values):
		res = self.r.lpush(key, *values)
		print(res)
		return self.r.lrange(key, 0, -1)

	def test_rpush(self, key, *values):
		res = self.r.rpush(key, *values)
		print(res)
		return self.r.lrange(key, 0, -1)

	def test_lrange(self,key,start,end):
		res = self.r.lrange(key, start, end)
		print(res)
		return res

	def test_lpop(self, key):
		res = self.r.lpop(key)
		print(res)
		return self.r.lrange(key, 0, -1)

	def test_rpop(self, key):
		res = self.r.rpop(key)
		print(res)
		return self.r.lrange(key, 0, -1)


class TestSet(Base):
	"""
	sadd/srem -- 添加/删除元素
	sismember -- 判断是否为set的一个元素
	smembers -- 返回该集合的所有元素
	sdiff -- 返回一个集合与其他集合的差集
	sinter -- 返回几个集合的交集
	sunion -- 返回几个集合的并集
	"""
	def test_sadd(self, key, *values):
		res = self.r.sadd(key, *values)
		print(res)
		return self.r.smembers(key)

	def test_srem(self, key, *values):
		res = self.r.srem(key, *values)
		print(res)
		return self.r.smembers(key)

	def test_sismember(self, key, value):
		res = self.r.sismember(key, value)
		print(res)

	def test_sdiff(self, key, *keys):
		res = self.r.sdiff(key, *keys)
		print(res)
		return res

	def test_sinter(self, key, *keys):
		res = self.r.sinter(key, *keys)
		print(res)
		return res

	def test_sunion(self, key, *keys):
		res = self.r.sunion(key, *keys)
		print(res)
		return res


class TestHash(Base):
	"""
	hset/hget -- 设置/获取散列值
	hmset/hmget -- 设置/获取多对散列值
	hsetnx -- 如果三列已经纯在，则不设置
	hkeys/hvals -- 返回所有的keys/values
	hlen -- 返回散列包含域（field）的数量
	hdel -- 删除散列指定的域（field）
	hexists -- 判断是否存在
	"""
	def test_hset(self,name,key,value):
		res = self.r.hset(name,key,value)
		print(res)
		return self.r.hvals(name)

	def test_hget(self,name,key):
		res = self.r.hget(name, key)
		print(res)
		return res

	def test_hmset(self, name, dict1):
		res = self.r.hmset(name, dict1)
		print(res)
		return self.r.hvals(name)

	def test_hmget(self, name, *keys):
		res = self.r.hmget(name, *keys)
		print(res)
		return res

	def test_hkeys(self, name):
		res = self.r.hkeys(name)
		print(res)
		return res

	def test_hvals(self, name):
		res = self.r.hvals(name)
		print(res)
		return res

	def test_hlen(self, name):
		res = self.r.hlen(name)
		print(res)
		return res

	def test_hdel(self, name, *keys):
		res = self.r.hdel(name, *keys)
		print(res)
		return self.r.hkeys(name)

	def test_hexists(self, name, key):
		res = self.r.hexists(name, key)
		print(res)
		return res




def main():
	# -- 以下为str操作对象 --
	# str_obj = TestString()
	# l = ['user1', 'user2', 'user3', 'user4']
	# str_obj.test_set('user4', '30')
	# str_obj.test_get()
	# str_obj.test_mset()
	# str_obj.test_mget(l)
	# str_obj.test_del()
	# str_obj.test_append()
	# str_obj.test_incr()
	# str_obj.test_decr()

	# -- 以下为list操作对象 --
	# list_obj = TestList()
	# li = ('aaa', 'bbb', 'ccc', 'ddd')
	# list_obj.test_lpush('user5', *li)
	# list_obj.test_rpush('user6', *li)
	# list_obj.test_lrange('user5', 1, 4)
	# list_obj.test_lpop()
	# list_obj.test_rpop('user5')
	
	# -- 以下为set操作对象 --
	# li = {'aaa', 'bbb', 'ccc', 'ddd'}
	# li_rem = {'aaa', 'ccc'}
	# set_obj = TestSet()
	# set_obj.test_sadd('user9', *li)
	# set_obj.test_srem('user7', *li_rem)
	# set_obj.test_sismember('user7', 'aaa')
	# set_obj.test_sdiff('user9', 'user8', 'user7')
	# set_obj.test_sinter('user9', 'user8', 'user7')
	# set_obj.test_sunion('user9', 'user8', 'user7')

	# -- 以下为hash操作对象 --
	hash_obj = TestHash()
	# hash_obj.test_hset('hash1', 'name', 'sunsc')
	# hash_obj.test_hget('hash1', 'name')
	# dict1 = {
	# 'name': 'sunshuchang',
	# 'age': 28,
	# 'sex': 'man'
	# }
	# hash_obj.test_hmset('hash2', dict1)
	# keys = ['name', 'age', 'sex']
	# hash_obj.test_hmget('hash2', *keys)
	# hash_obj.test_hkeys('hash2')
	# hash_obj.test_hvals('hash2')
	# hash_obj.test_hlen('hash2')
	# hash_obj.test_hdel('hash2', 'name', 'sex')
	hash_obj.test_hexists('hash2', 'age')




if __name__ == '__main__':
	main()