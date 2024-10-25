def process_file(input_path, output_path):

    input_data = []
    with open(input_path, "r") as infile:
        for line in infile:
            input_data.append(line.strip())  # do some parsing here

    input_data = input_data[1:]
    result = []
    table_id = 1
    for data in input_data:
        [x_size,y_size, tables] = data.split()
        for y in range(0, int(int(y_size))):
            for x in range(0, int(int(x_size)/3)):
                if(table_id > int(tables)):
                    continue
                result.append(f"{table_id} {table_id} {table_id} ")
                table_id = table_id + 1
            result.append("\n")
        result.append("\n")
        table_id = 1



    with open(output_path, "w") as outfile:
        for value in result:
            outfile.write(f"{value}")


def main():
    level = 2
    num_files = 5

    for i in range(1, num_files + 1):
        input_path = f"input/level_{level}/level{level}_{i}.in"
        output_path = f"output/level_{level}/level{level}_{i}.out"
        process_file(input_path, output_path)


if __name__ == "__main__":
    main()
