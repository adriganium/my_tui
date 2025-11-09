""" Importing """
from textual.app import App , ComposeResult
from textual import events
from textual.containers import Container
from textual.widgets import  Button, Static, Label

"""The App"""
class MyApp(App) :

    CSS_PATH = "stylish.css"


    def on_mount(self) -> None:
        self.screen.styles.background =  "black"



    def compose(self) -> ComposeResult:
        yield  Label("Hello Textual", id="label1")
        yield  Button("Click hier !", id="click1")
        yield  Button("Click NICHT hier !", id="click2")
        #with Container():
        #    yield  Label("Was wirst du drücken????", id="label2")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "click1":
            self.query_one(Label).update("Du hast gecklicked")
            event.button.styles.background = "red"

        if event.button.id == "click2":
            self.exit()


    def _on_key(self, event: events.Key) -> None:
        if event.key == "q":
            self.exit()

if __name__ == "__main__":
    app = MyApp()
    app.run()



