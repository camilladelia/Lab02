def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    nuovo_album= []

    try:
        with open (file_path,"r", encoding= "utf-8") as file:
            linee= file.readlines()
            if not linee:
                return nuovo_album
            for linea in linee[1:]:
                dati= linea.strip().split(",")
                if len(dati)== 5:
                    codice,titolo,autore,mese,anno = dati
                    mese= int(mese)
                    anno=int(anno)
                    #Raggruppa in dizionario
                    foto ={
                        "codice" : codice,
                        "titolo": titolo,
                        "autore": autore,
                        "mese": mese,
                        "anno": anno
                    }
                    anno_presente= False
                    for gruppo in nuovo_album:
                        if gruppo [0]== anno:
                            gruppo [1].append(foto)
                            anno_presente= True
                            break
                    if not anno_presente:
                        nuovo_album.append([anno, [foto]])
        return nuovo_album
    except FileNotFoundError:
        return None

def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    if mese< 1 or mese >12:
        return None
    for gruppo in album:
        for f in gruppo [1]:
            if f["codice"]== codice:
                return None
    try:
        with open (file_path, "r", encoding= "utf-8") as file:
            pass
    except FileNotFoundError:
        return None
    nuova_foto={
        "codice": codice,
        "titolo": titolo,
        "autore": autore,
        "mese":mese,
        "anno":anno
    }
    anno_presente= False
    for gruppo in album:
        if gruppo[0]== anno:
            gruppo[1].append(nuova_foto)
            anno_presente= True
            break
    if not anno_presente:
        album.append([anno,[nuova_foto]])
    with open (file_path, "a", encoding= "utf-8") as file:
        file.write(f"\n{codice},{titolo},{autore},{mese},{anno}")
    return nuova_foto

def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    for gruppo in album:
        lista_foto_anno= gruppo[1]

        for foto in lista_foto_anno:
            if foto ["codice"]== codice:
                risultato= f"{foto['codice']}{foto['titolo']}, {foto['autore']}, {foto['mese']}, {foto['anno']}"
                return risultato
    return None


def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    for gruppo in album:
        if gruppo [0]== anno:
            lista_foto_anno= gruppo [1]
            titoli = []
            for foto in lista_foto_anno:
                titoli.append(foto["titolo"])
            titoli.sort()

            return titoli
    return None
def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
