#请求层
import logging
import requests
from common.config import BASE_URL

logger = logging.getLogger(__name__)        #给当前模块创建一个以模块名为名字的日志记录器，后续用 logger.info() 等方法记日志，既方便定位来源，又能灵活控制日志级别和输出。

TIMEOUT = 10        # 超时秒数

def _send(method, path, **kwargs):
    url = f"{BASE_URL}{path}"
    logger.debug(f"→ {method} {url}")                        # 发出去之前，记一笔
    resp = requests.request(method, url, timeout=TIMEOUT, **kwargs)
    logger.debug(f"← {resp.status_code} {resp.text}")        # 回来后，记一笔
    return resp

def get(path, **kwargs):    return _send("GET", path, **kwargs)
def post(path, **kwargs):   return _send("POST", path, **kwargs)
def put(path, **kwargs):    return _send("PUT", path, **kwargs)
def delete(path, **kwargs): return _send("DELETE", path, **kwargs)
