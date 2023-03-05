from aiohttp import web


routes = web.RouteTableDef()

@routes.get('/')
async def test_api(request):
    return web.json_response({'rsp': 'success'})

async def web_server():
    app = web.Application()
    app.add_routes(routes)
    return app

if __name__ == '__main__':
    app = web_server()
    web.run_app(app)