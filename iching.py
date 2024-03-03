# python implimentation of various i-ching divination methods

from random import randrange

def threecoin():
    hexagram = ""
    l = 0
    while l < 6:
        toss, t = [], 0
        while t < 3:
            t += 1
            toss.append(randrange(2,4)) #value between 2 and 3, coin flip
        #print(toss)
        if sum(toss) == 6:
            hexagram += '0'
        elif sum(toss) == 7:
            hexagram += '0'
        elif sum(toss) == 8:
            hexagram += '1'
        else:
            hexagram += '1'
        l += 1
    return hexagram
            
def mod_threecoin():
    '''not implimented'''

def yarrowstalks():
    '''not implimented'''

iching_hexagrams =  iching_hexagrams = [
    {"number": 1, "icon": "\u4dc0", "chinese_name": "\u4e16", "chinese_transliteration": "Qián", "english_name": "The Creative", "unicode_name": "Hexagram For the Creative Heaven", "binary_sequence": "111111"},
    {"number": 2, "icon": "\u4dc1", "chinese_name": "\u5764", "chinese_transliteration": "Kūn", "english_name": "The Receptive", "unicode_name": "Hexagram For the Receptive Earth", "binary_sequence": "000000"},
    {"number": 3, "icon": "\u4dc2", "chinese_name": "\u5c6f", "chinese_transliteration": "Zhūn", "english_name": "Difficulty at the Beginning", "unicode_name": "Hexagram For Difficulty at the Beginning", "binary_sequence": "010001"},
    {"number": 4, "icon": "\u4dc3", "chinese_name": "\u8499", "chinese_transliteration": "Mēng", "english_name": "Youthful Folly", "unicode_name": "Hexagram For Youthful Folly", "binary_sequence": "100010"},
    {"number": 5, "icon": "\u4dc4", "chinese_name": "\u9700", "chinese_transliteration": "Xū", "english_name": "Waiting", "unicode_name": "Hexagram For Waiting", "binary_sequence": "010000"},
    {"number": 6, "icon": "\u4dc5", "chinese_name": "\u8a00", "chinese_transliteration": "Sòng", "english_name": "Conflict", "unicode_name": "Hexagram For Conflict", "binary_sequence": "100101"},
    {"number": 7, "icon": "\u4dc6", "chinese_name": "\u5e2b", "chinese_transliteration": "Shī", "english_name": "The Army", "unicode_name": "Hexagram For the Army", "binary_sequence": "010010"},
    {"number": 8, "icon": "\u4dc7", "chinese_name": "\u6bd2", "chinese_transliteration": "Bǐ", "english_name": "Holding Together", "unicode_name": "Hexagram For Holding Together", "binary_sequence": "111010"},
    {"number": 9, "icon": "\u4dc8", "chinese_name": "\u5c0f\u755c", "chinese_transliteration": "Xiǎo Chù", "english_name": "Small Taming", "unicode_name": "Hexagram For Small Taming", "binary_sequence": "010010"},
    {"number": 10, "icon": "\u4dc9", "chinese_name": "\u5c65", "chinese_transliteration": "Lǚ", "english_name": "Treading", "unicode_name": "Hexagram For Treading", "binary_sequence": "111011"},
    {"number": 11, "icon": "\u4dca", "chinese_name": "\u6cf0", "chinese_transliteration": "Tài", "english_name": "Peace", "unicode_name": "Hexagram For Peace", "binary_sequence": "100001"},
    {"number": 12, "icon": "\u4dcb", "chinese_name": "\u5426", "chinese_transliteration": "Pǐ", "english_name": "Standstill", "unicode_name": "Hexagram For Standstill", "binary_sequence": "000000"},
    {"number": 13, "icon": "\u4dcc", "chinese_name": "\u540c\u4eba", "chinese_transliteration": "Tóng Rén", "english_name": "Fellowship with Men", "unicode_name": "Hexagram For Fellowship with Men", "binary_sequence": "010010"},
    {"number": 14, "icon": "\u4dcd", "chinese_name": "\u5927\u6709", "chinese_transliteration": "Dà Yǒu", "english_name": "Possession in Great Measure", "unicode_name": "Hexagram For Possession in Great Measure", "binary_sequence": "111111"},
    {"number": 15, "icon": "\u4dce", "chinese_name": "\u8c26", "chinese_transliteration": "Qiān", "english_name": "Modesty", "unicode_name": "Hexagram For Modesty", "binary_sequence": "101000"},
    {"number": 16, "icon": "\u4dcf", "chinese_name": "\u8c6b", "chinese_transliteration": "Yù", "english_name": "Enthusiasm", "unicode_name": "Hexagram For Enthusiasm", "binary_sequence": "000101"},
    {"number": 17, "icon": "\u4dd0", "chinese_name": "\u968f", "chinese_transliteration": "Suí", "english_name": "Following", "unicode_name": "Hexagram For Following", "binary_sequence": "101101"},
    {"number": 18, "icon": "\u4dd1", "chinese_name": "\u8821", "chinese_transliteration": "Gŭ", "english_name": "Work on the Decayed", "unicode_name": "Hexagram For Work on the Decayed", "binary_sequence": "010001"},
    {"number": 19, "icon": "\u4dd2", "chinese_name": "\u81a8", "chinese_transliteration": "Lín", "english_name": "Approach", "unicode_name": "Hexagram For Approach", "binary_sequence": "110010"},
    {"number": 20, "icon": "\u4dd3", "chinese_name": "\u89c0", "chinese_transliteration": "Guān", "english_name": "Contemplation", "unicode_name": "Hexagram For Contemplation", "binary_sequence": "001010"},
    {"number": 21, "icon": "\u4dd4", "chinese_name": "\u5632\u55d1", "chinese_transliteration": "Shì Kè", "english_name": "Biting Through", "unicode_name": "Hexagram For Biting Through", "binary_sequence": "110101"},
    {"number": 22, "icon": "\u4dd5", "chinese_name": "\u8d31", "chinese_transliteration": "Bì", "english_name": "Grace", "unicode_name": "Hexagram For Grace", "binary_sequence": "101001"},
    {"number": 23, "icon": "\u4dd6", "chinese_name": "\u5269", "chinese_transliteration": "Bō", "english_name": "Splitting Apart", "unicode_name": "Hexagram For Splitting Apart", "binary_sequence": "010110"},
    {"number": 24, "icon": "\u4dd7", "chinese_name": "\u5fa9", "chinese_transliteration": "Fù", "english_name": "Return", "unicode_name": "Hexagram For Return", "binary_sequence": "011100"},
    {"number": 25, "icon": "\u4dd8", "chinese_name": "\u7121\u5996", "chinese_transliteration": "Wú Wàng", "english_name": "Innocence", "unicode_name": "Hexagram For Innocence", "binary_sequence": "101111"},
    {"number": 26, "icon": "\u4dd9", "chinese_name": "\u5927\u755c", "chinese_transliteration": "Dà Chù", "english_name": "Great Taming", "unicode_name": "Hexagram For Great Taming", "binary_sequence": "010010"},
    {"number": 27, "icon": "\u4dda", "chinese_name": "\u9804", "chinese_transliteration": "Yí", "english_name": "Providing Nourishment", "unicode_name": "Hexagram For Providing Nourishment", "binary_sequence": "110001"},
    {"number": 28, "icon": "\u4ddb", "chinese_name": "\u5927\u904e", "chinese_transliteration": "Dà Guò", "english_name": "Preponderance of the Great", "unicode_name": "Hexagram For Preponderance of the Great", "binary_sequence": "100111"},
    {"number": 29, "icon": "\u4ddc", "chinese_name": "\u574e", "chinese_transliteration": "Kǎn", "english_name": "The Abysmal Water", "unicode_name": "Hexagram For the Abysmal Water", "binary_sequence": "000010"},
    {"number": 30, "icon": "\u4ddd", "chinese_name": "\u96e2", "chinese_transliteration": "Lí", "english_name": "The Clinging Fire", "unicode_name": "Hexagram For the Clinging Fire", "binary_sequence": "101101"},
    {"number": 31, "icon": "\u4dde", "chinese_name": "\u54b8", "chinese_transliteration": "Xián", "english_name": "Influence", "unicode_name": "Hexagram For Influence", "binary_sequence": "011001"},
    {"number": 32, "icon": "\u4ddf", "chinese_name": "\u6052", "chinese_transliteration": "Héng", "english_name": "Duration", "unicode_name": "Hexagram For Duration", "binary_sequence": "100110"},
    {"number": 33, "icon": "\u4de0", "chinese_name": "\u905f", "chinese_transliteration": "Dùn", "english_name": "Retreat", "unicode_name": "Hexagram For Retreat", "binary_sequence": "010010"},
    {"number": 34, "icon": "\u4de1", "chinese_name": "\u5927\u58d1", "chinese_transliteration": "Dà Zhuàng", "english_name": "The Great Power", "unicode_name": "Hexagram For the Great Power", "binary_sequence": "100101"},
    {"number": 35, "icon": "\u4de2", "chinese_name": "\u6649", "chinese_transliteration": "Jìn", "english_name": "Progress", "unicode_name": "Hexagram For Progress", "binary_sequence": "101110"},
    {"number": 36, "icon": "\u4de3", "chinese_name": "\u660e\u5947", "chinese_transliteration": "Míng Yí", "english_name": "Darkening of the Light", "unicode_name": "Hexagram For Darkening of the Light", "binary_sequence": "011011"},
    {"number": 37, "icon": "\u4de4", "chinese_name": "\u5bb6\u4eba", "chinese_transliteration": "Jiā Rén", "english_name": "The Family", "unicode_name": "Hexagram For the Family", "binary_sequence": "110111"},
    {"number": 38, "icon": "\u4de5", "chinese_name": "\u776d", "chinese_transliteration": "Kuí", "english_name": "Opposition", "unicode_name": "Hexagram For Opposition", "binary_sequence": "001000"},
    {"number": 39, "icon": "\u4de6", "chinese_name": "\u8e7f", "chinese_transliteration": "Jiǎn", "english_name": "Obstruction", "unicode_name": "Hexagram For Obstruction", "binary_sequence": "000100"},
    {"number": 40, "icon": "\u4de7", "chinese_name": "\u89e3", "chinese_transliteration": "Xiè", "english_name": "Deliverance", "unicode_name": "Hexagram For Deliverance", "binary_sequence": "111001"},
    {"number": 41, "icon": "\u4de8", "chinese_name": "\u641d", "chinese_transliteration": "Sǔn", "english_name": "Decrease", "unicode_name": "Hexagram For Decrease", "binary_sequence": "000011"},
    {"number": 42, "icon": "\u4de9", "chinese_name": "\u76ca", "chinese_transliteration": "Yì", "english_name": "Increase", "unicode_name": "Hexagram For Increase", "binary_sequence": "110100"},
    {"number": 43, "icon": "\u4dea", "chinese_name": "\u592c", "chinese_transliteration": "Guài", "english_name": "Breakthrough", "unicode_name": "Hexagram For Breakthrough", "binary_sequence": "010001"},
    {"number": 44, "icon": "\u4deb", "chinese_name": "\u59e4", "chinese_transliteration": "Gòu", "english_name": "Coming to Meet", "unicode_name": "Hexagram For Coming to Meet", "binary_sequence": "111100"},
    {"number": 45, "icon": "\u4dec", "chinese_name": "\u8423", "chinese_transliteration": "Cuì", "english_name": "Gathering Together", "unicode_name": "Hexagram For Gathering Together", "binary_sequence": "001101"},
    {"number": 46, "icon": "\u4ded", "chinese_name": "\u5347", "chinese_transliteration": "Shēng", "english_name": "Pushing Upward", "unicode_name": "Hexagram For Pushing Upward", "binary_sequence": "101000"},
    {"number": 47, "icon": "\u4dee", "chinese_name": "\u56f0", "chinese_transliteration": "Kùn", "english_name": "Oppression", "unicode_name": "Hexagram For Oppression", "binary_sequence": "000010"},
    {"number": 48, "icon": "\u4def", "chinese_name": "\u4e95", "chinese_transliteration": "Jǐng", "english_name": "The Well", "unicode_name": "Hexagram For the Well", "binary_sequence": "100000"},
    {"number": 49, "icon": "\u4df0", "chinese_name": "\u9769", "chinese_transliteration": "Gé", "english_name": "Revolution", "unicode_name": "Hexagram For Revolution", "binary_sequence": "111101"},
    {"number": 50, "icon": "\u4df1", "chinese_name": "\u9f0e", "chinese_transliteration": "Dǐng", "english_name": "The Caldron", "unicode_name": "Hexagram For the Caldron", "binary_sequence": "010110"},
    {"number": 51, "icon": "\u4df2", "chinese_name": "\u9707", "chinese_transliteration": "Zhèn", "english_name": "Arousing Thunder", "unicode_name": "Hexagram For Arousing Thunder", "binary_sequence": "110101"},
    {"number": 52, "icon": "\u4df3", "chinese_name": "\u805a\u5bfb", "chinese_transliteration": "Gèn", "english_name": "Keeping Still", "unicode_name": "Hexagram For Keeping Still", "binary_sequence": "010010"},
    {"number": 53, "icon": "\u4df4", "chinese_name": "\u5f0f", "chinese_transliteration": "Jiàn", "english_name": "Development", "unicode_name": "Hexagram For Development", "binary_sequence": "111100"},
    {"number": 54, "icon": "\u4df5", "chinese_name": "\u8c08\u5408", "chinese_transliteration": "Guī Mèi", "english_name": "The Marrying Maiden", "unicode_name": "Hexagram For the Marrying Maiden", "binary_sequence": "001111"},
    {"number": 55, "icon": "\u4df6", "chinese_name": "\u4f2a", "chinese_transliteration": "Fēng", "english_name": "Abundance", "unicode_name": "Hexagram For Abundance", "binary_sequence": "101111"},
    {"number": 56, "icon": "\u4df7", "chinese_name": "\u65e0\u6c34", "chinese_transliteration": "Lǚ", "english_name": "The Wanderer", "unicode_name": "Hexagram For the Wanderer", "binary_sequence": "111010"},
    {"number": 57, "icon": "\u4df8", "chinese_name": "\u95f4\u9699", "chinese_transliteration": "Xùn", "english_name": "The Gentle", "unicode_name": "Hexagram For the Gentle", "binary_sequence": "011011"},
    {"number": 58, "icon": "\u4df9", "chinese_name": "\u878d", "chinese_transliteration": "Duì", "english_name": "The Joyous", "unicode_name": "Hexagram For the Joyous Lake", "binary_sequence": "110110"},
    {"number": 59, "icon": "\u4dfa", "chinese_name": "\u6c42\u9a8c", "chinese_transliteration": "Huàn", "english_name": "Dispersion", "unicode_name": "Hexagram For Dispersion", "binary_sequence": "000110"},
    {"number": 60, "icon": "\u4dfb", "chinese_name": "\u7ed3\u4e8e", "chinese_transliteration": "Jié", "english_name": "Limitation", "unicode_name": "Hexagram For Limitation", "binary_sequence": "011000"},
    {"number": 61, "icon": "\u4dfc", "chinese_name": "\u8c37", "chinese_transliteration": "Zhōng Fú", "english_name": "Inner Truth", "unicode_name": "Hexagram For Inner Truth", "binary_sequence": "100110"},
    {"number": 62, "icon": "\u4dfd", "chinese_name": "\u4eba\u5f71", "chinese_transliteration": "Xiǎo Guó", "english_name": "Preponderance of the Small", "unicode_name": "Hexagram For Preponderance of the Small", "binary_sequence": "011001"},
    {"number": 63, "icon": "\u4dfe", "chinese_name": "\u8ff0\u9053", "chinese_transliteration": "Jì Jǐ", "english_name": "After Completion", "unicode_name": "Hexagram For After Completion", "binary_sequence": "101100"},
    {"number": 64, "icon": "\u4dff", "chinese_name": "\u672a\u59cb\u6210", "chinese_transliteration": "Wèi Jì", "english_name": "Before Completion", "unicode_name": "Hexagram For Before Completion", "binary_sequence": "001101"}
]

'''
for hexagram in iching_hexagrams:
    print(f"Hexagram {hexagram['number']}:")
    print(f"Icon: {hexagram['icon']}")
    print(f"Chinese Name: {hexagram['chinese_name']}")
    print(f"Transliteration: {hexagram['chinese_transliteration']}")
    print(f"English Name: {hexagram['english_name']}")
    print(f"Unicode Name: {hexagram['unicode_name']}")
    print(f"Binary Sequence: {hexagram['binary_sequence']}")
    print()
'''

def find_hexagram_by_binary_sequence(binary_sequence):
    for hexagram in iching_hexagrams:
        if hexagram['binary_sequence'] == binary_sequence:
            return hexagram
    return None

print(threecoin())

hexagram = find_hexagram_by_binary_sequence(threecoin())
if hexagram:
    print(f"Found hexagram: {hexagram['icon']} - {hexagram['english_name']}")
else:
    print("No hexagram found with the given binary sequence.")
