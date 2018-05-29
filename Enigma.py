"""
Created on Mon May 28 15:26:03 2018

@author: Utility
"""

# Run loop
# Model of enigma selection function - templates
# Freestyle settings. wheel advance, rotors, etc.
# Rotor Selection Function
# Steckerboard Setting Function
# printout of encrypted message
# be able to get machine configuration
# verify edge cases "Letter can never encrypt as itself"
# Eventual nice to haves
# Enigma Uhr
# Rewireable reflector
# output "keysheet" to csv
# "post" and "get?" am I so ambitious? (no)



#code each rotor wiring to an array so that for later
#stepping operations index can be used to calculate 
#wiring position of wheel in a straightforward
#fashion (I bet a hash would do this faster, but
#I'm just gonna hack at this until I see daylight :D)
rotor_ic = list("DMTWSILRUYQNKFEJCAZBPGXOHV")
rotor_iic = list("HQZGPJTMOBLNCIFDYAWVEUSRKX")
rotor_iiic = list("UQNTLSZFMREHDPXKIBVYGJCWOA")
# Rotors from commercial Enigma A, B - introduced 1924
rotor_i = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotor_ii = list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotor_iii = list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
# Rotors introduced in 1930 with the Enigma I
rotor_iv = list("ESOVPZJAYQUIRHXLNFTGKDCMWB")
rotor_iv = list("VZBRGITYUPSDNHLXAWMJQOFECK")
# Rotors introduced in December 1938 with the
# M3 Army model of the Enigma.
rotor_ik = list("PEZUOHXSCVFMTBGLRINQJWAYDK")
rotor_iik = list("ZOUESYDKFWPCIQXHMVBLGNJRAT")
rotor_iiik = list("EHRVXGAOBQUSIMZFLYNWKTPDJC")
rotor_ukwk = list("IMETCGFRAYSQBZXWLHKDVUPOJN")
rotor_etwk = list("QWERTZUIOASDFGHJKPYXCVBNML")
# Rotors Introduced February 1939 for the Swiss K model
rotor_vi = list("JPGVOUMFYQBENHZRDKASXLICTW")
rotor_vii = list("NZJHGRCXMYSWBOUFAIVLPEKQDT")
rotor_viii = list("FKQHTLXOCBJSPDZRAMEWNIUYGV")
# Rotors introduced in 1939 for the M3 and February 
# 1942 for the M4 Naval Enigma
rotor_refa = list("EJMZALYXVBWFCRQUONTSPIKHGD")
rotor_refb = list("YRUHQSLDPXNGOKMIEBFZCWVJAT")
rotor_refc = list("FVPJIAOYEDRZXWGCTKUQSBNMHL")
rotor_refbt = list("ENKQAUYWJICOPBLMDXZVFTHRGS")
rotor_refct = list("RDOBJNTKVEHMLFCWZAXGYIPSUQ")
#reflectors b, and c thin respectively
rotor_etw = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
rotor_beta = list("LEYJVCNIXWPBQMDRTAKZGFUHOS")
rotor_gamma = list("FSOKANUERHMBTIYCWLQPZXVGJD")
# assorted varied function rotors introduced throughout
# the enigma program.
rotor_rocket_i = list("JGDQOXUSCAMIFRVTPNEWKBLZYH")
rotor_rocket_ii = list("NTZPSFBOKMWRCJDIVLAEYUXHGQ")
rotor_rocket_iii = list("JVIUBHTCDYAKEQZPOSGXNRMWFL")
rotor_rocket_ukw = list("QYHOGNECVPUZTFDJAXWMKISRBL")
rotor_rocket_etw = list("QWERTZUIOASDFGHJKPYXCVBNML")
# Rotors introduced February 7 1941 "German Railway"
# "(Rocket)" rotors.

