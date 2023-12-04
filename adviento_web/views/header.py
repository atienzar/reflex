import reflex as rx
import adviento_web.styles.styles as Style
from adviento_web.styles.styles import Size, TextColor


def header()-> rx.Component:
    return rx.vstack(
        rx.heading(
            "Calendario de Navidad 2023",
            size="lg",
            padding_bottom=Size.DEFAULT.value
        ),
        rx.flex(
            rx.box(
                class_name="nes-mario",
                margin_right=Size.VERY_BIG.value
            ),
            # rx.image(
            #     src="BNT.png",
            #     alt="Logo de bnt en la version academy",
            #     width="16em",
            #     height="8em",
            #     margin_right=Size.BIG.value
            # ),
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.text("24 Dias 24 Regalos"),
                        rx.text("Del 1 al 24 de Diciembre"),
                        class_name="nes-balloon from-right is-dark"
                    ),
                    rx.box(
                        class_name="nes-kirby"

                    ),
                ),
                rx.span(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer id dui eu arcu egestas porttitor a in leo.",
                    rx.span(
                        "comunidad bnt",
                        color=TextColor.ACCENT.value,
                        font_size=Size.MEDIUM.value
                    )
                ),
                rx.span(
                    "Proin nisi enim, volutpat ut dui et, venenatis blandit lectus. Etiam ultrices leo quis urna commodo. Cras dictum eros quis lorem imperdiet ultrices. "
                ),
                rx.span("Una actividad navideña y muy guay"),
                rx.link(
                    "#navidad2023",
                    href="http://twitter.com/#navidad2023",
                    is_external=True,
                    color=TextColor.PRIMARY.value,
                    padding_size=Size.VERY_BIG.value,
                    font_size=Size.DEFAULT.value,
                    margin_top=Size.BIG.value,
                ),
                align_items="start",
            ),
            flex_directions=("column", "column","column", "row", "row")
        ),
        padding_top = Size.BIG.value,
        style=Style.max_width_stye
    )
