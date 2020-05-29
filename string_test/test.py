import sys
sys.stdin = open("test.txt")

with open("test.txt", 'rb') as f:
    s = f.read().decode('utf8')
# print(s)
s = ''.join(s.split('  <p class="calibre1">'))
s = ''.join(s.split('</p>'))
print(s)