"""
= Aufgabe 4: Bahnticket =

Ein Reise wird geplant -- von Montpellier nach Berlin Südkreuz

Montpellier -> Lyon: 303km TGV
Lyon -> Strasbourg: 495km TGV
Strasbourg -> Frankfurt (Main): 218km TGV
Frankfurt (Main) -> Leipzig: 400km ICE
Leipzig -> Berlin Südkreuz: 180km RE

Preis: EUR 0.25 pro km
Ermäßigung BC50 50% in Deutschland
Interrail 4 Tage/Monat: EUR 283 (https://interrail.eu)
Reise: 800km pro Tag

* Ziel: Empfehlung ausgeben, welches Ticket am besten passt
* wieviele Tage ist der Reisende unterwegs
"""

strecken = [
    {"strecke": "montpellier-lyon", "laenge_in_km": 303, "zugbezeichnung": "TGV"},
    {"strecke": "lyon-strasbourg", "laenge_in_km": 495, "zugbezeichnung": "TGV"},
    {"strecke": "strasbourg-ffm", "laenge_in_km": 218, "zugbezeichnung": "TGV"},
    {"strecke": "ffm-leipzig", "laenge_in_km": 400, "zugbezeichnung": "ICE"},
    {"strecke": "leipzig-berlin", "laenge_in_km": 180, "zugbezeichnung": "RE"},
]

MAX_KM_PRO_TAG = 800
PREIS_PRO_KM = 0.25
BAHNCARD_ERMAESSIGUNG = 0.5
INTERRAIL_TICKET_PREIS = 283

def berechne_guenstigstes_ticket(strecken):
    tages_gesamt = 0
    tage_unterwegs = 0
    gesamt_preis_km = 0
    
    for strecke in strecken:
        if (tages_gesamt + strecke["laenge_in_km"]) > MAX_KM_PRO_TAG:
            tage_unterwegs += 1
            tages_gesamt = 0
        tages_gesamt += strecke["laenge_in_km"]
        if strecke["zugbezeichnung"] == "TGV":
            gesamt_preis_km += strecke["laenge_in_km"] * PREIS_PRO_KM
        else:
            gesamt_preis_km += (strecke["laenge_in_km"] * PREIS_PRO_KM) * BAHNCARD_ERMAESSIGUNG
    
    if tages_gesamt > 0:
        tage_unterwegs += 1
    
    guenstigstes_ticket = "interrail" if gesamt_preis_km > INTERRAIL_TICKET_PREIS else "ticket_pro_km"

    return {"tage_unterwegs": tage_unterwegs, "gesamt_preis_km": gesamt_preis_km, "guenstigstes_ticket": guenstigstes_ticket}

print(berechne_guenstigstes_ticket(strecken))