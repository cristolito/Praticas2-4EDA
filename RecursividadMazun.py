import flet as ft

class Matematico:
    def __init__(self):
        pass

    def Factorial(self,n):
        if(n<=1):
           res = 1
        if (n>1):
           res = n * self.Factorial(n-1)
        return res

    def Fibonacci(self,n):
        res = 0
        if(n == 1):
           res = 1
        if(n > 1):
           res = self.Fibonacci(n-1)+self.Fibonacci(n-2)
        return res
    
    def MaximoComunDivisor(self,a, b):
        if b == 0:
           return a
        return self.MaximoComunDivisor(b, a % b)
    
def main(page: ft.Page):
    def changeInterface(e):
        if(menu_options.value=="Fibonacci"):
            title.value = "La Serie Fibonacci"
            input1.label = "Posición de la serie Fibonacci"
            input2.visible=False
        if(menu_options.value=="Factorial"):
            title.value = "Encontrar el Factorial"
            input1.label = "¿Qué factorial quiere encontrar?"
            input2.visible=False
        if(menu_options.value=="Máximo Común Divisor"):
            title.value = "Encontrar el Máximo Común Divisor"
            input1.label = "Número 1"
            input2.visible=True
        input1.value = ""
        input2.value = ""
        result.value = "Resultado: "
        page.update()

    def handle_event_click(e):
        result.value = "Resultado: "
        if(menu_options.value=="Fibonacci"):
            result.value = result.value + str(matematico.Fibonacci(float(input1.value)))
        if(menu_options.value=="Factorial"):
            result.value = result.value + str(matematico.Factorial(float(input1.value)))
        if(menu_options.value=="Máximo Común Divisor"):
            result.value = result.value + str(matematico.MaximoComunDivisor(float(input1.value),float(input2.value)))
        page.update()

    title = ft.Text("La serie Fibonacci",size=25,weight="bold")
    result = ft.Text("Resultado: ")
    matematico = Matematico()

    input1 = ft.TextField(label="Posición de la serie Fibonacci", width=300)
    input2 = ft.TextField(label="Número 2", visible=False, width=300)
    menu_options = ft.Dropdown(options=[
        ft.dropdown.Option("Fibonacci"),
        ft.dropdown.Option("Factorial"),
        ft.dropdown.Option("Máximo Común Divisor")
    ], width=250,value="Fibonacci", on_change=changeInterface)
    btn_cal = ft.ElevatedButton("Encontrar numero", on_click=handle_event_click)

    container = ft.Container(
        ft.Column([
            menu_options, title, input1, input2, btn_cal, result]),alignment=ft.alignment.center,
            margin=25)

    page.add(container)

ft.app(target=main)