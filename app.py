import platform
import socket

from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h2("Hello, Posit Connect!"),
    ui.input_text("name", "Your name", value="World"),
    ui.output_text("greeting"),
    ui.hr(),
    ui.output_text("server_info"),
)


def server(input, output, session):
    @render.text
    def greeting():
        return f"Hello, {input.name()}!"

    @render.text
    def server_info():
        return f"Served by {socket.gethostname()} (Python {platform.python_version()})"


app = App(app_ui, server)
