import reflex as rx
from adviento_web.styles.styles import Size


def header_text(text:str, icon:str)-> rx.Component:
    return rx.hstack(
        rx.box(
            class_name=f"nes-icon is-medium {icon}"
        ),
        rx.heading(
            text,
            size="md"
        ),
        spacing = Size.DEFAULT.value,
        padding_button=Size.BUTTON.value
    )