def value() -> str:
    return """
    Dzień dobry,

    W załączniku znajduje się faktura {numer_faktury} za fracht morski na kwotę {kwota} USD.

    Faktura zawiera:
    Usługa brokera: {usluga_brokera}
    Odbiór z aukcji i fracht morski do Rotterdamu: {odbior_frachtu}
    Ubezpieczenie cargo: {ubezpieczenie_cargo}
    Opłata za późną płatność i parking na aukcji: {oplata}

    Płatność jest w USD i jest realizowana na nasze polskie konto walutowe w banku PKO BP.

    Bank: PKO BP
    Numer konta IBAN: PL57 1020 4900 0000 8902 3092 5632
    SWIFT: BPKOPLPW

    
    """ 