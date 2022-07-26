def flights(*args):
    result = {}

    for idx in range(0, len(args) - 1, 2):
        destination = args[idx]
        if destination == "Finish":
            break
        passengers = args[idx + 1]
        if destination in result:
            result[destination] += passengers
        else:
            result[destination] = passengers

    return result


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
