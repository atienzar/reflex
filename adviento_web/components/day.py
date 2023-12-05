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
                    padding_top=Size.MEDIUM.value
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
                    padding_top=Size.MEDIUM.value
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
                    # padding_top=Size.MEDIUM.value
                ),
                rx.span(
                    "Carrera",
                    padding_left=Size.SMALL.value
                ),
                rx.span(
                    "Navidad",
                    padding_left=Size.SMALL.value
                ),
                padding_top=Size.MEDIUM.value,
                position="absolute",
            ),
        ), 
        rx.cond(
            number == 22,
            rx.vstack(
                rx.box(
                    class_name="nes-icon is-large like",
                    alt="vacaciones",
                    padding_top=Size.MEDIUM.value
                ),

                rx.span(
                    "¡Vacas!",
                    padding_left=Size.SMALL.value
                ),
                position="absolute",
                padding_top=Size.MEDIUM.value,
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
                    "Cumple",
                    padding_left=Size.SMALL.value
                ),
                rx.span(
                    "JuanPi",
                    padding_left=Size.SMALL.value
                ),
                position="absolute",
                padding_top=Size.MEDIUM.value,
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
                padding_top=Size.MEDIUM.value,
                padding_right=Size.SMALL.value
            ),
        ),
        rx.cond(
            number == 31,
            rx.vstack(

                rx.hstack(
                    # rx.box(
                    #     class_name="nes-icon is-small star",
                    # ),
                    # rx.box(
                    #     class_name="nes-icon is-small star",
                    # ),
                ),
                rx.box(
                    class_name="nes-icon is-medium star",
                    alt="cumple JuanPi",
                ),
                rx.span(
                    "¡2024!",
                    padding_left=Size.SMALL.value
                ),
                position="absolute",
                padding_top=Size.MEDIUM.value,
            
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