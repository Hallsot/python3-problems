def is_year_leap(year):
	if divmod(year/2, 2)[1] == 0.0: 
		return True
	else: 
		return False
