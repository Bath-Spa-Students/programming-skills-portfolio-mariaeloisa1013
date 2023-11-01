
ppl = ["phoebe", "rinoa","marwa"]
list = ppl 
msg = "come have dinner with us, "

#invitations
print ( "invitations")
print ( "\t" + msg + ppl[0])
print ( "\t" + msg + ppl[1])
print ( "\t" + msg + ppl[2])

#alexa can't come
print ("Hello " + ppl[1] + ". Sadly, we only have a table for two. Sorry we can't provide any more seats.")
newppl = ppl.pop(1)
print ("\tnew list: ", ppl) 



#invitations pt 2
print ("new invitations")
print ( "\t"  + msg + ppl[0])
print ( "\t"  + msg + ppl[1])

#empty list
del ppl[1]
del ppl[0]
print ("list:", ppl)
