# Redis数据库的地址和端口
HOST = 'localhost'
PORT = 6379

# 如果Redis有密码，则添加这句密码，否则设置为None或''
PASSWORD = ''

# 获得代理测试时间界限
get_proxy_timeout = 9

# 代理池数量界限
POOL_LOWER_THRESHOLD = 100
POOL_UPPER_THRESHOLD = 1000

# 检查周期
<<<<<<< HEAD
# VALID_CHECK_CYCLE = 60
# POOL_LEN_CHECK_CYCLE = 20
=======
>>>>>>> 864c253a27f57eb3640978d9606349bba4a2fb89
VALID_CHECK_CYCLE = 3600
POOL_LEN_CHECK_CYCLE = 20

# 测试API，用百度来测试
<<<<<<< HEAD
# TEST_API='http://www.baidu.com'
# TEST_API='http://www.sogou.com'
TEST_API='http://weixin.sogou.com/'
=======
TEST_API='http://www.baidu.com'
# TEST_API='http://www.sogou.com'
>>>>>>> 864c253a27f57eb3640978d9606349bba4a2fb89