from decimal import Decimal
from challenge.validation_rules import Validation

class CalculationPaint():

    def area(self, data_calculation):
        validation = Validation()
        area, message = 0, None

        #Terminar a parte de verificação dos dados que veio pelo html
        for i in range(1, 5):
            height = round(Decimal(data_calculation[i]['height']), 2)
            message = validation.valid_height(height)
            if message is not None:
                break
            width = round(Decimal(data_calculation[i]['width']), 2)
            message = validation.valid_area(width, height)
            if message is not None:
                break
            area += width * height

            window = round(Decimal(data_calculation[i]['window']), 2)
            door = round(Decimal(data_calculation[i]['door']), 2)
            message = validation.valid_doors_window(door, window, area)
            if message is not None:
                break

        return round(area, 2), message


    def calculation_paint_cans(self, data_calculation):
        liters_area, message = self.area(data_calculation)

        if message is not None:
            return {}, liters_area, message

        liters_paint = round(liters_area/ 5, 2)
        total_paint_cans = {
            '18 L': 0,
            '3.6 L': 0,
            '2.5 L': 0,
            '0.5 L': 0,
        }

        while liters_paint != 0:
            if liters_paint >= 18:
                liters_paint = round(liters_paint - Decimal(18), 2)
                total_paint_cans['18 L'] += 1
            elif 18 > liters_paint >= 3.6:
                liters_paint = round(liters_paint - Decimal(3.6), 2)
                total_paint_cans['3.6 L'] += 1
            elif 3.6 > liters_paint >= 2.5:
                liters_paint = round(liters_paint - Decimal(2.5), 2)
                total_paint_cans['2.5 L'] += 1
            elif 2.5 > liters_paint >= 0.5:
                liters_paint = round(liters_paint - Decimal(0.5), 2)
                total_paint_cans['0.5 L'] += 1
            elif 0 < liters_paint < 0.5:
                liters_paint = round(liters_paint - liters_paint, 2)
                total_paint_cans['0.5 L'] += 1

        return total_paint_cans, liters_area, message
