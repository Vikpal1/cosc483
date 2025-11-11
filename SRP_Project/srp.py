import hashlib
import random
import math

p = 233000556327543348946447470779219175150430130236907257523476085501968599658761371268535640963004707302492862642690597042148035540759198167263992070601617519279204228564031769469422146187139698860509698350226540759311033166697559129871348428777658832731699421786638279199926610332604408923157248859637890960407
g = 5

#a = random.randint(1, p-1)
#print(a)

a = 169898110038228991132223955166432706499190986383944325941544292818973659967023664389076940495833044662891780765186714280374186209021585420267521137858196849726624119178120659520284458644491262851137782230375341756181993768315722006199014944374539185294855147228431975029228013960919234933808709937879008357806

ga = pow(g,a,p)
print(ga)
ga = 146462406569631426770742412577369640166512322441712796761535842088574279323198183126665542913606479884142210983261282163453025503988857729700726289536241499850663063385873242687265928596855359438989047579352054851804301145081851069228815616217569696554170759737183971366723316943487158021724070723037031582774

password = "ultraproud"
asciipass = password.encode("ascii")
salt = 0xfffcb83c

print(asciipass)
saltbytes = salt.to_bytes(4, 'big')
print(saltbytes)
saltedpass =  saltbytes + asciipass

print(saltedpass)

x = hashlib.sha256(saltedpass).digest()
print(f"{x}")

for _ in range(999):
    x = hashlib.sha256(x).digest()
print("This is x:")
x = int.from_bytes(x, byteorder='big')
print(x)
x = 77759039237487199292103174350135667872259895769996042948083094781226090741939

p_bytes = p.to_bytes((p.bit_length() + 7) // 8, 'big')
g_bytes = g.to_bytes(1, 'big')
print(p_bytes)
print(g_bytes)
pg_bytes = p_bytes + g_bytes

k = hashlib.sha256(pg_bytes).hexdigest()
k = int(k,16)
print(k)

B_ = 19007204720075987050667963099121007535085287175717243221954821388399340555062784698533428027052714464864974833069438817141393184597803758702123763104650427540708852707542025824371682778325085034232679330552849109138320241614144809716371943685171864855107066430219268071592224431316936209075529378458176283358


v = pow(g,x,p)
gb = (B_ - k*v) % p

print("this is gb")
print(gb)

ga_byte = ga.to_bytes((ga.bit_length() + 7) // 8, 'big')
gb_byte = gb.to_bytes((gb.bit_length() + 7) // 8, 'big')

u = hashlib.sha256(ga_byte + gb_byte).hexdigest()
u = int(u,16)
print("This is u:")
print(u)

shared_key = pow(gb,(a+u*x),p)
print("Shared key")
print(shared_key)


# Start M1 and M2
hp = hashlib.sha256(p_bytes).digest()
hg = hashlib.sha256(g_bytes).digest()

ihp = int.from_bytes(hp, byteorder='big')
ihg = int.from_bytes(hg, byteorder='big')

hpg = ihp ^ ihg
print("HP XOR WITH HG")
print(hpg)
hpg_bytes = hpg.to_bytes((hpg.bit_length() + 7) // 8, 'big')
print(hpg_bytes)

netid = "vpotter2"
netid = netid.encode("ascii")
print(netid)
netid_hash = hashlib.sha256(netid).digest()
print("This is the netid hash")
print(netid_hash)

shared_key_bytes = shared_key.to_bytes((shared_key.bit_length() + 7) // 8, 'big')
print(shared_key_bytes)

M_1 = hpg_bytes + netid_hash + saltbytes + ga_byte + gb_byte + shared_key_bytes
#print(M_1)
M_1_bytes = hashlib.sha256(M_1).digest()
print("This is M1")
print(M_1_bytes.hex())


M_2 = (ga_byte + M_1_bytes + shared_key_bytes)
M_2_Hex = hashlib.sha256(M_2).hexdigest()
print("This is M2")
print(M_2_Hex)