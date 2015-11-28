from distance_calculator.distance_calculator import get_distance


def parse_input(input_dictionary):

    v = []
    e = []

    for key, value in input_dictionary.iteritems():
        v.append(key)

    for source_key, source_value in input_dictionary.iteritems():
        for target_key, target_value in input_dictionary.iteritems():
            if source_key != target_key:
                e.append(((source_key, target_key), get_distance(source_value, target_value)))

    return v, e


def format_output(solution):
    return ''
