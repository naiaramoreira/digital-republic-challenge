from challenge.validation_rules import Validation

class CalculationPaint():

    def area(self, data_calculation):
        validation = Validation()
        area = 0

        #Terminar a parte de verificação dos dados que veio pelo html
        for i in range(1, 5):
            height = data_calculation[i]['height']
            validation.valid_height(height)
            width = data_calculation[i]['width']
            validation.valid_area(width, height)
            area += width * height

            window = data_calculation[i]['window']
            door = data_calculation[i]['door']
            validation.valid_doors_window(door, window, area)

        return round(area, 2)


    def calculoLatas(self, data_calculation):
        litros_tinta = self.area(data_calculation) / 5
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

        return total_latas
