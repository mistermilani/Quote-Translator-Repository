import flet as ft

def main(page: ft.Page):
    #Functions
    def change(e: ft.Event[ft.Button]):
        quote.value = radio.value

    #Main page
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Controls
    quote = ft.Text(value = "“夢を見るのは悪いことじゃない、だが現実も見ろ。”\n— All Might", size = 25, weight = ft.FontWeight.BOLD)
    allimage = ft.Image(src = "AllMight.png", height = 500, width = 500)
    row = ft.Row(controls=[allimage, quote], spacing=80, alignment=ft.MainAxisAlignment.START)
    radio = ft.RadioGroup(
        content = ft.Column(
            controls=[
                ft.Radio(value = "“夢を見るのは悪いことじゃない、だが現実も見ろ。”\n— All Might", label = "Japanese (Original)"),
                ft.Radio(value = "“It's not bad to dream, but you also have to consider what's realistic.”\n— All Might", label = "English"),
                ft.Radio(value = "“No está mal soñar, pero también tienes que considerar lo que es realista.”\n— All Might", label = "Spanish"),
                ft.Radio(value = "“Não é ruim sonhar, mas você também precisa considerar o que é realista.”\n— All Might", label = "Portuguese (Brazil)"),
                ft.Radio(value = "“Ce n’est pas mal de rêver, mais tu dois aussi considérer ce qui est réaliste.”\n— All Might", label = "French")]), on_change = change)
    
    page.add(row, radio)
ft.run(main, assets_dir = "images123")