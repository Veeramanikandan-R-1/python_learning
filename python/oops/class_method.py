class subject:
	fav_sub="mani"
	def fav_sub_method(self):
		print("my fav subject is {}".format(self.fav_sub))
subject.fav_sub_method=classmethod(subject.fav_sub_method)
subject.fav_sub_method()
