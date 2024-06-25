import os
import tornado.ioloop
import tornado.web


class FileHandler(tornado.web.RequestHandler):
    async def get(self, filename):
        try:
            file_path = os.path.join("./files/", filename)
            with open(file_path, 'rb') as f:
                content = f.read()
            self.set_header("Content-Type", "application/octet-stream")
            self.write(content)
        except FileNotFoundError:
            self.set_status(404)
            self.write("File not found")


def make_app():
    return tornado.web.Application([
        (r"/files/(.*)", FileHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("Server listening on http://localhost:8000")
    tornado.ioloop.IOLoop.current().start()
