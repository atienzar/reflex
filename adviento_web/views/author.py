import reflex as rx
import adviento_web.constants as constants
import  adviento_web.styles.styles  as Styles
from adviento_web.components.header_text import header_text
from adviento_web.components.button import button
from adviento_web.styles.styles import Size,Color,TextColor


def author()-> rx.Component:
    return rx.vstack(
        header_text(
            "Hola, mi nombre es Rosa Atienza",
            "like",

        ),
        rx.hstack(
            
            # rx.box(
            #     name="atienzar",
            #     class_name="nes-icon coin is-large",
            #     bg=Color.PRIMARY.value,
            #     pading="2px",
            #     border="4px",
            #     border_color=Color.SECONDARY.value
            # ),
            rx.avatar(
                name="Rosa Atienza",
                size="2xl",
                font_size=Size.SMALL.value,
                bg=Color.PRIMARY.value,
                text_color = TextColor.PRIMARY.value,
                padding="2px",
                border="4px",
                border_color=Color.SECONDARY.value,
                margin_right=Size.DEFAULT.value,
                margin_bottom=Size.DEFAULT.value
            ),
            rx.vstack(
                rx.span('Me gusta probar cosas nuevas y por eso estoy probando con Reflex.'),
                rx.span("Con este framework podemos hacer web con Python de forma muy sencilla."),
                # rx.mobile_only(
                #     rx.vstack(
                #         author_buttons(),
                #     ),
                # ),
                # rx.tablet_and_desktop(
                #     rx.hstack(
                #         author_buttons(),
                #     ),
                # )
                author_buttons(),
                width="100%",
                align_items="start"
            ),
            align_items="start",
            spacing=Size.BIG.value,
            flex_direction=["column", "column", "column", "row", "row"]
        ),
        style=Styles.max_width_stye
    )


def author_buttons() -> rx.Component:
    return rx.box(
        button(
            "YouTube",
            constants.YOUTUBE_URL
        ),
        button(
            "Discord",
            constants.DISCORD_URL
        ),
        button(
            "Twitch",
            constants.TWITCH_URL
        ),
    )
