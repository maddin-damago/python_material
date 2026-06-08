from typing import TypedDict


class Route(TypedDict):
    von: str
    nach: str
    distanz: int
    zugtyp: str
    abfahrt: str
    ankunft: str


routen: list[Route] = [
    {
        "von": "Montpellier",
        "nach": "Lyon",
        "distanz": 303,
        "zugtyp": "TGV",
        "abfahrt": "6:25",
        "ankunft": "8:24",
    },
    {
        "von": "Lyon",
        "nach": "Strasbourg",
        "distanz": 495,
        "zugtyp": "TGV",
        "abfahrt": "8:32",
        "ankunft": "12:24",
    },
    {
        "von": "Strasbourg",
        "nach": "Frankfurt (Main)",
        "distanz": 218,
        "zugtyp": "TGV",
        "abfahrt": "13:09",
        "ankunft": "14:56",
    },
    {
        "von": "Frankfurt (Main)",
        "nach": "Leipzig",
        "distanz": 400,
        "zugtyp": "ICE",
        "abfahrt": "15:19",
        "ankunft": "18:31",
    },
    {
        "von": "Leipzig",
        "nach": "Berlin Südkreuz",
        "distanz": 180,
        "zugtyp": "RE",
        "abfahrt": "18:51",
        "ankunft": "20:31",
    }
]
