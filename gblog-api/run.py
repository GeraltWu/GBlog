import os
import uvicorn

# 获取端口配置，如果没有设置则默认为8000
app_port = 8081

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=app_port, reload=True)