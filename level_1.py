def process_file(input_path, output_path):

    input_data = []
    with open(input_path, "r") as infile:
        for line in infile:
            input_data.append(line.strip())  # do some parsing here

    input_data = input_data[1:]
    result = []
    for data in input_data:
        [x,y] = data.split()
        result.append(int(x)/3*int(y))

    with open(output_path, "w") as outfile:
        for value in result:
            outfile.write(f"{int(value)}\n")


def main():
    level = 1
    num_files = 5

    for i in range(1, num_files + 1):
        input_path = f"input/level_{level}/level{level}_{i}.in"
        output_path = f"output/level_{level}/level{level}_{i}.out"
        process_file(input_path, output_path)


if __name__ == "__main__":
    main()
