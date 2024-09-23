DARK_COLORS = [
	"#1d3557",
	"#043a3c",
	"#006d77",
	"#6247aa",
	"#b9375e",
	"#6d071a",
	"#7f5539",
	"#353535",
]

LIGHT_COLORS = [
	"#d1e2ef",
	"#bbd4d5",
	"#9ad1d4",
	"#ebd9fc",
	"#ffcbf2",
	"#f1cdcd",
	"#e6ccb2",
	"#e7ecef",
]

CONTENT_DARK_COLORS = [
	"#212529",
]

CONTENT_LIGHT_COLORS = [
	"#f8f9fa"
]

SCHEMES = [
    {
        "primary": DARK_COLORS,
        "secondary": DARK_COLORS,
        "third": DARK_COLORS,
        "dark": CONTENT_DARK_COLORS,
        "light": CONTENT_LIGHT_COLORS
    },
    {
        "primary": DARK_COLORS,
        "secondary": LIGHT_COLORS,
        "third": DARK_COLORS,
        "dark": CONTENT_DARK_COLORS,
        "light": CONTENT_LIGHT_COLORS
    },
    {
        "primary": LIGHT_COLORS,
        "secondary": DARK_COLORS,
        "third": DARK_COLORS,
        "dark": CONTENT_DARK_COLORS,
        "light": CONTENT_LIGHT_COLORS
    },
    {
        "primary": LIGHT_COLORS,
        "secondary": DARK_COLORS,
        "third": LIGHT_COLORS,
        "dark": CONTENT_DARK_COLORS,
        "light": CONTENT_LIGHT_COLORS
    },
    {
        "primary": DARK_COLORS,
        "secondary": DARK_COLORS,
        "third": DARK_COLORS,
        "dark": CONTENT_DARK_COLORS,
        "light": CONTENT_LIGHT_COLORS
    },
    {
        "primary": DARK_COLORS,
        "secondary": DARK_COLORS,
        "third": LIGHT_COLORS,
        "dark": CONTENT_DARK_COLORS,
        "light": CONTENT_LIGHT_COLORS
    }
]

TEMPLATES = [
    SCHEMES[0],
    SCHEMES[1],
    SCHEMES[2],
    SCHEMES[1],
    SCHEMES[3],
    SCHEMES[1],
    SCHEMES[4],
    SCHEMES[5],
]