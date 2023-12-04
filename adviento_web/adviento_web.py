import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.styles.styles import Size
from adviento_web.views.navbar import navbar
from adviento_web.views.header import header
from adviento_web.views.footer import footer
from adviento_web.views.author import author
from adviento_web.views.instructions import instructions

def index()-> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                instructions(),
                author(),
                footer(),
                width="100%",
                spacing="4em"
            )
        ) 
    )


app = rx.App(
    # Con esto ya cargamos las 2 hojas de estulo que hemos definido.
    stylesheets=styles.STYLESHEET,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title="Calendario de adviento 2023 | 24 dias. 24 regalos" ,
    description="Cada dia un regalo diferente"
    
)

app.compile()
