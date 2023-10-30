def sparse_add(vector_1: dict, vector_2: dict):
    vector_add = dict()
    vector_add["length"] = vector_1["length"]
    for index in range(vector_1["length"]):
        if index in vector_1 and index in vector_2:
            sum_index = vector_1[index] + vector_2[index]
            if sum_index:
                vector_add[index] = sum_index
        elif index in vector_1:
            vector_add[index] = vector_1[index]
        elif index in vector_2:
            vector_add[index] = vector_2[index]
    return vector_add


def sparse_dot_product(vector_1: dict, vector_2: dict):
    dot_product = 0
    for index in range(vector_1["length"]):
        if index in vector_1 and index in vector_2:
            dot_product_index = vector_1[index] * vector_2[index]
            dot_product += dot_product_index
    return dot_product


def main():
    vector_1 = {"length": 10, 0: 3, 1: 4, 6: 5}
    vector_2 = {"length": 10, 0: 1, 3: 2, 6: 3, 9: 4}

    vector_add = sparse_add(vector_1, vector_2)
    print(f"vector add: {vector_add}")

    vector_dot_product = sparse_dot_product(vector_1, vector_2)
    print(f"vector_dot_product: {vector_dot_product}")


if __name__ == "__main__":
    main()
