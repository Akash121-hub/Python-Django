import re

str1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, 8551910910 but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 9766366007 and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum (732)-666-8888."

pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'

matches = re.findall(pattern, str1)
print(matches)
my_dict = {"name":"Manas","id":23}

a = my_dict.get('name')
print(a)