#1▹ Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
# W pętli spróbuj wykonać dzielenie 10 przez wartość z listy.
# Złap wyjątki jakie mogą się przy tej okazji wydarzyć.

items = [13, 'string', 2.45, 0, 'e', True, False, [], {'key': 3}]
collected_errors = []


for value in items:
    try:
        result = 10 / value
    except TypeError as e:
        result = 0
        collected_errors.append(e)
    except ZeroDivisionError as e:
        result = 1
        collected_errors.append(e)

    print(result)

for err in collected_errors:
    print(f' {err}')