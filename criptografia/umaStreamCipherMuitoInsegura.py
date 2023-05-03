def prng(key, length):
    keystream = bytearray(key)
    for i in range(2, length):
        keystream.append((keystream[i-1] + keystream[i-2]) % 256)
    return keystream

ciphertext = bytes.fromhex('6b5d05c42ed2a85479dcbde616cd7178fbeb38471cc37bd6fdf81c35edd158b577f9abdab51cb36a2e5628f7ed307d07e2dcf8f06bb3c014b661bf91a08c146efa6898c47074776b527ce990fff674fac415fe619a6fc2a72e7a4a2c0c916fba889cc6162e11e88c1a1afe34e6cffeddedea69c5c7046d5ff97999a4fb06932624ebe15705a353cd6b9578716c7f6a40615caf24623241c467a8fec2e949c2fdff1e9c443ce178b39cbbf976276396758b9cadbfceca2ebfcd7c8886df046aeed0')
key = bytes.fromhex('2d3c')

keystream = prng(key, len(ciphertext))
plaintext = bytes([ciphertext[i] ^ keystream[i] for i in range(len(ciphertext))])
print(plaintext.decode())
#plain text
#Fala ai Lucas! Eu acabei de criar um PRG mas acho que a chave está muito pequena, você acha que os bixos são capazes de quebrar? Por enquanto, fala pra eles que a flag é Ganesh{ForçaBruta}