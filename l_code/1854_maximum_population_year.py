# Time O(n*log(n))  Space: O(n)
def get_max_population_year(logs):
    events = []
    for start, end in logs:
        events.append((start, 's'))
        events.append((end, 'e'))

    events.sort()
    population = 0
    max_population = 0
    max_population_year = None

    for year, event_type in events:
        if event_type == 'e':
            population -= 1
        else:
            population += 1

        if max_population < population:
            max_population = population
            max_population_year = year

    return max_population_year


def test():
    logs = [[1980, 2000], [2000, 2020]]
    assert get_max_population_year(logs) == 1980


def test_2():
    logs = [[1980, 2000], [1999, 2020]]
    assert get_max_population_year(logs) == 1999