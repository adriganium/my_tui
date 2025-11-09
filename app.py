""" Importing """
from textual.app import App , ComposeResult
from textual import events
from textual.getters import query_one
from textual.widgets import  Button, Static, Label

"""The App"""
class MyApp(App) :

    CSS = """
    #centertext {
            align: center middle;
    }
        
    #click1 {
        margin: 1 0;
        color: green;
    }
    
    #click2 {
        margin: 1 0;
        color: blue;
    }
    
    Label { 
        margin: 0 0;
        color: yellow;
    }
    """


    def on_mount(self) -> None:
        self.screen.styles.background =  "black"



    def compose(self) -> ComposeResult:
        yield  Label("Hello Textual")
        yield  Button("CLick hier !", id="click1")
        yield  Button("CLick NICHT hier !", id="click2")
        yield  Static("Was wirst du drücken????", id="centertext")


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



