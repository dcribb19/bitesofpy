def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    hex_conversion = '#'
    for color in rgb:
       if not color in range(0, 256):
          raise ValueError
       else:
          color = '{0:x}'.format(color).upper()
          if len(color) == 1:
             color = '0' + color
       hex_conversion += color
    return hex_conversion
