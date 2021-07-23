

import os

# 设置一个环境变量

os.environ["xadmin_host"] = "http://49.235.92.12:8020"
# host = "http://49.235.92.12:8020"
host = os.environ["xadmin_host"]
print(host)