class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if int(low) > int(high):
            return 0
        self.findStrobogrammatic(len(high))
        #��low����
        low_rec = self.record[len(low)]
        #�ҵ�һ�� >= low�������±�
        low_cnt = 0
        for i, num in enumerate(low_rec):
            if int(num) >= int(low):
                low_cnt = len(low_rec) - i
                break
                
        high_rec = self.record[len(high)]
        high_cnt = len(high_rec)
        for i, num in enumerate(high_rec):
            if int(num) > int(high):
                high_cnt = i
                break

        if len(low) + 1 == len(high):
            return low_cnt + high_cnt
        elif len(low) == len(high):
            return low_cnt + high_cnt - len(high_rec)
        else:
            tmp = 0
            for l in range(len(low) + 1, len(high)):
                # print l, self.record
                tmp += len(self.record[l])
            return tmp + low_cnt + high_cnt
        #�ҵ�һ�� > high�������±�
        # left, right = 0, len(low_rec) - 1
        # while left < right:
        #     mid = (left + right) // 2
        #     if low_rec[mid] == low:
        #         low_cnt = len(low_rec) - mid
        #     elif low_rec[mid] > low:
        #         right = mid - 1
        #     elif low_rec[mid] < low:
        #         left = mid + 1
            
        
        
 
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.record = dict()
        self.record[0] = ["0"]
        self.record[1] = ["0", "1", "8"]
        self.record[2] = ["11", "69", "88", "96"]
        pair = ["00", "11", "88", "69", "96"]
        if n <= 2:
            return self.record[n]
        cnt = 3
        while cnt <= n:
            tmp = []
            if (cnt - 1) % 2 == 0: #���ǰһ����ż�����ȣ���ôֱ�����м�ӳ���Ϊ1�ľͿ���
                for item in self.record[cnt - 1]:
                    for num in self.record[1]:
                        tmp.append(item[:len(item)// 2] + num + item[len(item) // 2:])
            else:                  #���ǰһ�����������ȣ���ô�����м�ӳ���Ϊ2�ľͿ��� ��ע��Ҫ����ӡ�00��
                for item in self.record[cnt - 2]:
                    for num in pair:
                        tmp.append(item[:len(item)// 2] + num + item[len(item) // 2:])
            self.record[cnt] = sorted(tmp, key = lambda x: int(x))
            cnt += 1