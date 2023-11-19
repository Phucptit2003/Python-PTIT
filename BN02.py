from heapq import heappush, heappop
from collections import defaultdict

def huffman_encoding(source_dict):
    elsym = source_dict['elsym']
    elprob = source_dict['elprob']
    huffman_dict = {'source': source_dict['source'], 'elsym': elsym, 'elprob': elprob}
    code_len = len(elsym)
    
    heap = [[weight, [symbol, ""]] for symbol, weight in zip(elsym, elprob)]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    huffman_code = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    elcodeword = [code[1] for code in huffman_code]
    
    huffman_dict['elcodeword'] = elcodeword
    
    return huffman_dict

def encode_text(text, encoding_dict):
    elsym = encoding_dict['elsym']
    elcodeword = encoding_dict['elcodeword']
    encoding = dict(zip(elsym, elcodeword))
    encoded_text = ''.join(encoding[char] for char in text)
    return encoded_text

def huffman_decoding(coded_text, encoding_dict):
    elcodeword = encoding_dict['elcodeword']
    elsym = encoding_dict['elsym']
    decoding = dict(zip(elcodeword, elsym))
    decoded_text = ''
    current_code = ''
    for char in coded_text:
        current_code += char
        if current_code in decoding:
            decoded_text += decoding[current_code]
            current_code = ''
    return decoded_text

def calculate_encoding_parameters(encoding_dict):
    elcodeword = encoding_dict['elcodeword']
    avg_l = sum(len(code) for code in elcodeword) / len(elcodeword)
    sigma_l_2 = sum((len(code) - avg_l) ** 2 for code in elcodeword) / len(elcodeword)
    
    encoding_dict['avg_l'] = avg_l
    encoding_dict['sigma_l_2'] = sigma_l_2
    encoding_dict['isNewLess'] = 1  # Chìm nhất
    encoding_dict['isLeftBrachZero'] = 1  # Nhánh trái bằng 0
    
    return encoding_dict

def display_encoding_info(encoding_dict):
    print("Source: {}".format(encoding_dict['source']))
    print("Elements: {}".format(encoding_dict['elsym']))
    print("Element Probabilities: {}".format(encoding_dict['elprob']))
    print("Element Codewords: {}".format(encoding_dict['elcodeword']))
    print("Average Length: {}".format(encoding_dict['avg_l']))
    print("Variance of Length: {}".format(encoding_dict['sigma_l_2']))
    print("isNewLess: {}".format(encoding_dict['isNewLess']))
    print("isLeftBranchZero: {}".format(encoding_dict['isLeftBrachZero']))

# Ví dụ sử dụng
source_dict = {
    'source': 'X',
    'elsym': ['x_1', 'x_2', 'x_3', 'x_4'],
    'elprob': [0.125, 0.25, 0.125, 0.5]
}

encoding_dict = huffman_encoding(source_dict)
encoded_text = encode_text("x_1x_2x_3", encoding_dict)
decoded_text = huffman_decoding(encoded_text, encoding_dict)
encoding_dict = calculate_encoding_parameters(encoding_dict)

display_encoding_info(encoding_dict)
print("Encoded Text: {}".format(encoded_text))
print("Decoded Text: {}".format(decoded_text))
