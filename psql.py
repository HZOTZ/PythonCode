#!/usr/bin/env python
#-*-coding:utf-8-*-


import psycopg2 
import threadpool as tp
import time 

global cur
global cursor
num = 200 
'''
	缺点：
			1.模糊查询匹配不够好，搜索时间长
			2.感觉代码还能再减点
			3.文本处理那个方法也可以改成多线程的
'''
def deal_file():
	fo = open('zi1.txt', 'w')
	for name in ['zi.txt']:
	    fi = open(name)
	    while True:
	    	s = fi.readline()
	    	s=s.split(',')[0]#读取每行，以“,”分隔，去第一组的字符串 
	        print "OK"
	        if not s:
	        	print "Finish!"
	    		break
	        fo.write(s+'\n')
	    fi.close()
	fo.close()

def connectdb():
	try:
		conn = psycopg2.connect("dbname='test' user='postgres' password='root' host='127.0.0.1'  port='5432'")  
		print "\n connection successful \n"
		return conn
		
	except Exception, e:
		print "\n connection Failed \n"
	

def Insertdb_thread(args):
    flag = 0
    urllist = open('./7001.txt', 'r')
    for url in urllist.readlines():
        url = url.strip('\n')
        try:
            sql='INSERT INTO test (domain) VALUES (\'%s\')'
            cursor.execute(sql%url)
            cur.commit()
        except:
            print "[ERROR] [%s] %s\n" % (flag, url)
            continue

        flag += 1
        print "[%s] %s \n" % (flag, url)



def getsubdomain(cursor,domain):
	sql='SELECT domain from test where domain~*\'%s\';'#模糊查询
	cursor.execute(sql%domain)
	results=cursor.fetchall()#所行已返回
	array=[]
	for r in results:
		r=''.join(list(r))#将返回的tuple元组转换成list列表 
		array.append(r)#加入数组中
	return  array#返回数组

def circlescan(cur,cursor):
	cursor.close()
	cur.close()
	
if __name__ == '__main__':
	#处理子域名文本
	deal_file()
	#连接数据库,创建连接对象
	cur=connectdb()
	#获得游标
	cursor=cur.cursor()

	
	#利用多线程插入数据
	args = range(0,-1)
	start=time.time()
	Insertdb_thread(args)
	#线程池编写
	pool = tp.ThreadPool(num)
	reqs = tp.makeRequests(Insertdb_thread, args)
	[pool.putRequest(req) for req in reqs]
	pool.wait()
	pool.dismissWorkers(num, do_join=True)
	end=time.time()
	print("multithread using %.5f seocnds"%(end-start))
	print "Done.\n"

	#Insertdb(cur)#插入数据


	domain=str(raw_input("Input main domain:"))
	#获得子域名
	domain=getsubdomain(cursor,domain)
	print domain
	#关闭游标和连接
	circlescan(cur,cursor)
	