from distance_calculator.distance_calculator import get_distance


def parse_input(input_dictionary):

    v = input_dictionary
    e = {}

    for source_key, source_value in input_dictionary.iteritems():
        for target_key, target_value in input_dictionary.iteritems():
            if source_key != target_key:
                e[(source_key, target_key)] = get_distance(source_value, target_value)

    return v, e


def format_output(solution):
    output_string = '%d\n' % solution['total']
    for vertex in solution['order']:
        output_string = "%s%d\n" % (output_string, vertex)
    return output_string
