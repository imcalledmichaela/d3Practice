import asyncio
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from sse_starlette.sse import EventSourceResponse
import random

from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

async def homepage(request):
    template = "sse-client.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)

async def numbers(minimum, maximum):
    for i in range(minimum, maximum):
        await asyncio.sleep(0.9)
        yield dict(data=random.randint(minimum, maximum - 1))

async def sse(request):
    generator = numbers(1, 100)
    return EventSourceResponse(generator)

routes = [
    Route("/", endpoint=homepage),
    Route("/stream", endpoint=sse)
]

app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level='info')