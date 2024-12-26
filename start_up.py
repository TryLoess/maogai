import os
from pyngrok import ngrok

# 启动 Streamlit 应用
# 确保这里替换为你的 Streamlit 应用路径，例如 app.py
streamlit_script = r"E:\python\建模\web_try\app.py"  # 你的 Streamlit 主脚本
os.system(f"streamlit run {streamlit_script}")

