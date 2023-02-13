class Converter:
    def __init__(self, value, in_unit, out_unit):
        self.value = value
        self.in_unit = in_unit
        self.out_unit = out_unit
        self.length_units = {'mm': 0.001, 'cm': 0.01, 'm': 1, 'feet': 0.3048, 'inches': 0.0254}
        self.volume_units = {'ml': 0.001, 'dl': 0.01, 'L': 1, 'pints': 0.473176473, 'quarts': 0.946352946, 'cups': 0.236588236}

    def convert_length(self):
        in_value = self.value * self.length_units[self.in_unit]
        out_value = in_value / self.length_units[self.out_unit]
        return out_value

    def convert_volume(self):
        in_value = self.value * self.volume_units[self.in_unit]
        out_value = in_value / self.volume_units[self.out_unit]
        return out_value

def main(value, in_unit, out_unit):
    length_units = ['mm', 'cm', 'm', 'feet', 'inches']
    volume_units = ['ml', 'dl', 'L', 'pints', 'quarts', 'cups']
    if in_unit in length_units and out_unit in length_units:
        converter = Converter(value, in_unit, out_unit)
        result = converter.convert_length()
    elif in_unit in volume_units and out_unit in volume_units:
        converter = Converter(value, in_unit, out_unit)
        result = converter.convert_volume()
    else:
        raise ValueError("Invalid units")
    return result

if __name__ == '__main__':
    import sys
    value = int(sys.argv[1])
    in_unit = sys.argv[2][1:]
    out_unit = sys.argv[4][1:]
    print(main(value, in_unit, out_unit))
