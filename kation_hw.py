# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#!/usr/bin/env python
# -*- coding:utf8 -*-
"homework - string fuctions"

def xfind(src_find, sub_str):
    "== src_find.find(sub_str)"

    if sub_str == "":
        return 0
        
    pos = 0
    
    while pos < len(src_find):
        if src_find[pos:pos + len(sub_str)] == sub_str:
            return pos
        else:
            pos += 1

    return -1

def xreplace(src_replace, old, new):
    "== src_replace.replace(old, new)"

    replced = ""

    if old == "":
        for src_replace_part in src_replace:
            replced += new + src_replace_part
        replced += new
        return replced

    replced = src_replace
    pos = 0

    while pos < len(replced):
        if replced[pos:pos + len(old)] == old:
            replced = replced[0:pos] + new + replced[pos+len(old):len(replced)]
            pos = pos + len(new)
        else:
            pos += 1

    return replced

def xsplit(src_split, splitter):
    "== src_split.split(splitter)"

    splitted_array = []

    if splitter == "":
        raise ValueError("empty separator")

    pos = 0
    start_pos = 0
    end_pos = 0

    while pos < len(src_split):
        if src_split[pos:pos + len(splitter)] == splitter:
            end_pos = pos
            splitted_array.append(src_split[start_pos:end_pos])
            pos = pos + len(splitter)
            start_pos = pos
        else:
            pos += 1

    splitted_array.append(src_split[start_pos:len(src_split)])

    return splitted_array

def xjoin(separator, join_array):
    "== separator.join(join_array)"

    res_join = ""

    if join_array.count == 0:
        return ""

    if join_array.count == 1:
        return join_array[0]

    for join_arary_part in join_array:
        res_join += separator + join_arary_part

    res_join = res_join[len(separator):len(res_join)]

    return res_join

def test_xfind():
    "unit test for find function"
    
    assert xfind("a", "a") == 0
    assert xfind("eatya", "a") == 1
    assert xfind("bbafad", "ad") == 4
    assert xfind("aba", "abab") == -1
    assert xfind("some text", "text") == 5
    assert xfind("some text 2", " ") == 4
    assert xfind("s" * 500 + "tre" + "s" * 500, "tre") == 500
    assert xfind("s" * 1000, "sf") == -1
    assert xfind("", "sf") == -1
    assert xfind("sf", "") == 0
    assert xfind("", "") == 0

def test_xreplace():
    "unit test for replace function"
    
    assert xreplace("abc", "a", "d") == "dbc"
    assert xreplace("abc", "b", "d") == "adc"
    assert xreplace("abc", "c", "d") == "abd"
    assert xreplace("abcd", "b", "ff") == "affcd"
    assert xreplace("abcd", "bc", "ff") == "affd"
    assert xreplace("abcdefgabcdef", "de", "xx") == "abcxxfgabcxxf"   
    assert xreplace("abcd", "bc", "x") == "axd"
    assert xreplace("abcd123abcd", "cd12", "__") == "ab__3abcd"
    assert xreplace("abcd", "abcde", "abcdef") == "abcd"   
    assert xreplace("(&*^%&)", "()", "__") == "(&*^%&)"
    assert xreplace("fffffffda", "ff", "1") == "111fda"
    assert xreplace("fr" * 1000, "fr", "test_") == "test_"*1000
    assert xreplace("ertw", "er", "") == "tw"
    assert xreplace("ertw", "", "1") == "1e1r1t1w1"
    assert xreplace("ertw", "", "") == "ertw"
    assert xreplace("", "", "ertv") == "ertv"
    assert xreplace("123", "", "ertv") == "ertv1ertv2ertv3ertv"
    assert xreplace("", "ertv", "") == ""
    assert xreplace("", "ertv", "11111") == ""

def test_xsplit():
    "unit test for split function"
    
    assert xsplit("a.b.c.d.e", ".") == ["a", "b", "c", "d", "e"]
    assert xsplit("aa.bbb.cccc.dd.ee", ".") == ["aa", "bbb", "cccc", "dd", "ee"]
    assert xsplit("a.xb.xc.xd.xe", ".x") == ["a", "b", "c", "d", "e"]
    assert xsplit("a.xb.c.d.xe", ".x") == ["a", "b.c.d", "e"]
    assert xsplit("a b c d e", " ") == ["a", "b", "c", "d", "e"]
    assert xsplit("a b  c d e", "  ") == ["a b", "c d e"]
    assert xsplit("", ".") == [""]
    assert xsplit("a.b.c.d.", ".") == ["a", "b", "c", "d", ""]
    assert xsplit(".b.c.d.e", ".") == ["", "b", "c", "d", "e"]
    assert xsplit(".", ".") == ["", ""]
    try:
        xsplit("a.b.c.d.e", "")
    except ValueError as inst:
        assert inst.args[0] == "empty separator"

def test_xjoin():
    "unit test for join function"
    
    assert xjoin("-", ["a", "b", "c", "d", "e"]) == "a-b-c-d-e"
    assert xjoin("-asd-", ["a", "b", "c", "d"]) == "a-asd-b-asd-c-asd-d"
    assert xjoin("---", ["a", "b"]) == "a---b"
    assert xjoin("-", ["a"]) == "a"
    assert xjoin("-", [""]) == ""
    assert xjoin("", ["a", "b", "c", "d", "e"]) == "abcde"

def main():
    "main"
    test_xfind()
    test_xjoin()
    test_xreplace()
    test_xsplit()
    print "Test pass: OK"
    raw_input()
    return 0

if __name__ == "__main__":
    exit(main())
    


