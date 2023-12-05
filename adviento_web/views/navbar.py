import reflex as rx
import adviento_web.constants as constants
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
            # rx.box(
            #     class_name="nes-icon trophy is-small"
            # ),
            rx.link(
                "#Navidad2023",
                href=constants.ADVIENTO_HASHTAG_URL,
                is_external=True,
            ),
            rx.spacer(),
            rx.tablet_and_desktop(
                link_icon(
                    "twitch",
                    constants.TWITCH_URL
                ),
            ),
            link_icon(
                "twitter",
                constants.TWITTER_URL_PABLO
            ),
            # link_icon(
            #     "twitch",
            #     constants.TWITCH_URL
            # ),
            link_icon(
                "github",
                constants.GITHUB_URL
            ),
            width="100%"
        ),
        position="sticky",
        bg=Color.PRIMARY.value,
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )