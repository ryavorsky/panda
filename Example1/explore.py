import json
import statistics

part_number = 1
file_name = "part" + str(part_number)

with open(file_name + ".json", encoding="utf-8") as f:
    data = json.load(f)

min_max_size = []
average_size = []
for section in data[1:]:
    section_number = [section["section_number"]]
    paragraphs = section["paragraphs"]
    sizes = [len(par) for par in paragraphs]
    print(sizes)

    min_size = min(sizes)
    max_size = max(sizes)
    med_size = statistics.median(sizes)
    min_max_size.append([section_number, min_size, max_size])
    average_size.append([section_number, med_size])

print(min_max_size)
print(average_size)


with open("index_template.txt", "r") as template_file:
    result_html = template_file.read()

result_html = result_html.replace("{{ranges}}", json.dumps(min_max_size))
result_html = result_html.replace("{{averages}}", json.dumps(average_size))

with open(file_name + ".html", "w") as res_file:
    res_file.write(result_html)
