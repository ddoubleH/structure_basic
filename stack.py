#Last in first out
class stack():

	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		try:
			del self.stack[-1]
			return True
		except:
			return False
	# return True,  try catch  try catch: true 데이터 삭제 굳이 리턴을 하면 예외처리를 하기 위해서 예외 발생시 false

	def isEmpty(stack):
		if stack is None:
			return True
		else:
			return False

	def getSize(self):
		return len(self.stack)


if __name__ == '__main__':
	S = stack()
	print(S.stack)
	S.push(10)
	S.push(20)
	S.push(30)
	S.push(40)
	S.push(50)
	print(S.stack)
	S.pop()
	S.pop()
	print(S.stack)
