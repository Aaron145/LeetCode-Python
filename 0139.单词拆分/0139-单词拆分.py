class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        record = [0]#һ��ʼ�ӿ�ͷ��ʼ��
        
        for j in range(len(s) + 1):
            for i in record:#��֮ǰÿһ���ҷ��Ļ�������
                if s[i : j] in wordDict: #�ҵ�һ�ֿ��еķַ���˵����Զ���Բ�ֵ�j
                    record.append(j)
                    break
        # print record
        return record[-1] == len(s)
                