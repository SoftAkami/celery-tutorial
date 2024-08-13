
import falcon

class Counter:
    def on_post():
        ...



app = falcon.App()
app.add_route("/worker", Counter())