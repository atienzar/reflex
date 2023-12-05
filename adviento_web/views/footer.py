import reflex as rx
import adviento_web.styles.styles as Styles
from adviento_web.styles.styles import Size, TextColor


def footer()-> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Ccalendario de 2023",
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.ZERO.value,

            ),
            rx.link(
                "Creado con ",
                rx.box(class_name="nes-icon is-small heart"),
                " para Pablo",
                is_external=True,
                margin_top=Size.ZERO.value,
                font_size=Size.MEDIUM.value,
                color=TextColor.TERCIARY.value,
                
            ),
            align_items="start",
            spacing="0.8em"
        ),
        rx.spacer(),
        # rx.image(
        #     src="favicon.ico",
        #     alt="Logotipo BNT",
        #     class_name=""
        # ),
        rx.box(
            class_name="nes-charmander is-small"
            
        ),
        padding_bottom=Size.BIG.value,
        style=Styles.footer_width_stye,
        
    )
