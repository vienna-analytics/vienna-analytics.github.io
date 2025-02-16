import reflex as rx


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.text("Vienna Analytics", font_family="IBM Plex Sans"),
                rx.text(
                    "Deploying AI is the most impactful action a company can take. A paradigm shift in business. A new renaissance. Vienna Analytics is dedicated to engineering and deploying AI systems that future-proof enterprises.",
                    font_family="IBM Plex Sans",
                ),
                align_items="center",
                justify_content="center",
            ),
            width="50%",
            align_items="center",
            justify_content="center",
            padding_top="100px",
        ),
        height="100vh",
        background="#000000",
        align_items="center",
        justify_content="center",
    )


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,100..700;1,100..700&display=swap"
    ],
    theme=rx.theme(
        appearance="dark",
        has_background=False,
        accent_color="gray",
        gray_color="slate",
        radius="medium",
    ),
)
app.add_page(index)


"""
rx.text(
    "Deploying AI is the most impactful action a company can take. A paradigm shift in business. A new renaissance. Vienna Analytics is dedicated to engineering and deploying AI systems that future-proof enterprises.",
    color="white",
    font_family="IBM Plex Sans",
),
# Second paragraph
rx.text(
    "Specializing in automating business processes, our aim is to eradicate inefficiency, enhance productivity, and significantly reduce operational cost. We also provide strategic consultancy to help businesses leverage AI to gain an edge on the competition.",
    color="white",
    font_family="IBM Plex Sans",
),
# Third paragraph
rx.text(
    "We offer one-time system builds, or a subscription allowing us to partner in building out systems for your entire operation. All our prices are calculated using productivity growth. This means that you pay a fee based on the amount of productivity growth that we provide your company.",
    color="white",
    font_family="IBM Plex Sans",
),
"""
