import reflex as rx
import adviento_web.constants as constants
import  adviento_web.styles.styles  as Styles
from adviento_web.components.header_text import header_text
from adviento_web.components.button import button
from adviento_web.components.day import day
from adviento_web.styles.styles import Size,Color,TextColor


def calendar()-> rx.Component:
    return rx.vstack(
        header_text(
            "Calendario de Navidad",
            "heart"
        ),
        rx.vstack(
            rx.hstack(
                rx.text("Los días que quedan para Navidad:"),
                rx.text(id="countdown" ),
                align_items="start",
            ),
            button(
                "Recordatorio",
                constants.DISCORD_URL
            ),
            rx.span(
                "Todo lo que pueda traer Papá Noel es una sorpresa, no tiene que ser todo lo que has pedido y lo mismo él añade sopresas que te gustarán."
            ),
            class_name="nes-container is-dark ",
            align_items="start",
            width="100%",
        ),
        rx.responsive_grid(
            rx.foreach(
                list(range(1,31)),
                lambda number:
                    day(
                        number
                    )
                ),
            columns=[3,3,4,5,6],
            spacing=Size.DEFAULT.value,
            width="100%",
            padding_y = Size.BIG.value
        ),
        rx.script(src="/js/countdown.js"),
        style=Styles.max_width_stye,
    )