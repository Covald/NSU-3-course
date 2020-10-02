import matplotlib.pyplot as plt

file = open('alice.txt', 'r')
file_as_string = file.read()
file.close()
list_of_words = file_as_string.split()
print(file_as_string, '\n')
print('number of words:', len(list_of_words), '\n')

file_as_string = file_as_string.replace(list_of_words[2], list_of_words[2][::-1], 1)  # [begin:end:step]
print(file_as_string, '\n')

# s = ' '.join(s.split()[::-1])
s_new = ''
check = 0

for x in file_as_string:
    if x == '.' and check == 0:
        s_new = ' '.join(s_new.split()[::-1])
        check = 1
    s_new += x

file_as_string = s_new
print(file_as_string, '\n')

file_as_string = file_as_string[0].upper() + file_as_string[1::]
print(file_as_string, '\n')

file = open('result.txt', 'w')
file.write(file_as_string)
file.close()

x_axis = [chr(x) for x in range(ord('a'), ord('z') + 1)]
x_axis_pos = [x for x in range(26)]
y_axis = [file_as_string.lower().count(x) for x in x_axis]

ax = plt.axes()
ax.set_xticks(x_axis_pos)
ax.set_xticklabels(x_axis)

plt.bar(x_axis_pos, y_axis, color='black')
plt.show()
