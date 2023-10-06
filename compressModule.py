import zlib, base64


def compress(inputfile, outputfile):
    # open the file
    data = open(inputfile, "r").read()

    # convert the file into Bytes..!
    data_bytes = bytes(data, "utf-8")

    # Compress the file using the b64 and zlib modules
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))

    # decoding the compressed File
    decoded_data = compressed_data.decode("utf-8")

    # opening another file and writing the compressed data into it...!
    compressed_file = open(outputfile, "w")
    compressed_file.write(decoded_data)


def decompress(inputfile, outputfile):
    file_content = open(inputfile, "r").read()
    encode_data = file_content.encode("utf-8")
    decompressed_data = zlib.decompress(base64.b64decode(encode_data))
    decoded_data = decompressed_data.decode("utf-8")

    file = open(outputfile, "w")
    file.write(decoded_data)
