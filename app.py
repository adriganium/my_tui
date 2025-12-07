""" Importing """
from textual.app import App , ComposeResult , Screen
from textual import events
from textual.containers import Container
from textual.widgets import  Button, Label
import psutil

"""The App"""
class MyApp(App) :

    """CSS Pfad"""
    CSS_PATH = "stylish.css"

    def compose(self) -> ComposeResult:

        with Container():
            yield Label("Was wirst du drücken????", id="label2")
            yield Button("Click hier !", id="click1")
            yield Button("Click NICHT hier !", id="click2")
            yield Label("Q um zu beenden", id="label1")

    def on_mount(self):
        self.set_interval(1.0, self.batch_update )
    

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


# fetching and displaying of system processes with putil
# ask for user input , and give the user the ability to write in a promt box to start fetures
# implement 