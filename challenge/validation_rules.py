from decimal import Decimal
class Validation():

    def valid_height(self, height):
        if height < (1.9 + 0.30):
            message = 'A altura de paredes com porta deve ser, no mínimo, 30 centímetros maior que a altura da porta'
            return message
        else:
            return None

    def valid_area(self, width, height):
        if 1 <= (width * height) <= 15:
            return None
        else:
            message = 'Nenhuma parede pode ter menos de 1 metro quadrado nem mais de 15 metros quadrados'
            return message

    def valid_doors_window(self, qtd_door, qtd_window, area):
        if ((Decimal(2.00) * Decimal(1.20)) * qtd_window) + ((Decimal(0.80) * Decimal(1.90)) * qtd_door) <= (area * Decimal(50)) / Decimal(100):
            return None
        else:
            message = 'O total de área das portas e janelas deve ser no máximo 50% da área total da parede'
            return message
