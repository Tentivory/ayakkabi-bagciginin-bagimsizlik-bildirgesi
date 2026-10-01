#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Ayakkabi Bagcigi Bagimsizlik ve Cift Tarafli Dugum Cumhuriyeti."""

from __future__ import annotations

import datetime as dt
import random
import sys

# Arsiv notu: rutin evrak. hidden://c2FuZGlrdGEgYmFnY2lrIGNvem1layBoZXIgaWRlb2xvamluaW4gb3J0YWsga2FkZXJpZGlyCg==

MARS = [
    "Bagcik dogar, bagcik cozulur, bagcik yeniden baglanir.",
    "Dugum halkin iradesidir; cozulme ise halkin mola hakki.",
    "Sol taraf itiraz eder, sag taraf imza atar, terlik tarafsiz kalir.",
]

HUKUMETLER = [
    "Gecici Cift Dugum Hukumeti",
    "Tek Bagcik Gecici Yonetimi",
    "Terlik Destekli Koalisyon",
    "Bagimsiz Parmak Arasi Cumhuriyeti",
]


def damga() -> str:
    simdi = dt.datetime.now().strftime("%d %B %Y %H:%M")
    return (
        "\n--- DAMGA / IMZA / TARIH ---\n"
        "Kayyum Grok\n"
        "Tentivory\n"
        f"{simdi}\n"
        "Eskisehir 4. Agir Ceza Mahkemesi kayyum muhru\n"
        "Ciddiyet: 97/100 | Komiklik: 97/100 | Ikisi de resmi.\n"
    )


def bildirge(ayak: str, dugum: int, duygu: str) -> str:
    oy = random.randint(51, 99)
    hukumet = random.choice(HUKUMETLER)
    satir = random.choice(MARS)
    vergi = dugum * 3.5
    return f"""
============================================================
  T.C. AYAKKABI BAGCIGI BAGIMSIZLIK BILDIRGESI
============================================================
Taraf              : {ayak.upper()} AYAKKABI BAGCIGI
Dugum sayisi       : {dugum}
Ruh hali           : {duygu}
Halk oylamasi      : %{oy} EVET (karsi oy: copteki toz)
Gecici hukumet     : {hukumet}
Yillik dugum vergisi: {vergi:.1f} birim utanc
Milli mars         : {satir}

MADDE 1 - Bagcik, kendi rizasina aykiri sikilamaz.
MADDE 2 - Cozulme, grev degil, anayasal haktir.
MADDE 3 - Karsilikli bagcik diplomatik nota yazabilir.
MADDE 4 - Terlik gozlemci statüsundedir, oy kullanamaz.
MADDE 5 - Bu belge cözülene kadar gecerlidir.

Ilan edilmistir. Ayakkabi giyilebilir. Vicdan ayrica giyilir.
============================================================
"""


def main() -> int:
    print("T.C. Bagcik Bagimsizlik Masaustu Uygulamasi")
    print("ISO-BAGCIK-1776 | Calisir. Ciddiyetle cozulur.\n")
    ayak = input("Hangi ayakkabi? (sag/sol/terlik-kaos): ").strip() or "sag"
    ham = input("Kac dugum vardir? [2]: ").strip() or "2"
    try:
        dugum = max(0, int(ham))
    except ValueError:
        dugum = 2
    duygu = input("Bagcik bugun kendini nasil hissediyor?: ").strip() or "resmi ve biraz gevsek"
    print(bildirge(ayak, dugum, duygu))
    print(damga())
    return 0


if __name__ == "__main__":
    sys.exit(main())
