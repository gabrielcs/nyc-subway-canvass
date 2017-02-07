def add_coord_columns(dataframe, condensed_column, sep=', ', _reversed=False):
    """
    Extracts the longitude and latitude from condensed_column in dataframe and
    adds a column for each of them in the same dataframe.

    Obs.: expects latitude and longitude to be surrounded by parentheses. Reversed
    means longitude before latitude.
    """
    coord_str = dataframe.apply(lambda x: x[condensed_column][x[condensed_column].find("(") + 1 : \
                                                              x[condensed_column].find(")")], \
                                axis='columns')

    if not _reversed:
        coords = ('latitude', 'longitude')
    else:
        coords = ('longitude', 'latitude')

    dataframe[coords[0]] = coord_str.apply(lambda x: x[ : x.find(sep)]).astype(float)
    dataframe[coords[1]] = coord_str.apply(lambda x: x[x.find(sep) + 1 : ]).astype(float)
