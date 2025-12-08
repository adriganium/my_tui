import ipaddress

from textual.app import App , ComposeResult , Screen
from textual import events
from textual.containers import Container, Horizontal, Vertical, Grid
from textual.widgets import Button, Label, Header, Rule, Static, ListItem, ListView
import psutil

class MyApp(App) :

    #CSS Path
    CSS_PATH = "stylish.css"

    # Enableing the on_startup
    ENABLE_STARTUP = True

    def compose(self) -> ComposeResult:

        # Static System Information
        cpu_threads = psutil.cpu_count()
        cpu_thread_count = str(cpu_threads)
        pc_memory = psutil.virtual_memory()
        pc_mem_total = str(int(pc_memory.total / pow(2, 20)))
        pc_mem_available = str(int(pc_memory.available / pow(2, 20)))
        recieved_bits = psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv
        bekommene_bits = str(int(recieved_bits / pow(2, 20)))
        sending_bits = psutil.net_io_counters(pernic=False, nowrap=True).bytes_sent
        gesandte_bits = str(int(sending_bits / pow(2, 20)))
        ip_addr = psutil.net_connections(kind="inet4")
        ipv4addr = ip_addr[0].laddr[0]


        #Creating lines
        with Vertical():
            # Creating Header
            yield Header(id="header1", icon="(-_-)", show_clock=True)
            #vertical Line
            #yield Rule(id="rule2", line_style="thick", orientation="horizontal")
            # Creating all the Container things
            with Grid():
                yield Label(f"CPU Thread Count: {cpu_thread_count}", id="stat1", classes="static_value")
                yield Label(f"Total System RAM : {pc_mem_total} MB", id="stat2", classes="static_value")
                yield Label(f"Total Avaliable RAM : {pc_mem_available} MB", id="stat3", classes="variable_value")
                yield Label(f"Total recieved MB: {bekommene_bits} MB ", id="stat4", classes="variable_value")
                yield Label(f"Total sent MB: {gesandte_bits} MB", id="stat5", classes="variable_value")
                yield Label(f"IPV4 Adress: {ipv4addr}", id="stat6", classes="variable_value")

    def on_mount(self) -> None:
        # Screen stuff
        self.screen.styles.border = ("heavy", "orange")

        # Header Configuration
        self.title = "System Information"

        # Auto update every second
        self.set_interval(1.0, self.update_ram)

    def update_ram(self):
        ram_widget = self.query_one("#stat3", Static)
        available = int(psutil.virtual_memory().available / (1024 ** 2))

        recieved_widget = self.query_one("#stat4", Static)
        bits_bekommen = int(psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv  / pow(2, 20))

        sent_widget = self.query_one("#stat5", Static)
        bist_gesendet = int(psutil.net_io_counters(pernic=False, nowrap=True).bytes_sent / pow (2, 20))

        ip_addr_widget = self.query_one("#stat6", Static)
        adressen_dings = psutil.net_connections(kind="inet4")
        ipv4addresse = adressen_dings[0].laddr[0]


        ram_widget.update(f"Total Available RAM: {available} MB")
        recieved_widget.update(f"Total recieved Data: {bits_bekommen} MB ")
        sent_widget.update(f"Total sent Data: {bist_gesendet} MB ")
        ip_addr_widget.update(f"IPV4 Adress: {ipv4addresse}")

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


# implementing that there are also time dependent values like
# for example data recieved per socond and such
