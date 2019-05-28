from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or beginWord == endWord:
            return 0
        visited = set()
        wordList = set(wordList)
        
        q = deque()
        q.append([beginWord, 0])
        
        char = "abcdefghijklmnopqrstuvwxyz"
        while q:
            cur, cnt = q.popleft() #�Ӷ�����ȡһ������
            if cur == endWord: #����պ��ҵ���
                return cnt + 1
               
            for i in range(len(cur)):
                for j in range(26):
                    word = cur[:i] + char[j] + cur[i + 1:] #��26�ֱ任���ܶ�����
                    if word in wordList and word not in visited: #�жϱ任��û��Ч
                        visited.add(word)
                        q.append([word, cnt + 1])
                    
        return 0
                    
            