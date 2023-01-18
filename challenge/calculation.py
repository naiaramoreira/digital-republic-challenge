from challenge.validation_rules import Validation

class Tintas():

    def area(self):
        validation = Validation()
        area = 0

        for i in range(1,5):
            height = round(float(input(f"Qual a altura da parede {i}?: ")), 2)
            validation.valid_height(height)
            width = round(float(input(f"Qual a largura da parede {i}?: ")), 2)
            validation.valid_area(width, height)
            area += width + height

            window = int(input(f"Quantas janelas  possui a parede {i}?: "))
            door = int(input(f"Quantas portas  possui a parede {i}?: "))
            validation.valid_doors_window(door, window, area)



        return round(area, 2)


    def calculoLatas(self):
        litros_tinta = self.area() / 5
        total_latas = {
            '18 L': 0,
            '3.6 L': 0,
            '2.5 L': 0,
            '0.5 L': 0,
        }
        print(f"Você vai precisar de {litros_tinta}")

        while round(litros_tinta, 2) != 0:
            if litros_tinta >= 18:
                litros_tinta -= 18
                total_latas['18 L'] += 1
            elif 18 > litros_tinta >= 3.6:
                litros_tinta -= 3.6
                total_latas['3.6 L'] += 1
            elif 3.8 > litros_tinta >= 2.5:
                litros_tinta -= 2.5
                total_latas['2.5 L'] += 1
            elif 2.5 > litros_tinta >= 0.5:
                # Verificar com 19 litros de tinta - > tamanho total 95
                litros_tinta -= 0.5
                total_latas['0.5 L'] += 1
            elif 0 > litros_tinta < 0.5:
                litros_tinta -= litros_tinta
                total_latas['0.5 L'] += 1
        print(total_latas)

Tintas().calculoLatas()
