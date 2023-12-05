import reflex as rx
from adviento_web.styles.styles import Size,TextColor


def header_text(text:str, icon:str, dark=True)-> rx.Component:
    return rx.hstack(
        rx.box(
            class_name=f"nes-icon is-medium {icon}"
        ),
        rx.heading(
            text,
            size="md",
            color=TextColor.ACCENT.value if dark else TextColor.SECONDARY.value
        ),
        spacing = Size.DEFAULT.value,
        padding_button=Size.BUTTON.value
    )