
def get_summary_rss(file_path):
    with open(file_path, encoding='utf-8') as file:
        total_bits = 0
        for line in file.readlines()[1:]:
            splitted_line = line.split()
            rss_value = splitted_line[5]
            total_bits += int(rss_value)

        total_kb = total_bits / 1024
        total_mb = total_kb / 1024
        print(f"{total_bits} B, {total_kb} KB, {total_mb} MB")
path_to_file = 'output_file.txt'
if __name__ == '__main__':
    get_summary_rss(path_to_file)