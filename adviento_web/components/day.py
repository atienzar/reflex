import reflex as rx
from adviento_web.styles.styles import Size,TextColor,Color


def day(number:int, image:str = "gift.png", url: str = "")-> rx.Component:
    return rx.box(
        # rx.cond(
        #     number < 23:
        #     rx.link(
        #         rx.image(
        #             src=image,
        #             alt=f"Regalo asociado al dia {number}",
        #             href=url,
        #             is_external = True,
        #             html_height="32px"
        #         ),
        #         position="absolute",
        #     ),
        # ),
        rx.cond(
            number == 6,
            rx.vstack(
                rx.box(
                    class_name="snes-jp-logo",
                    alt="jugar",
                ),
                rx.span(
                    "Jugar VR!"
                ),
                position="absolute",
            ),
        ), 
        rx.cond(
            number == 7,
            rx.vstack(
                rx.box(
                    class_name="snes-jp-logo",
                    alt="jugar",
                ),
                rx.span(
                    "Jugar VR!"
                ),
                position="absolute",
            ),
        ), 
            rx.cond(
            number == 17,
            rx.vstack(
                rx.box(
                    class_name="nes-icon trophy is-large",
                    alt="carrera Navidad",
                ),
                rx.span(
                    "Carrera de"
                ),
                rx.span(
                    "Navidad"
                ),
                position="absolute",
            ),
        ), 
        rx.cond(
            number == 22,
            rx.vstack(
                rx.box(
                    class_name="nes-icon is-large like",
                    alt="vacaciones",
                ),

                rx.span(
                    "¡Vacas!",
                ),
                position="absolute",
            ),
        ),  
        rx.cond(
            number == 23,
            rx.vstack(
                rx.box(
                    class_name="nes-icon is-large star",
                    alt="cumple JuanPi",
                ),
                rx.span(
                    "Cumple de",
                    padding_right=Size.SMALL.value
                ),
                rx.span(
                    "JuanPi"
                ),
                position="absolute",
            ),
        ),     
        rx.cond(
            number == 24,
            rx.image(
                src=image,
                width="32",
                height="32",
                alt=f"Regalo asociado al dia {number}",
                position="absolute",
                html_height="32px",
            ),
        ),
        rx.text(
            number,
            padding=Size.SMALL.value,
            spacing=Size.VERY_BIG.value,
            float="right",
            position="relative"
        ),
        bg=Color.ACCENT.value,
        width="100%",
        aspect_ratio="1",
        position="relative",
    )