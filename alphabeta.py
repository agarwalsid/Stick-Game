
from sys import maxsize



class Node(object):
	def __init__(self,depth,playNum,sticksRem,val=0):
		self.depth=depth
		self.playNum=playNum
		self.sticksRem=sticksRem
		self.val=val
		self.children=[]
		self.CreateChildren()


	def CreateChildren(self):
		if self.depth>=0:
			for i in range(1,4):
				v=self.sticksRem-i
				self.children.append(Node(self.depth-1,-self.playNum,v,self.RealVal(v)))

	def RealVal(self,value):
		if(value==0):
			return maxsize*-self.playNum #return maxsize*self.playNum
		elif(value<0): 
			return maxsize*-self.playNum
		return 0

	def __repr__(self, level=0):
        	ret = "\t"*level+repr(self.val)+"\n"
        	for child in self.children:
        		ret += child.__repr__(level+1)
        	return ret

	def height(self):  
       
        	height = 0  
        	for child in self.children:  
            		height = max(height, child.height() + 1)  
        	return height  



def MinMax(node,depth,playNum):
	if(depth==0)or(abs(node.val)==maxsize):
		return node.val

	bestVal=maxsize*-playNum

	for i in range(len(node.children)):
		child=node.children[i]
		newVal=MinMax(child,depth-1,-playNum)
		if(abs(maxsize*playNum-newVal)<abs(maxsize*playNum-bestVal)):
			bestVal=newVal
	#print (str(depth*playNum) + ") "+" "*depth + str(bestVal))
	return bestVal

def AlphaBeta(node, depth, alpha, beta, playNum):
        if(depth==0)or(abs(node.val)==maxsize):
		return node.val

	bestVal=maxsize*-playNum
	if (playNum == 1):
		for i in range(len(node.children)):
			child=node.children[i]
			alpha = max(alpha, AlphaBeta(child, depth - 1, alpha, beta, 1))
			if (beta<=alpha):
				break
		print (str(depth*playNum) + ") "+" "*depth + str(alpha))
		return alpha
		
	else:
		for i in range(len(node.children)):
			child=node.children[i]
			beta = min(beta, AlphaBeta(child, depth - 1, alpha, beta, -1))
			if (beta<=alpha):
				break
		print (str(depth*playNum) + ") "+" "*depth +  str(beta))
		return beta
		
		

def Decis(sticks,playNum):
	if sticks<=0:
		print ("*"*33)
		if playNum > 0:
			if sticks == 0:
				print ("\tComp Win")
			else:
				print ("\Comp Lose")
		else:
			if sticks == 0:
				print ("\tComp Lose")
			else:
				print ("\tComp Win")
		print ("*"*33)
		return 0
	return 1

if __name__ == '__main__':
	sticksTotal = input("\nNo of sticks - 7,15 or 21:")
	depth = 4
	currPlay = 0
	while (currPlay != 1) and (currPlay != -1):
		currPlay = input("\nEnter 1 to play first, else enter -1:")
	node2 = Node(depth,currPlay,sticksTotal)
	print repr(node2)
	
	


	if currPlay == 1:
		print("Player to pick up stick. Pick 1,2 or 3 sticks")

	while(sticksTotal>0):
		if currPlay == 1:
			print("\n%d sticks remain. Pick number" %sticksTotal)
			choice = input("\n1,2 or 3:")
			while (choice>3) or (choice>sticksTotal):
				print("\n%d sticks remain. Wrong input. Pick number" %sticksTotal)
				choice = input("\n1,2 or 3:")
			sticksTotal-= int(float(choice))
		else:
			currPlay = 1
		if Decis(sticksTotal, currPlay):
			currPlay*=-1
			node = Node(depth,currPlay,sticksTotal)
			bestChoice = -100
			bestVal = -currPlay*maxsize
			for i in range(len(node.children)):
				nChild = node.children[i]
				newVal = AlphaBeta(nChild, depth, maxsize, -maxsize, currPlay)
				if (abs(currPlay*maxsize-newVal) <= abs(currPlay*maxsize-bestVal)):
					bestVal = newVal
					bestChoice = i
			bestChoice +=1
			if (bestChoice>sticksTotal):
				bestChoice = sticksTotal
			print ("Comp chooses: "+str(bestChoice) + "\tBased on value: " + str(bestVal))
			sticksTotal -= bestChoice
			Decis(sticksTotal, currPlay)
		currPlay*=-1
		 
