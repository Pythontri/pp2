import re 

def repl(obj):
   return "_" + obj.group(1).casefold()

pattern = r"([A-Z][a-z]*)"

def test(pattern, Data, Number, Result):
    x = re.sub(pattern, repl, Data)
    p = r"\b_"
    x = re.sub(p, "", x)
    print(x)
    if x == Result:
        print(Number + " is passed!")
    else: 
        print(Number + " is not passed!")

test(pattern, "MySuperTest", "Test 1", "my_super_test")
test(pattern, "ATiZheDelaeshLabyImGhoul", "Test 2", "a_ti_zhe_delaesh_laby_im_ghoul")
test(pattern, "SkazhiPrivetMame", "Test 3", "skazhi_privet_mame")
test(pattern, "CryMeARiver", "Test 4", "cry_me_a_river")
test(pattern, "HELLO", "Test 4", "h_e_l_l_o")