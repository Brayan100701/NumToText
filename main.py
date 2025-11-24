import flet as ft
import utilidades

def main(page: ft.Page):
    def convert(*_):
        pass


    page.window.width = 500
    page.window.height = 300
    page.title = 'Traductor numero a texto'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    lbl_number = ft.Text(value='Ingresa el numero')
    txt_number = ft.TextField(value='0', width=150)
    btn_translate = ft.Button(text='Traducir a Texto', on_click=convert)
    lbl_text = ft.Text(value='')

    page.add(
        ft.Column(
            controls=[
                lbl_number,
                txt_number,
                btn_translate,
                lbl_text
            ]
        )
    )

    page.update()


if __name__ == '__main__':
    ft.app(main)
