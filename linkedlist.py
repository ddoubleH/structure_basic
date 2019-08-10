class Node:
    def __init__(self):
        self.data = None
        self.link = None

class LinkedList:
    state = True

    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.nodelist = [self.head]

    def newNode(self, data):

        newNode = Node()
        newNode.data = data
        newNode.link = None

        return newNode

    # 추가 (노드와 노드 사이에 데이터 추가)
    def insert(self, LinkedList, newnode):

        if LinkedList.state:
            LinkedList.head.link = newnode
            LinkedList.state = False
        else:
            LinkedList.tail.link = newnode

        LinkedList.nodelist.append(newnode)
        LinkedList.tail = newnode

    def info(linkedlist):
        print('LinkedList Head : ', linkedlist.head,
              'LinkedList Tail : ', linkedlist.tail)

        for i in range(len(linkedlist.nodelist)):
            print(i, 'Node :', linkedlist.nodelist[i],
                  i, 'Node Data : ' , linkedlist.nodelist[i].data,
                  i, 'Node Link : ', linkedlist.nodelist[i].link )

    # 삭제 (맨뒤에 있는 노드, 중간에 노드 > 값 )

    # 검색 (몇번째 노드인지 출력)



if __name__ == '__main__':
    LinkedList = LinkedList()

    while(True):
        word = input('Input Command > ')

        if word == 'quit' or word == 'q' :
            break

        elif word == 'insert':
            data = input('Input Node Data > ')
            node = LinkedList.newNode(data)
            LinkedList.insert(LinkedList, node)

        elif word == 'info':
            LinkedList.info()

        else:
            print('Command Not Found')


