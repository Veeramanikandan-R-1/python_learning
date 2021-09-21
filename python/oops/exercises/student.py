class student:
	def __init__(self,score1,score2,score3):
		self.score1=score1
		self.score2=score2
		self.score3=score3
	def summing_scores(score_list):
		sum=0	
		for value in score_list:
			sum+=value
		return sum
class result_finder(student):
	def __init__(self,score1,score2,score3):
		super().__init__(score1,score2,score3)
	def result(self):
		first_sum=student.summing_scores(self.score1)
		second_sum=student.summing_scores(self.score2)
		third_sum=student.summing_scores(self.score3)
		if(first_sum>second_sum and first_sum>third_sum):
			return 2
		elif((first_sum>second_sum and first_sum<third_sum)or(first_sum<second_sum and first_sum>third_sum)):
			return 1
		else:
			return 0
scores=result_finder([30,40,45,10,10],[40,40,40,10,10],[50,20,30,10,10])
print(scores.result())
		
