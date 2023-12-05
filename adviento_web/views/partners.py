import reflex as rx
import adviento_web.constants as constants
import  adviento_web.styles.styles  as Styles
from adviento_web.components.header_text import header_text
from adviento_web.styles.styles import Size,Color


def partners()-> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_text(
                "Con la ayuda de Papá Noel", 
                "star",
                False
            ),
            rx.span(
                "PApá Noel nos va informando subre sus avances y sus apariciones en TV y redes sociales."
            ),
            rx.span(
                "¿Quieres apoyar esta iniciativa? Ponte en contacto conmigo por Twitter."
            ),
            # spacing=Size.BIG.value,
            padding_y=Size.VERY_BIG.value,
            style=Styles.max_width_stye
        ),        
        bg=Color.ACCENT.value,
        width="100%"

    )