class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = []
        self.maxLength = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.maxLength:
            self.queue.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.maxLength:
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self):
        """
        :rtype: bool
        """
        if len(self.queue):
            self.queue.pop(0)
            return True
        else:
            return False

    def deleteLast(self):
        """
        :rtype: bool
        """
        if len(self.queue):
            self.queue.pop(len(self.queue) - 1)
            return True
        else:
            return False

    def getFront(self):
        """
        :rtype: int
        """
        if len(self.queue):
            return self.queue[0]
        else:
            return -1

    def getRear(self):
        """
        :rtype: int
        """
        if len(self.queue):
            return self.queue[len(self.queue) - 1]
        else:
            return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        if len(self.queue):
            return False
        else:
            return True

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.queue) == self.maxLength:
            return True
        else:
            return False
