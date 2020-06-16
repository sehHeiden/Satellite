# https://uber.github.io/h3/#/documentation/core-library/resolution-table

h3_res = {0: 1107.712591000,
          1: 418.676005500,
          2: 158.244655800,
          3: 59.810857940,
          4: 22.606379400,
          5: 8.544408276,
          6: 3.229482772,
          7: 1.220629759,
          8: 0.461354684,
          9: 0.174375668,
          10: 0.065907807,
          11: 0.024910561,
          12: 0.009415526,
          13: 0.003559893,
          14: 0.001348575,
          15: 0.000509713
          }


def h3_radius(level: int) -> float:
    """
    :param level: h3 resolution level
    :return: the radius of the h3 hexagon of level level in meter
    """
    return 0.866 * h3_res[level] * 1000.0
