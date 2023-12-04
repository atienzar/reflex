import reflex as rx
from adviento_web.styles.styles import Size,Color
from adviento_web.components.link_icons import link_icon
# from adviento_web.constants import constants

def navbar()-> rx.Component:
    return rx.vstack(
        rx.hstack(
            # rx.image(
            #     src="ip4b-logo.png",
            #     description="Imgane tux navideño",
            #     width=Size.VERY_BIG,
            #     height=Size.VERY_BIG
            # ),
            rx.box(
                class_name="nes-icon trophy is-small"
            ),
            rx.text("Navidad 2023"),
            rx.spacer(),
            link_icon(
                "twitter",
                "http://twitter.com/atienzar"
            ),
            link_icon(
                "facebook",
                "http://twitter.com/atienzar"
            ),
            width="100%"
        ),
        position="sticky",
        bg=Color.PRIMARY.value,
        border_bottom="0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )