#! /usr/bin/env python
# -*- coding: utf-8 -*-

#########module##############

import os,sys,time,re

def fun_read_bed(PATH):
	try:
		FILE_IN=open(PATH,"r")
	except IOError:
		print "There is no file in %s"%PATH
		os._exit(0)
	LIST_BED=[]
	while True:
		LINE=FILE_IN.readline().split()
		if not LINE:
			break
		LINE[1]=int(LINE[1])
		LINE[2]=int(LINE[2])
		LIST_BED.append(LINE)
	return LIST_BED

def fun_read_bed_into_dict(PATH):
	try:
		FILE_IN=open(PATH,"r")
	except IOError:
		print "There is no file in %s"%PATH
		os._exit(0)
	DICT_BED={}
	while True:
		LINE=FILE_IN.readline().split()
		if not LINE:
			break
		LINE[1]=int(LINE[1])
		LINE[2]=int(LINE[2])
		NAME=LINE[3]
		if len(LINE)>4:
			LINE=LINE[0:3]+LINE[4:]
		else:
			LINE=LINE[0:3]
		DICT_BED[NAME]=LINE
	return DICT_BED

def fun_read_chrom_size(PATH):
	try:
		FILE_IN=open(PATH,"r")
	except IOError:
		print "There is no file in %s"%PATH
		os._exit(0)
	DICT_CHROM_SIZE={}
	while True:
		LINE=FILE_IN.readline().split()
		if not LINE:
			break
		DICT_CHROM_SIZE[LINE[0]]=int(LINE[1])
	return DICT_CHROM_SIZE

def fun_write_list(LIST, PATH):
	try:
		FILE_OUT=open(PATH,"w")
	except IOError:
		print "Cannot create %s"%PATH
		os._exit(0)
	for i in LIST:
		for j in range(len(i)-1):
			FILE_OUT.write("%s\t"%i[j])
		FILE_OUT.write("%s\n"%i[len(i)-1])

def fun_quick_write(CONTENT, PATH):
	try:
		FILE_OUT=open(PATH,"w")
	except IOError:
		print "Cannot create %s"%PATH
		os._exit(0)
	FILE_OUT.write(CONTENT)
	FILE_OUT.close()



