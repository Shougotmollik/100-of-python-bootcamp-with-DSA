#looping through all key-value pairs 

#store people's favourite language

fav_lang={
    'shougot':'pyhton',
    'mollik':'c++',
    'jen':'java',
    'phill':'go'
}

#show each person's favaurite language 

for name,language in fav_lang.items():
    print(f"{name} : {language}")

#looping through all the keys 

#showing everyone's taken the servey 

for name in fav_lang.keys():
    print(name)

#looping through all the values 

#show al the language that have been chosen.

for language in fav_lang.values():
    print(language)

#looping through all the keys in order 

#showing each person favourite language in order by the persons name 

for name in sorted(fav_lang.keys()):
    print(f"{name}:{language}") 

