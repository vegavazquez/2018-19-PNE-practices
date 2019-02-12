from Seq import Seq

s1 = Seq ("AGTACACTGGT")
s2 = Seq ("CGTAAC")
s3 = s1.complement()
s4 = s3.reverse()

#Seq 1
print ("Sequence 1: "+s1.get_strbase())
print ("Length: "+str (s1.len()))
print ("Bases count: A:"+str(s1.count("A"))+", T:"+str(s1.count("T"))+", C:"+str(s1.count("C"))+", G:"+str(s1.count("G")) )
print ("Bases percentage: A:"+str(s1.perc("A"))+"%, T:"+str(s1.perc("T"))+"%, C:"+str(s1.perc("C"))+"%, G:"+str(s1.perc("G")) )
print ("")

#Seq 2
print ("Sequence 2: "+s2.get_strbase())
print ("Length: "+str (s2.len()))
print ("Bases count: A:"+str(s2.count("A"))+", T:"+str(s2.count("T"))+", C:"+str(s2.count("C"))+", G:"+str(s2.count("G")) )
print ("Bases percentage: A:"+str(s2.perc("A"))+"%, T:"+str(s2.perc("T"))+"%, C:"+str(s2.perc("C"))+"%, G:"+str(s2.perc("G")) )
print ("")

#Seq 3
print ("Sequence 3: "+s3.get_strbase())
print ("Length: "+str (s3.len()))
print ("Bases count: A:"+str(s3.count("A"))+", T:"+str(s3.count("T"))+", C:"+str(s3.count("C"))+", G:"+str(s3.count("G")) )
print ("Bases percentage: A:"+str(s3.perc("A"))+"%, T:"+str(s3.perc("T"))+"%, C:"+str(s3.perc("C"))+"%, G:"+str(s3.perc("G")) )
print ("")

#Seq 4
print ("Sequence 4: "+s4.get_strbase())
print ("Length: "+str (s4.len()))
print ("Bases count: A:"+str(s4.count("A"))+", T:"+str(s4.count("T"))+", C:"+str(s4.count("C"))+", G:"+str(s4.count("G")) )
print ("Bases percentage: A:"+str(s4.perc("A"))+"%, T:"+str(s4.perc("T"))+"%, C:"+str(s4.perc("C"))+"%, G:"+str(s4.perc("G")) )
print ("")