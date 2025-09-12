from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route
import requests
import uvicorn

# 虎扑首页 URL
HUPU_URL = 'https://www.hupu.com/'


# 定义异步函数来获取虎扑首页 HTML
async def get_hupu():
    try:
        params = {
            'c': 'a',
            'encode': 'json'
        }
        response = requests.get(HUPU_URL, params=params)
        status_code = response.status_code
        if status_code == 200:
            # 返回完整 HTML 内容
            return {'html': response.text}
        else:
            return {'error': f'请求虎扑失败，状态码: {status_code}'}
    except requests.RequestException as e:
        return {'error': f'请求过程中出现错误: {str(e)}'}


# 定义处理根路径请求的异步函数
async def homepage(request):
    result = await get_hupu()
    # 如果有错误，就返回 JSON
    if "error" in result:
        return JSONResponse(result)
    # 否则返回 HTML
    return PlainTextResponse(result["html"], media_type="text/html")


# 创建 Starlette 应用实例
app = Starlette(
    debug=True,
    routes=[
        Route('/', homepage),
    ]
)

if __name__ == "__main__":
    # 使用 uvicorn 运行应用
    uvicorn.run(app, host='0.0.0.0', port=8000)
