import pandas as pd

def read_table_from_file(joins, directory, filename):
    next_table = pd.read_csv(directory + '/' + filename, index_col=joins[filename]['index_col'],
                             usecols=joins[filename]['usecols'])

    if('resolve_duplicates' in joins[filename].keys()):
        field_to_resolve = joins[filename]['resolve_duplicates']
        duplicates = next_table.loc[next_table.duplicated(subset=field_to_resolve, keep=False)]
        for index, row in duplicates.iterrows():
            next_table.loc[index, field_to_resolve ] = row[field_to_resolve ] + '-' + str(index)

    columns_to_rename = joins[filename]['col_rename']
    if columns_to_rename is not None:
        next_table.rename(columns=columns_to_rename, inplace=True)
    return next_table


def next_join(joins, filename):
    return joins[filename]['join_with'], joins[filename]['join_on']


def joiner(joins, directory, start_file):
    accumulator = read_table_from_file(joins, directory, start_file)
    next_file, next_join_on = next_join(joins, start_file)
    while next_file is not None:
        print('Joining ' + next_file)
        next_table = read_table_from_file(joins, directory, next_file)
        accumulator = accumulator.join(next_table, on=next_join_on)
        next_file, next_join_on = next_join(joins, next_file)
    return accumulator

