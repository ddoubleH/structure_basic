class Node:
    def __init__(self):
        self.data = None
        self.link = None


class LinkedList:
    state = True

    def __init__(self):
        self.head = Node()
        self.before = None
        self.current = None
        self.tail = self.head
        self.nodelist = [self.head]
        self.nodenum = 1

    def newNode(self, data):

        newNode = Node()
        newNode.data = data
        newNode.link = None

        return newNode

    # 추가 (노드와 노드 사이에 데이터 추가)
    def insert(self, LinkedList, newnode):

        # 헤드 뒤 연결
        if LinkedList.state:
            LinkedList.head.link = newnode
            LinkedList.nodelist.append(newnode)
            #LinkedList.current = newnode
            #LinkedList.before = LinkedList.head
            LinkedList.state = False

        # 노드와 노드 사이에 데이터 추가
        # 값, 인덱스
        elif False:
            pass

        # 젤뒤에 연결
        else:
            #LinkedList.before = LinkedList.nodelist[-1]
            #LinkedList.current = newnode
            LinkedList.tail = newnode
            LinkedList.nodelist[-1].link = newnode
            LinkedList.nodelist.append(newnode)  # 뒤에 붙임


    def info(linkedlist):
        print('LinkedList Head : ', linkedlist.head,
              'LinkedList Tail : ', linkedlist.tail)

        for i in range(len(linkedlist.nodelist)):
            print(i, 'Node :', linkedlist.nodelist[i],
                  i, 'Node Data : ', linkedlist.nodelist[i].data,
                  i, 'Node Link : ', linkedlist.nodelist[i].link)

    def isEmpty(self, LinkedList):
        if LinkedList is None:
            return True
        else:
            return False

    # 삭제 (중복 값 없음)
    # Value, Index
    def delete(self, LinkedList, removeData):
        if self.isEmpty(LinkedList):
            return 'No node to delete'

        # 지우고자 하는 값이 Tail인 경우
        elif LinkedList.nodelist[-1].data == removeData:
            LinkedList.tail = LinkedList.nodelist[-2]
            LinkedList.nodelist[-2].link = None
            del LinkedList.nodelist[-1]
            return 'Node Remove'

        # 지우고자 하는 값이 중간에 있는 경우
        else:
            for i in range(len(LinkedList.nodelist)):
                if LinkedList.nodelist[i].data == removeData:
                    # swap
                    LinkedList.nodelist[i-1].link = LinkedList.nodelist[i].link
                    del LinkedList.nodelist[i]
                    return 'Node Remove'
        

    # 검색 (몇번째 노드인지 출력)
    def search(self, LinkedList, node):
        if LinkedList.tail == None:
            print('No node to search')
            return
        else:
            link = LinkedList.head.link
            num = 0
            if node == data:
                return num


if __name__ == '__main__':
    LinkedList = LinkedList()

    while(True):
        word = input('Input Command > ')

        if word == 'quit' or word == 'q':
            break

        elif word == 'insert':
            data = input('Input Node Data > ')
            node = LinkedList.newNode(data)
            LinkedList.insert(LinkedList, node)

        elif word =='delete':
            data = input('Delete Node Data > ')
            LinkedList.delete(LinkedList, removeData=data)

        elif word =='search':
            data = input('Search Node Data > ')
            node = LinkedList.newNode(data)
            LinkedList.search(LinkedList, node)

        elif word == 'info':
            LinkedList.info()

        else:
            print('Command Not Found')


