#存放配置

from  pathlib  import Path
from common.utils import load_cases

BASE_URL = "http://127.0.0.1:5000"
PROJECT_ROOT = Path(__file__).parent.parent          # 项目根目录的绝对路径 __file__ 是"当前这个文件的路径"，Path(__file__).parent 是"它所在的目录"。
CASES = load_cases(PROJECT_ROOT / "test_data" / "create_todo_validation.yml")       #PROJECT_ROOT / "test_data" / "文件名" 是 pathlib 的路径拼接写法（用 / 拼，比字符串相加干净）。
