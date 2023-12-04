import reflex as rx
import adviento_web.constants as constants
import  adviento_web.styles.styles  as Styles
from adviento_web.components.header_text import header_text
from adviento_web.components.button import button
from adviento_web.styles.styles import Size,Color,TextColor


def author()-> rx.Component:
    return rx.vstack(
        header_text(
            "like",
            "Hola, mi nombre es Rosa Atienza"
        ),
        rx.hstack(
            rx.avatar(
                name="atienzar",
                size="2xl",
                class_name="nes-icon coin is-large",
                bg=Color.PRIMARY.value,
                padding="2px",
                border="4px",
                border_color=Color.SECONDARY.value
            ),
            rx.vstack(
                rx.span(),
                rx.span(),
                author_buttons,
                width="100%",
                align_items="start"
            ),
            align_items="start",
            spacing="2em"
        ),
        style=Styles.max_width_stye
    )


def author_buttons() -> rx.Component:
    rx.box(
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
