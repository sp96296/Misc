char = "絨"
encoded = char.encode()
test = "𫠕"
encoded = test.encode("utf-8")
decodeEscape = encoded.decode('unicode-escape')
encodedStr = encoded.decode("utf-8")
print(encoded, decodeEscape ,encodedStr)

