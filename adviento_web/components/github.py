import reflex as rx
import adviento_web.constants as constants
from adviento_web.styles.styles import Size,TextColor,Color


def github()-> rx.Component:
    return rx.link(
        rx.vstack(
            rx.vstack(

                rx.span(
                    "Proyecto"
                ),
                rx.span(
                    "en Github"
                ),
                align_items="start",
                class_name="nes-balloon from-right is-dark",
                margin_bottom=Size.BIG.value
            ),
            rx.box(
                rx.span(
                    constants.VERSION,
                    class_name="is-error",
                ),
                class_name="nes-badge",
            ),

        ),
        rx.box(
            class_name="nes-octocat animate"
        ),
        href=constants.GITHUB_REPO,
        is_external=True,
        margin_top=Size.ZERO.value,
        align_items="end",
        display="flex"
    )