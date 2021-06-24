
stuId ={
    303 : "Afrin",
    "102" : "Prova",
    "103" : "Abruna"

}
print(stuId[303]) # giving a wrong key , it will be error output
print(stuId.get("109")) # , it will be None
print(stuId.get("108","Not a valid key")) # it will show "not a valit key" output