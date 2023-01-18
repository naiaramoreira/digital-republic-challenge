class Validation():

    def valid_height(self, height):
        if height < (1.9 + 0.30):
            print('A altura de paredes com porta deve ser, no mínimo, 30 centímetros maior que a altura da porta')
            return False
        else:
            return True

    def valid_area(self, width, height):
        if 1 <= (width * height) <= 15:
            return True
        else:
            print('"Nenhuma parede pode ter menos de 1 metro quadrado nem mais de 15 metros quadrados"')
            return False

    def valid_doors_window(self, qtd_door, qtd_window, area):
        if ((2.00 * 1.20) * qtd_window) + ((0.80 * 1.90) * qtd_door) <= (area * 50) / 100:
            return True
        else:
            print("O total de área das portas e janelas deve ser no máximo 50% da área total da parede")
            return False
