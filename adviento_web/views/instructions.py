import reflex as rx
import adviento_web.styles.styles as Style
import adviento_web.constants as constants
from adviento_web.styles.styles import Size, TextColor
from adviento_web.components.button import button

def instructions()-> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "¿Cómo funciona el calendario?",
                class_name="title",
                color=TextColor.ACCENT.value
            ),
            rx.span("* Cada día iremos actualizando el número de días que quedan para que venga Papá Noel."),
            rx.span("* Te dejamos esta selección de villancicos para que vayas poniendole música a la Navidad."),
            button(
                "Villancicos",
                constants.YOUTUBE_URL2

            ),
            rx.span("* Puedes ir viendo como va viajando Papá Noel si pinchas en el hashtag"),
            button(
                "Twitter",
                constants.TWITTER_URL
            ),
            class_name="nes-container is-dark with-title",
            align_items="start",
            width="100%",
            
        ),
        style=Style.max_width_stye
    )           
