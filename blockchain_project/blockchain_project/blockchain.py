import hashlib
import random
import math


def find_block(prev_block, quote):
    nonce = 0

    prev_block = bytes.fromhex(prev_block)
    byte_quote = quote.encode("ascii")
    #print(byte_quote)
    while True:
        byte_nonce = nonce.to_bytes((nonce.bit_length() + 7) // 8, 'big')
        combined = prev_block + byte_nonce + byte_quote
        #print(combined)
        hash = hashlib.sha256(combined).hexdigest()
        #print("This is the hash")
        #print(hash)
        if(hash[0:6] == "000000"):
            break
        nonce = nonce + 1
    print("This is the nonce for the block below:")
    print(nonce)
    return hash
    





genesis_block = "d9e049aa232d0a6c2ac45f02e1d7709a56cd828231d41f019d5388fa1a52c9e4"

block_1_quote = "Code is poetry. -- wordpress.org"
block1 = find_block(genesis_block, block_1_quote)
print("Block One Hash:")
print(block1)

block1_hash = "000000efb410e6acfeb843c083946007672ed6680c8b66809c845e6bf3bb7d19"
block_2_quote = "The ability to simplify means to eliminate the unnecessary so that the necessary may speak. -- Hans Hofmann"
block2 = find_block(block1_hash, block_2_quote)
print("Block Two Hash:")
print(block2)


block2_hash = "000000e67075c09da2884a26d55b12f97a02df7c4dbf79a3ac8f321d234f30a9"
block_3_quote = "The purpose of abstraction is not to be vague, but to create a new semantic level in which one can be absolutely precise. -- Edsger Dijkstra"
block3 = find_block(block2_hash, block_3_quote)
print("Block Three Hash:")
print(block3)

block3_hash = "000000d9875709f2c11b0a5c8d83762a7b90ec730ea971973c326cafdff899c8"
block_4_quote = "The great dividing line between success and failure can be expressed in five words: \"I did not have time.\" -- WestHost weekly newsletter 14 Feb 2003"
block4 = find_block(block3_hash, block_4_quote)
print("Block Four Hash:")
print(block4)

block4_hash = "000000a149533bd47a07fb6dc459fa4ac79acecb3dd03c22f8fd92dcdd4eea0c"
block_5_quote = "For complex systems, the compiler and development environment need to be in the same language that its supporting. It's the only way to grow code. -- Alan Kay"
block5 = find_block(block4_hash, block_5_quote)
print("Block Five Hash:")
print(block5)

block5_hash = "00000044c49a29e55f22936e3fbac0b14fc4bddb34693093b36e0834d24a5575"
block_6_quote = "Linux is only free if your time has no value. -- Jamie Zawinski"
block6 = find_block(block5_hash, block_6_quote)
print("Block Six Hash:")
print(block6)

block6_hash = "000000a1b62114e1b24bbfa10c8111ea46422919063a0230ba2cbd87936b0df8"
block_7_quote = "If something isn't working, you need to look back and figure out what got you excited in the first place. -- David Gorman (ImThere.com)"
block7 = find_block(block6_hash, block_7_quote)
print("Block Seven Hash:")
print(block7)

block7_hash = "00000088dedf128cdb8e5ac44179bbccd5321a3c650a913ecfc6333ec7f80d58"
block_8_quote = "If you tell the truth, you don't have to remember anything. -- Mark Twain"
block8 = find_block(block7_hash, block_8_quote)
print("Block Eight Hash:")
print(block8)

block8_hash = "000000a7e24eb9b2dab9bbf4771d6bbb74a3bcb4eecd0ac4342744529fc67b62"
block_9_quote = "A little learning is a dangerous thing. -- Alexander Pope"
block9 = find_block(block8_hash, block_9_quote)
print("Block Nine Hash:")
print(block9)

block9_hash = "000000c2dd3d2ecfa2fedd48f308bba4599cb8b892ba3994c1ec0067473229e6"
block_10_quote = "Every man prefers belief to the exercise of judgment. -- Seneca"
block10 = find_block(block9_hash, block_10_quote)
print("Block Ten Hash:")
print(block10)

