import memcache

# 连接到Memcached服务器
client = memcache.Client(['127.0.0.1:11211'])

# 设置键值对到Memcached
client.set('key1', 'value1 66666666')
client.set('key2', 'value2 88888888')

# 从Memcached获取值
value1 = client.get('key1')
value2 = client.get('key2')

print(f'Value for key1: {value1}')
print(f'Value for key2: {value2}')