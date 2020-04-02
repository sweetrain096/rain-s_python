class Node:
    def __init__(self, key, data=None):
        self.key = key      # 해당 노드에 포함되는 단어
        self.data = data    # 완성된 단어인지 체크
        self.children = {}  # 다음 연결될 단어
        self.cnt = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head
        if current_node.cnt.get(len(string)):
            current_node.cnt[len(string)] += 1
        else:
            current_node.cnt[len(string)] = 1

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)

            current_node = current_node.children[char]
            if current_node.cnt.get(len(string)):
                current_node.cnt[len(string)] += 1
            else:
                current_node.cnt[len(string)] = 1
        current_node.data = string

    def search(self, string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        if current_node.data:
            return True

    def start_with(self, prefix):
        current_node = self.head

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            elif char == '?':
                if current_node.cnt.get(len(prefix)):
                    return current_node.cnt[len(prefix)]
                return 0
            else:
                return 0



def solution(words, queries):
    answer = []
    len_dict = dict()
    trie = Trie()
    backtrie = Trie()
    for word in words:
        trie.insert(word)
        backtrie.insert(word[::-1])
        if len_dict.get(len(word)):
            len_dict[len(word)] += 1
        else:
            len_dict[len(word)] = 1

    for query in queries:
        if query[0] == '?' and query[-1] == '?':
            if len_dict.get(len(query)):
                answer.append(len_dict[len(query)])
            else:
                answer.append(0)
        elif query[0] != '?':
            answer.append(trie.start_with(query))
        else:
            answer.append(backtrie.start_with(query[::-1]))
    return answer



words = [["frodo", "front", "frost", "frozen", "frame", "kakao"]	,
         ["sfei", "fwji", "fdsi", "asei", "bsei", "wwqtei"]]
queries = [["fro??", "????o", "fr???", "fro???", "pro?"]	,
           ["z???","???i", "??ei", "????", "?????", "??????"]]
for i in range(len(words)):
    print(solution(words[i], queries[i]))