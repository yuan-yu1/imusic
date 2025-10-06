import os, webbrowser, threading, time
from app import create_app

app = create_app()

# 等服务器启动完成后再打开浏览器
def open_browser():
    time.sleep(1.5)          # 确保服务已就绪
    url = 'http://localhost:5000/static/player.html'
    webbrowser.open_new_tab(url)

if __name__ == '__main__':
    threading.Thread(target=open_browser, daemon=True).start()
    app.run(debug=False)     # 用 False 避免双开浏览器