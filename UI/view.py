import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self.dd_biblioteca = ft.Dropdown(label = "Biblioteca",
                                     options = [],
                                     width = 300,
        )
        self.dd_biblioteca.on_change = self.controller.on_select_biblioteca

        self.dd_genere = ft.Dropdown(label = "Genere",
                                     options = [],
                                     width = 300,
        )
        self.dd_genere.on_change = self.controller.on_select_genere

        row_filtri = ft.Row(
            controls=[self.dd_biblioteca, self.dd_genere],
            alignment=ft.MainAxisAlignment.CENTER

        )

        # Sezione 3: Libri
        self.btn_mostra_libri = ft.FilledButton(
            content=ft.Text("Mostra Libri"),
            on_click=self.controller.handle_mostra_libri
        )

        self.lista_libri = ft.ListView(
            expand=True,
            spacing=10,
            padding=10,
            auto_scroll=False
        )

        container_libri = ft.Container(
            content=self.lista_libri,
            border=ft.Border.all(1, "outline"),
            border_radius=8,
            height=300,
            padding=10,
            width=600
        )

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            row_filtri,

            # Sezione 3: Libri
            ft.Row([self.btn_mostra_libri], alignment=ft.MainAxisAlignment.CENTER),
            container_libri
        )

        if self.controller:
            self.controller.popola_dropdown()

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
