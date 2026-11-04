import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        self._view.dd_biblioteca.options.clear()

        self._view.dd_biblioteca.options.append(
            ft.DropdownOption(key="NONE", text="Nessun filtro")    #di default per ignorare il filtro
        )
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(
                ft.DropdownOption(key=str(b.id), text=b.nome)
            )

        generi = self._model.get_generi()
        self._view.dd_genere.options.clear()

        self._view.dd_genere.options.append(
            ft.DropdownOption(key="NONE", text="Nessun filtro")
        )
        for g in generi:
            self._view.dd_genere.options.append(
                ft.DropdownOption(key=g, text=g)
            )

        self._view.update()

    # CALLBACKS DROPDOWN
    def on_select_biblioteca(self, e):
        """Salva l'ID della biblioteca selezionata oppure None se disattivato."""
        valore = self._view.dd_biblioteca.value
        if valore and valore != "NONE":
            try:
                self.biblioteca_selezionata = int(valore)
            except ValueError:
                self.biblioteca_selezionata = valore
        else:
            self.biblioteca_selezionata = None

    def on_select_genere(self, e):
        """Salva il genere selezionato oppure None se disattivato."""
        valore = self._view.dd_genere.value
        if valore and valore != "NONE":
            self.genere_selezionato = valore
        else:
            self.genere_selezionato = None

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        valore_bib = self._view.dd_biblioteca.value
        valore_gen = self._view.dd_genere.value

        id_biblioteca = int(valore_bib) if valore_bib and valore_bib != "NONE" else None
        genere = valore_gen if valore_gen and valore_gen != "NONE" else None

        libri = self._model.get_libri_filtrati(id_biblioteca, genere)

        # Svuoto la lista prima di riempirla
        self._view.lista_libri.controls.clear()

        if not libri:
            self._view.lista_libri.controls.append(
                ft.Text("Nessun libro trovato.")
            )
        else:
            for libro in libri:
                self._view.lista_libri.controls.append(
                    ft.Text(f"{libro.titolo} — Autore: {libro.autore} (Genere: {libro.genere})")
                )

        self._view.update()