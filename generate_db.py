# encoding: utf-8
#!/usr/bin/python

import getopt,sys,MySQLdb,random,string,time

def main():
	
	need_print  = False
	count = None
	
	try:
		opts, args = getopt.getopt(sys.argv[1:], "c:p", ["count", "print"])
	except getopt.GetoptError:
		sys.eixt(2)
	
	for opt, arg in opts:
		if opt in ("-c", "--count"):
			count = arg
		
		elif opt in ("-p", "--print"):
			need_print = True

	print ("count is:",count,", need_print is:", need_print)

	# open db
	db = MySQLdb.connect(host = "localhost", user = "root", passwd="wawdsh1!")
	
	# get cursor
	cursor = db.cursor()
	
	# show version
	# cursor.execute("select version()")
	# print ("version: %s") % cursor.fetchone()
	
	# cursor.execute("show databases")
	# rows = cursor.fetchall()
	# for data in rows:
	# print (data)

	cursor.execute("use test_db")
	#cursor.execute("create table tb2 (name varchar(20), sex char(1), birth date, death date)")
		
	for i in range( int(count) ):
		name = generate_randname(10)
		birth = generate_randdate('1980-01-01','2000-12-31')
		death = generate_randdate(birth,'2030-12-31')
		sex = generate_sex()
		sql = "insert into tb2 values ('%s','%s','%s','%s')" % (name,sex,birth,death)
		if need_print:
			print sql
		cursor.execute(sql)
		time.sleep(0.05)

		# execute
		db.commit()

	# close cursor
	cursor.close()

	# close db
	db.close()

	print ("succeed")

def generate_randname(length):
	length = random.randint(3,length)
	rand_name = "".join([random.choice(string.ascii_lowercase) for _ in range(length)])
	return rand_name

def generate_randdate(start_time,end_time):
	format = '%Y-%m-%d';
	stime = time.mktime( time.strptime(start_time,format) )
	etime = time.mktime( time.strptime(end_time,format) )
	rtime = stime + random.random() * (etime-stime)
	return time.strftime(format, time.localtime(rtime))

def generate_sex():
	return random.choice('mf')
	
if __name__ == "__main__":
	main()
